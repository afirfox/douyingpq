import json

def format_json_to_text(input_file='douyin_cleaned_data.json', output_file='抖音笔记内容（已整理）.txt'):
    """
    读取清理后的JSON文件，并将其内容格式化为一个易于阅读的文本文件。

    Args:
        input_file (str): 清理后的JSON文件名。
        output_file (str): 输出的文本文档名。
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 错误：找不到输入文件 '{input_file}'。请确保它和脚本在同一个文件夹下。")
        return
    except json.JSONDecodeError:
        print(f"❌ 错误：文件 '{input_file}' 格式不正确，无法解析。")
        return

    print("✅ 成功读取JSON文件，开始生成文本文档...")

    # --- 1. 处理作者正文（去重） ---
    raw_description = data.get("author_description", "（未找到作者正文）")
    
    # 找到核心句子的结束标志，用于切分和去重
    # 这里我们选取句子中一个独特且靠后的部分作为标志
    unique_ending = "光鲜的背后全是心酸"
    if unique_ending in raw_description:
        # 找到标志第一次出现的位置，并截取从开头到该标志结束的完整句子
        end_index = raw_description.find(unique_ending) + len(unique_ending)
        cleaned_description = raw_description[:end_index]
    else:
        # 如果找不到标志，则保留原文（作为备用方案）
        cleaned_description = raw_description

    # --- 2. 获取评论列表 ---
    comments = data.get("comments", [])

    # --- 3. 写入到新的文本文件 ---
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入文件大标题
        f.write("=" * 50 + "\n")
        f.write(" " * 12 + "抖音图文笔记内容整理\n")
        f.write("=" * 50 + "\n\n")

        # 写入作者正文部分
        f.write("-" * 20 + "\n")
        f.write("   【作者正文】\n")
        f.write("-" * 20 + "\n")
        f.write(cleaned_description + "\n\n")

        # 写入评论区部分
        f.write("-" * 20 + "\n")
        f.write(f"   【评论区】(共 {len(comments)} 条评论)\n")
        f.write("-" * 20 + "\n\n")

        if not comments:
            f.write("（暂无评论）\n")
        else:
            # 遍历并写入每一条评论
            for i, comment_data in enumerate(comments, 1):
                username = comment_data.get("username", "未知用户")
                comment_text = comment_data.get("comment", "")
                
                # 写入格式化的评论
                f.write(f"{i}. 用户名: {username}\n")
                f.write(f"   评论内容: {comment_text}\n")
                
                # 在每条评论之间添加分隔线，除了最后一条
                if i < len(comments):
                    f.write("\n" + "-" * 30 + "\n\n")

    print(f"🎉 任务完成！已将所有内容整理并保存到 '{output_file}' 文件中。")


if __name__ == '__main__':
    format_json_to_text()

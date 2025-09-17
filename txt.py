# compact_comments.py
# 功能：将 comment.txt 中的评论内容提取并紧凑排列，每行一条，无空行、无编号

INPUT_FILE = "douyin_final_readable.txt"
OUTPUT_FILE = "comments_compact.txt"

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 提取“评论内容: ...”这一行，并清理格式
comments = []
for line in lines:
    if "评论内容:" in line:
        # 分割出“评论内容:”之后的部分，去除首尾空格

        content = line.split("评论内容:", 1)[1].strip()
        if content:  # 非空才保留
            comments.append(content)

# 写入紧凑版文件
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for comment in comments:
        f.write(comment + '\n')

print(f"✅ 已成功提取 {len(comments)} 条评论")
print(f"📁 输出文件：{OUTPUT_FILE}")

import time
from playwright.sync_api import sync_playwright

# --- 配置 ---
COOKIE_FILE = "douyin_cookies.json"

def save_douyin_cookies():
    """
    启动浏览器，让用户手动登录，然后保存登录状态 (cookies)。
    """
    with sync_playwright() as p:
        # 启动一个有界面的浏览器
        browser = p.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()

        print("🚀 正在打开抖音首页...")
        page.goto("https://www.douyin.com/")

        # --- 用户手动操作 ---
        print("="*50)
        print("✅ 浏览器已打开，请在浏览器窗口中手动完成登录操作。")
        print("   (使用手机号、扫码等方式均可)")
        print("🔴 登录成功后，不要关闭浏览器，回到这里，然后按 Enter 键继续...")
        print("="*50)
        
        # 等待用户在终端按回车
        input()

        # --- 保存 Cookies ---
        try:
            print("正在保存登录状态...")
            context.storage_state(path=COOKIE_FILE)
            print(f"✅ 登录状态已成功保存到文件: {COOKIE_FILE}")
        except Exception as e:
            print(f"❌ 保存失败: {e}")
        finally:
            # 关闭浏览器
            browser.close()
            print("浏览器已关闭。")

if __name__ == "__main__":
    save_douyin_cookies()

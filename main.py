import flet as ft
from src.routes import Router

def main(page: ft.Page):
    # 页面基础配置
    page.title = "多功能工具箱"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    
    # 初始化路由
    router = Router(page)
    router.setup_routes()
    
    # 导航到首页
    router.navigate("/")

if __name__ == "__main__":
    ft.run(main)
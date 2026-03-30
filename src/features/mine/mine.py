# src/features/mine/mine.py - 我的页面
import flet as ft
from src.features.base_page import BasePage
from src.utils.responsive import ResponsiveConfig


class MinePage(BasePage):
    """我的页面（个人中心）"""
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        super().__init__(page, responsive)
        
        # 菜单配置
        self.menu_items = [
            {"icon": ft.Icons.SETTINGS, "title": "设置", "color": ft.Colors.BLUE},
            {"icon": ft.Icons.NOTIFICATIONS, "title": "消息通知", "color": ft.Colors.ORANGE},
            {"icon": ft.Icons.HELP, "title": "帮助与反馈", "color": ft.Colors.GREEN},
            {"icon": ft.Icons.INFO, "title": "关于我们", "color": ft.Colors.PURPLE},
        ]
    
    def build(self) -> ft.Control:
        """构建我的页面"""
        # 用户信息卡片
        user_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.PERSON, size=60, color=ft.Colors.BLUE),
                    ft.Text("用户名", size=20, weight="bold"),
                    ft.Text("用户 ID: 12345", color=ft.Colors.GREY),
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20,
            ),
            elevation=4,
        )
        
        # 功能菜单列表
        menu_list = ft.Column([
            ft.ListTile(
                leading=ft.Icon(item["icon"], color=item["color"]),
                title=ft.Text(item["title"]),
                trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                on_click=lambda e, t=item["title"]: self.on_menu_click(t),
            )
            for item in self.menu_items
        ], spacing=0)
        
        content = ft.Column([
            ft.Container(height=20),
            user_card,
            ft.Container(height=20),
            ft.Text("功能菜单", size=18, weight="bold", color=ft.Colors.GREY),
            ft.Divider(),
            menu_list,
        ], spacing=0)
        
        if self.responsive.is_desktop:
            content = self.get_container(content)
        
        return content
    
    def on_menu_click(self, title: str):
        """处理菜单点击事件
        
        Args:
            title: 菜单项标题
        """
        self.page.show_snack_bar(ft.SnackBar(ft.Text(f"点击了：{title}")))

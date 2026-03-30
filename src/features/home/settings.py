# src/features/home/settings.py - 设置页面
import flet as ft
from src.features.base_page import BasePage
from src.utils.responsive import ResponsiveConfig


class SettingsPage(BasePage):
    """设置页面"""
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        super().__init__(page, responsive)
    
    def build(self) -> ft.Control:
        """构建设置页面"""
        app_bar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back()),
            title=ft.Text("设置"),
            center_title=True,
        )
        
        settings_list = ft.Column([
            ft.Switch(label="深色模式", label_position=ft.LabelPosition.LEFT),
            ft.Switch(label="通知", label_position=ft.LabelPosition.LEFT),
            ft.Switch(label="自动更新", label_position=ft.LabelPosition.LEFT),
            ft.Divider(),
            ft.Text("关于", size=18, weight="bold"),
            ft.Text("版本：1.0.0"),
            ft.Text("作者：Your Name"),
        ], spacing=15)
        
        content = ft.Container(content=settings_list, padding=20)
        
        if self.responsive.is_desktop:
            content = self.get_container(content)
        
        return ft.Column([app_bar, content])

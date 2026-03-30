# src/features/home/counter.py - 计数器页面
import flet as ft
from src.features.base_page import BasePage
from src.utils.responsive import ResponsiveConfig


class CounterPage(BasePage):
    """计数器页面"""
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        super().__init__(page, responsive)
        self.txt_number = None
    
    def build(self) -> ft.Control:
        """构建计数器页面"""
        app_bar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back(),
            ),
            title=ft.Text("计数器"),
            center_title=True,
        )
        
        # 计数器显示
        self.txt_number = ft.Text(value="0", size=60, color=ft.Colors.BLUE, weight="bold")
        
        # 按钮行
        button_row = ft.Row([
            ft.FloatingActionButton(icon=ft.Icons.REMOVE, on_click=self.minus_click, bgcolor=ft.Colors.RED_200),
            self.txt_number,
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.plus_click, bgcolor=ft.Colors.GREEN_200),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=40)
        
        content = ft.Container(content=button_row, alignment=ft.Alignment.CENTER, padding=20)
        
        if self.responsive.is_desktop:
            content = self.get_container(content)
        
        return ft.Column([app_bar, content])
    
    def minus_click(self, e):
        """减少计数"""
        try:
            current_value = int(self.txt_number.value)
            self.txt_number.value = str(current_value - 1)
            self.txt_number.color = ft.Colors.RED if current_value - 1 < 0 else ft.Colors.BLUE
        except ValueError:
            self.txt_number.value = "0"
        self.page.update()
    
    def plus_click(self, e):
        """增加计数"""
        try:
            current_value = int(self.txt_number.value)
            self.txt_number.value = str(current_value + 1)
            self.txt_number.color = ft.Colors.BLUE
        except ValueError:
            self.txt_number.value = "0"
        self.page.update()

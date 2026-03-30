# src/features/home/converter.py - 单位转换页面
import flet as ft
from src.features.base_page import BasePage
from src.utils.responsive import ResponsiveConfig


class ConverterPage(BasePage):
    """单位转换页面"""
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        super().__init__(page, responsive)
        self.input_value = ft.TextField(label="输入值", width=200)
        self.result_text = ft.Text(value="结果：-", size=20, color=ft.Colors.BLUE)
    
    def build(self) -> ft.Control:
        """构建单位转换页面"""
        app_bar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back()),
            title=ft.Text("单位转换"),
            center_title=True,
        )
        
        # 转换控件
        converter_type = ft.Dropdown(
            label="转换类型",
            options=[
                ft.dropdown.Option("长度", "length"),
                ft.dropdown.Option("重量", "weight"),
                ft.dropdown.Option("温度", "temperature"),
            ],
            width=200,
            on_change=lambda e: self.page.update(),
        )
        
        from_unit = ft.Dropdown(
            label="从",
            options=[
                ft.dropdown.Option("米", "m"),
                ft.dropdown.Option("千米", "km"),
                ft.dropdown.Option("英尺", "ft"),
            ],
            width=200,
        )
        
        to_unit = ft.Dropdown(
            label="到",
            options=[
                ft.dropdown.Option("米", "m"),
                ft.dropdown.Option("千米", "km"),
                ft.dropdown.Option("英尺", "ft"),
            ],
            width=200,
        )
        
        convert_btn = ft.ElevatedButton(
            text="转换",
            on_click=self.convert,
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
        )
        
        content = ft.Container(
            content=ft.Column([
                converter_type,
                self.input_value,
                ft.Row([from_unit, to_unit], spacing=20),
                convert_btn,
                ft.Container(height=20),
                self.result_text,
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            alignment=ft.Alignment.CENTER,
        )
        
        if self.responsive.is_desktop:
            content = self.get_container(content)
        
        return ft.Column([app_bar, content])
    
    def convert(self, e):
        """执行单位转换"""
        try:
            value = float(self.input_value.value)
            # TODO: 实现实际的转换逻辑
            self.result_text.value = f"结果：{value * 1.0}"
        except ValueError:
            self.result_text.value = "请输入有效数字"
        self.page.update()

# src/features/home/calculator.py - 计算器页面
import flet as ft
from src.features.base_page import BasePage
from src.utils.responsive import ResponsiveConfig


class CalculatorPage(BasePage):
    """计算器页面"""
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        super().__init__(page, responsive)
        self.result = ft.Text(value="0", size=40, color=ft.Colors.BLUE, weight="bold")
        self.current_input = ""
        
        # 按钮布局配置
        self.buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]
        
        # 按钮颜色映射
        self.colors = {
            "C": ft.Colors.RED, "±": ft.Colors.GREY, "%": ft.Colors.GREY,
            "÷": ft.Colors.ORANGE, "×": ft.Colors.ORANGE, "-": ft.Colors.ORANGE,
            "+": ft.Colors.ORANGE, "=": ft.Colors.GREEN,
        }
    
    def build(self) -> ft.Control:
        """构建计算器页面"""
        app_bar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back(),
            ),
            title=ft.Text("计算器"),
            center_title=True,
        )
        
        # 创建按钮网格
        button_grid = ft.Column([
            ft.Row([self._create_button(text) for text in row], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
            for row in self.buttons
        ], spacing=10)
        
        content = ft.Container(
            content=ft.Column([
                self.result,
                ft.Container(height=20),
                button_grid,
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            alignment=ft.Alignment.CENTER,
        )
        
        if self.responsive.is_desktop:
            content = self.get_container(content)
        
        return ft.Column([app_bar, content])
    
    def _create_button(self, text: str) -> ft.ElevatedButton:
        """创建计算器按钮
        
        Args:
            text: 按钮文本
            
        Returns:
            ft.ElevatedButton: 按钮控件
        """
        bg_color = self.colors.get(text, ft.Colors.WHITE)
        text_color = ft.Colors.BLACK if text not in ["÷", "×", "-", "+", "="] else ft.Colors.WHITE
        
        return ft.ElevatedButton(
            text=text,
            bgcolor=bg_color,
            color=text_color,
            on_click=lambda e, t=text: self.on_button_click(t),
            width=60,
            height=60,
        )
    
    def on_button_click(self, text: str):
        """处理按钮点击事件
        
        Args:
            text: 按钮文本
        """
        try:
            if text == "C":
                self.current_input = ""
                self.result.value = "0"
            elif text == "=":
                expr = self.current_input.replace("×", "*").replace("÷", "/")
                result = eval(expr)
                self.result.value = str(result)
                self.current_input = str(result)
            elif text == "±":
                if self.current_input:
                    self.current_input = str(-float(self.current_input))
                    self.result.value = self.current_input
            elif text == "%":
                if self.current_input:
                    self.current_input = str(float(self.current_input) / 100)
                    self.result.value = self.current_input
            else:
                self.current_input += text
                self.result.value = self.current_input
        except Exception:
            self.result.value = "错误"
            self.current_input = ""
        
        self.page.update()

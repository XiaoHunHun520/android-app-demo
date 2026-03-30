# src/features/home/home.py - 首页（工具列表）
import flet as ft
from src.features.base_page import BasePage
from src.utils.responsive import ResponsiveConfig


class HomePage(BasePage):
    """首页 - 显示工具卡片列表"""
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        super().__init__(page, responsive)
        
        # 工具配置数据
        self.tools = [
            {"name": "计数器", "icon": ft.Icons.ADD_BOX, "route": "/counter", "color": ft.Colors.BLUE},
            {"name": "计算器", "icon": ft.Icons.CALCULATE, "route": "/calculator", "color": ft.Colors.GREEN},
            {"name": "单位转换", "icon": ft.Icons.SWAP_HORIZ, "route": "/converter", "color": ft.Colors.ORANGE},
            {"name": "设置", "icon": ft.Icons.SETTINGS, "route": "/settings", "color": ft.Colors.GREY},
        ]
    
    def build(self) -> ft.Control:
        """构建首页内容
        
        Returns:
            ft.Control: 首页主控件
        """
        # 创建响应式网格布局
        columns = self.responsive.get_grid_columns()
        tool_cards = ft.GridView(
            runs_count=columns,
            max_extent=300,
            spacing=15,
            run_spacing=15,
            expand=True,
            controls=[self._create_card(tool) for tool in self.tools],
        )
        
        return ft.Column([
            ft.AppBar(
                title=ft.Text("🧰 多功能工具箱"),
                center_title=True,
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.Container(
                content=tool_cards,
                padding=20,
                alignment=ft.Alignment.CENTER,
                expand=True,
            ),
        ])
    
    def _create_card(self, tool: dict) -> ft.Card:
        """创建工具卡片
        
        Args:
            tool: 工具配置字典
            
        Returns:
            ft.Card: 工具卡片控件
        """
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(tool["icon"], size=40, color=tool["color"]),
                    ft.Text(tool["name"], size=16, weight="bold"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                on_click=lambda e, r=tool["route"]: self.go_to(r),
            ),
            elevation=4,
        )
    
    def go_to(self, route: str):
        """页面跳转
        
        Args:
            route: 目标路由路径
        """
        if self.navigate:
            self.navigate(route)
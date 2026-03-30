# src/components/unified_nav.py - 统一导航组件
import flet as ft
from src.utils.responsive import ResponsiveConfig
from typing import Callable, Optional


class UnifiedNavigationBar:
    """统一导航栏 - 自动适配移动端/PC 端
    
    Attributes:
        page: Flet 页面对象
        responsive: 响应式配置对象
        on_nav_change: 导航切换回调函数
    """
    
    def __init__(
        self, 
        page: ft.Page, 
        responsive: ResponsiveConfig, 
        on_nav_change: Optional[Callable[[int], None]] = None
    ):
        self.page = page
        self.responsive = responsive
        self.on_nav_change = on_nav_change
        self.current_index = 0
        
        # 导航目标配置
        self.destinations = [
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                selected_icon=ft.Icons.HOME_FILLED,
                label="主页",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINE,
                selected_icon=ft.Icons.PERSON,
                label="我的",
            ),
        ]
        
        # 底部导航（移动端）
        self.bottom_nav = ft.NavigationBar(
            destinations=self.destinations,
            on_change=self._handle_nav_change,
            selected_index=0,
        )
        
        # 侧边导航（PC 端）
        self.sidebar_nav = ft.NavigationRail(
            destinations=self.destinations,
            on_change=self._handle_nav_change,
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
        )
    
    def _handle_nav_change(self, e):
        """处理导航切换"""
        self.current_index = e.control.selected_index
        if self.on_nav_change:
            self.on_nav_change(self.current_index)
    
    def set_index(self, index: int):
        """设置当前选中项
        
        Args:
            index: 导航项索引 (0=主页，1=我的)
        """
        self.current_index = index
        self.bottom_nav.selected_index = index
        self.sidebar_nav.selected_index = index

# src/features/base_page.py - 页面基类
import flet as ft
from src.utils.responsive import ResponsiveConfig
from typing import Callable, Optional


class BasePage:
    """页面基类 - 提供响应式支持
    
    所有页面应继承此基类以获得响应式布局能力
    
    Attributes:
        page: Flet 页面对象
        responsive: 响应式配置对象
        navigate: 页面导航回调函数
    """
    
    def __init__(self, page: ft.Page, responsive: ResponsiveConfig):
        self.page = page
        self.responsive = responsive
        self.navigate: Optional[Callable[[str], None]] = None
    
    def build(self) -> ft.Control:
        """构建页面内容
        
        Returns:
            ft.Control: 页面内容控件
            
        Raises:
            NotImplementedError: 子类必须实现此方法
        """
        raise NotImplementedError("子类必须实现 build() 方法")
    
    def go_back(self):
        """返回上一页"""
        if self.navigate:
            self.navigate("/")
    
    def get_container(self, content: ft.Control) -> ft.Container:
        """获取响应式容器
        
        Args:
            content: 要包裹的内容控件
            
        Returns:
            ft.Container: 响应式容器
        """
        return ft.Container(
            content=content,
            width=self.responsive.get_container_width(),
            padding=20 if self.responsive.is_mobile else 40,
            alignment=ft.Alignment.CENTER if self.responsive.is_desktop else None,
        )

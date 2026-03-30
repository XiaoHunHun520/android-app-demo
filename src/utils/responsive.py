# src/utils/responsive.py - 响应式配置管理
import flet as ft
from typing import Optional


class ResponsiveConfig:
    """响应式配置管理器
    
    根据窗口宽度自动判断设备类型（移动端/平板/PC 端）
    
    Attributes:
        page: Flet 页面对象
        is_mobile: 是否为移动设备
        is_tablet: 是否为平板设备
        is_desktop: 是否为桌面设备
    """
    
    # 断点定义（像素）
    MOBILE_BREAKPOINT = 600
    TABLET_BREAKPOINT = 900
    DESKTOP_BREAKPOINT = 1200
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.is_mobile = True
        self.is_tablet = False
        self.is_desktop = False
        self._update_device_type()
    
    def _update_device_type(self):
        """根据窗口宽度更新设备类型"""
        width = self.page.window.width
        self.is_mobile = width < self.MOBILE_BREAKPOINT
        self.is_tablet = self.MOBILE_BREAKPOINT <= width < self.DESKTOP_BREAKPOINT
        self.is_desktop = width >= self.DESKTOP_BREAKPOINT
    
    def get_nav_style(self) -> str:
        """获取导航样式
        
        Returns:
            "sidebar" (PC 端) 或 "bottom" (移动端/平板)
        """
        if self.is_desktop:
            return "sidebar"
        return "bottom"
    
    def get_grid_columns(self) -> int:
        """获取网格布局列数
        
        Returns:
            列数：PC 端=3，平板=2，移动端=1
        """
        if self.is_desktop:
            return 3
        elif self.is_tablet:
            return 2
        return 1
    
    def get_container_width(self) -> Optional[int]:
        """获取容器最大宽度
        
        Returns:
            PC 端返回 1200px，移动端/平板返回 None（全屏）
        """
        if self.is_desktop:
            return 1200
        return None

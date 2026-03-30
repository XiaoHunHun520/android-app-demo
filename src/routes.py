# routes.py - 响应式路由管理
import flet as ft
from src.features.home import HomePage, CounterPage, CalculatorPage, ConverterPage, SettingsPage
from src.features.mine import MinePage
from src.components.unified_nav import UnifiedNavigationBar
from src.utils.responsive import ResponsiveConfig


class Router:
    """路由管理器 - 支持移动端/PC 端响应式布局"""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.unified_nav = None
        self.current_tab = 0
        self.nav_history = []
        
        # 响应式配置
        self.responsive = ResponsiveConfig(page)
        
        # 监听窗口大小变化
        self.page.on_resize = self._handle_resize
        
        # 主页工具页面映射
        self.tool_pages = {
            "/": HomePage(self.page, self.responsive),
            "/counter": CounterPage(self.page, self.responsive),
            "/calculator": CalculatorPage(self.page, self.responsive),
            "/converter": ConverterPage(self.page, self.responsive),
            "/settings": SettingsPage(self.page, self.responsive),
        }
        
        # 底部标签页
        self.tabs = {
            0: self.tool_pages["/"],
            1: MinePage(self.page, self.responsive),
        }
    
    def _handle_resize(self, e):
        """窗口大小变化处理"""
        self.responsive._update_device_type()
        self._refresh_page()
    
    def _refresh_page(self):
        """刷新页面布局"""
        current_route = self.nav_history[-1] if self.nav_history else "/"
        self.navigate(current_route, refresh=True)
    
    def _update_navigation(self):
        """更新导航样式"""
        if self.responsive.is_desktop:
            self.page.navigation_bar = None
        else:
            self.page.navigation_bar = self.unified_nav.bottom_nav
    
    def setup_routes(self):
        """初始化路由和导航"""
        # 注入 navigate 方法到所有页面
        for route, page_obj in self.tool_pages.items():
            page_obj.navigate = self.navigate
        
        # 创建统一导航栏
        self.unified_nav = UnifiedNavigationBar(
            self.page,
            self.responsive,
            on_nav_change=self.on_bottom_nav_change
        )
        
        self._update_navigation()
        self.navigate("/")
    
    def on_bottom_nav_change(self, index: int):
        """底部导航切换处理"""
        self.current_tab = index
        if index == 0:
            self.navigate("/")
        elif index == 1:
            self.show_mine_page()
    
    def show_mine_page(self):
        """显示我的页面"""
        self.page.clean()
        content = self.tabs[1].build()
        
        if self.responsive.is_desktop:
            # PC 端：侧边导航 + 内容
            self.page.add(
                ft.Row(
                    [
                        self.unified_nav.sidebar_nav,
                        ft.VerticalDivider(width=1),
                        ft.Container(content=content, expand=True, padding=20),
                    ],
                    spacing=0,
                    expand=True,
                )
            )
        else:
            # 移动端：AppBar + 内容
            self.page.add(
                ft.AppBar(
                    title=ft.Text("我的"),
                    center_title=True,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                ),
                content,
            )
        self.page.update()
    
    def navigate(self, route: str, refresh=False):
        """导航到指定页面"""
        if not refresh:
            self.nav_history.append(route)
        
        if route in self.tool_pages:
            self.page.clean()
            content = self.tool_pages[route].build()
            
            if self.responsive.is_desktop:
                # PC 端：侧边导航 + 内容
                self.page.add(
                    ft.Row(
                        [
                            self.unified_nav.sidebar_nav,
                            ft.VerticalDivider(width=1),
                            ft.Container(content=content, expand=True, padding=20),
                        ],
                        spacing=0,
                        expand=True,
                    )
                )
            else:
                # 移动端：直接添加内容
                self.page.add(content)
            
            self._update_navigation()
            self.page.update()
    
    def go_back(self):
        """返回上一页"""
        if len(self.nav_history) > 1:
            self.nav_history.pop()
            prev_route = self.nav_history[-1]
            self.navigate(prev_route)

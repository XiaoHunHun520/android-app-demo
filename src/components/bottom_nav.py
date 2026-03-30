import flet as ft

class BottomNavigationBar:
    def __init__(self, page: ft.Page, on_nav_change=None):
        self.page = page
        self.on_nav_change = on_nav_change
        self.current_index = 0
        
        self.nav_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME,
                    selected_icon=ft.Icons.HOME_FILLED,
                    label="主页",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PERSON_OUTLINE,       # 修改为空心图标
                    selected_icon=ft.Icons.PERSON,      # 修改为实心图标，移除 _FILLED 后缀
                    label="我的",
                ),
            ],
            on_change=self.handle_nav_change,
            selected_index=0,
        )
    
    def handle_nav_change(self, e):
        """处理导航切换"""
        self.current_index = e.control.selected_index
        if self.on_nav_change:
            self.on_nav_change(self.current_index)
    
    def get_bar(self):
        return self.nav_bar
    
    def set_index(self, index: int):
        """设置当前选中项"""
        self.nav_bar.selected_index = index
        self.current_index = index
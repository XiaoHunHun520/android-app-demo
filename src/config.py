import flet as ft

# 应用配置
APP_CONFIG = {
    "name": "多功能工具箱",
    "version": "1.0.0",
    "author": "Your Name",
}

# 主题配置
THEME_CONFIG = {
    "primary_color": ft.Colors.BLUE,
    "theme_mode": ft.ThemeMode.LIGHT,
    "app_bar_color": ft.Colors.BLUE,
    "app_bar_text_color": ft.Colors.WHITE,
}

# 工具列表配置
TOOLS_CONFIG = [
    {
        "id": "counter",
        "name": "计数器",
        "icon": ft.Icons.COUNTERTOP,
        "route": "/counter",
        "description": "简单的数字计数器",
    },
    {
        "id": "calculator",
        "name": "计算器",
        "icon": ft.Icons.CALCULATE,
        "route": "/calculator",
        "description": "基础计算器",
    },
    {
        "id": "converter",
        "name": "单位转换",
        "icon": ft.Icons.SWAP_HORIZ,
        "route": "/converter",
        "description": "单位转换工具",
    },
    {
        "id": "settings",
        "name": "设置",
        "icon": ft.Icons.SETTINGS,
        "route": "/settings",
        "description": "应用设置",
    },
]

ROUTES_CONFIG = {
    "HOME": "/",
    "COUNTER": "/counter",
    "CALCULATOR": "/calculator",
    "CONVERTER": "/converter",
    "SETTINGS": "/settings",
    "MINE": "/mine",
}
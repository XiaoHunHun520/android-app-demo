import flet as ft

def main(page: ft.Page):
    # 1. 配置页面属性
    page.title = "Flet 现代 App 示例"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT # 或 DARK
    
    # 2. 定义界面元素 (控件)
    txt_number = ft.Text(value="0", size=60, color=ft.colors.BLUE, weight="bold")
    
    # 定义点击事件逻辑
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        # 如果小于0，字体变红，使用 Flutter 原生状态管理
        if int(txt_number.value) < 0:
            txt_number.color = ft.colors.RED
        page.update() # 关键：更新页面

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        if int(txt_number.value) >= 0:
            txt_number.color = ft.colors.BLUE
        page.update()

    # 3. 将控件添加到页面布局中
    # 使用 Row 行布局放置按钮和数字
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Python 安卓开发"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    
    page.add(
        app_bar,
        ft.Row(
            [
                # 悬浮按钮 (Flutter 原生手感)
                ft.FloatingActionButton(icon=ft.icons.REMOVE, on_click=minus_click, bgcolor=ft.colors.RED_200),
                txt_number,
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=40
        ),
        ft.Container(height=20),
        ft.Text("这是一个由 Python 和 Flet 驱动的原生 UI App", color=ft.colors.GREY_700)
    )

# 4. 启动 App (本地测试用)
if __name__ == "__main__":
    # 使用 flet.app 命令在本地窗口中预览
    ft.app(target=main)
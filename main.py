import flet as ft

def main(page: ft.Page):
    # 1. 配置页面属性
    page.title = "Flet 现代 App 示例"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # 2. 定义界面元素 (控件)
    txt_number = ft.Text(value="0", size=60, color=ft.colors.BLUE, weight="bold")
    
    # 定义点击事件逻辑
    def minus_click(e):
        try:
            current_value = int(txt_number.value)
            txt_number.value = str(current_value - 1)
            if current_value - 1 < 0:
                txt_number.color = ft.colors.RED
            else:
                txt_number.color = ft.colors.BLUE
            page.update()
        except ValueError:
            txt_number.value = "0"
            txt_number.color = ft.colors.BLUE
            page.update()

    def plus_click(e):
        try:
            current_value = int(txt_number.value)
            txt_number.value = str(current_value + 1)
            if current_value + 1 >= 0:
                txt_number.color = ft.colors.BLUE
            page.update()
        except ValueError:
            txt_number.value = "0"
            txt_number.color = ft.colors.BLUE
            page.update()

    # 3. 将控件添加到页面布局中
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Python 安卓开发"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    
    # 使用 Column 确保内容正确显示
    page.add(
        app_bar,
        ft.Column(
            [
                ft.Row(
                    [
                        ft.FloatingActionButton(
                            icon=ft.icons.REMOVE, 
                            on_click=minus_click, 
                            bgcolor=ft.colors.RED_200
                        ),
                        txt_number,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, 
                            on_click=plus_click,
                            bgcolor=ft.colors.GREEN_200
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40
                ),
                ft.Container(height=20),
                ft.Text(
                    "这是一个由 Python 和 Flet 驱动的原生 UI App", 
                    color=ft.colors.GREY_700,
                    text_align=ft.TextAlign.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

# 4. 启动 App（兼容多平台）
if __name__ == "__main__":
    # view 参数确保移动端正常渲染
    ft.app(target=main, view=ft.FLET_APP)
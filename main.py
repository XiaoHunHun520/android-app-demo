import flet as ft

def main(page: ft.Page):
    # 1. 配置页面属性
    page.title = "Flet 现代 App 示例"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # 2. 定义界面元素 (控件)
    txt_number = ft.Text(value="0", size=60, color=ft.Colors.BLUE, weight="bold")
    
    # 定义点击事件逻辑
    def minus_click(e):
        try:
            current_value = int(txt_number.value)
            txt_number.value = str(current_value - 1)
            if current_value - 1 < 0:
                txt_number.color = ft.Colors.RED
            else:
                txt_number.color = ft.Colors.BLUE
            page.update()
        except ValueError:
            txt_number.value = "0"
            txt_number.color = ft.Colors.BLUE
            page.update()

    def plus_click(e):
        try:
            current_value = int(txt_number.value)
            txt_number.value = str(current_value + 1)
            if current_value + 1 >= 0:
                txt_number.color = ft.Colors.BLUE
            page.update()
        except ValueError:
            txt_number.value = "0"
            txt_number.color = ft.Colors.BLUE
            page.update()

    # 3. 将控件添加到页面布局中
    # 修复：替换不存在的颜色常量
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.Icons.COLOR_LENS),
        leading_width=40,
        title=ft.Text("Python 安卓开发"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE,  # 替换 SURFACE_VARIANT → SURFACE
    )
    
    # 使用 Column 确保内容正确显示
    page.add(
        app_bar,
        ft.Column(
            [
                ft.Row(
                    [
                        ft.FloatingActionButton(
                            icon=ft.Icons.REMOVE, 
                            on_click=minus_click, 
                            bgcolor=ft.Colors.RED_200
                        ),
                        txt_number,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD, 
                            on_click=plus_click,
                            bgcolor=ft.Colors.GREEN_200
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40
                ),
                ft.Container(height=20),
                ft.Text(
                    "这是一个由 Python 和 Flet 驱动的原生 UI App", 
                    color=ft.Colors.GREY,  # 替换 GREY_700 → GREY
                    text_align=ft.TextAlign.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

# 4. 启动 App（使用新 API 消除警告）
if __name__ == "__main__":
    ft.run(main)  # 替换 ft.app(main) → ft.run(main)
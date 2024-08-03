import flet as ft


def main(page: ft.Page):
    page.title = "Photos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    layout = ft.Row(spacing=2, wrap=True)
    for i in range(50):
        layout.controls.append(
            ft.Image(
                src=f"https://picsum.photos/350/350?{i}",
                border_radius=ft.border_radius.all(10)
            ),
        )
    page.add(layout)

ft.app(main)

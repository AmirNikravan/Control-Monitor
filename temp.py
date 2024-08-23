import flet as ft

def main(page: ft.Page):
    page.title = "Beautiful Calculator"
    page.window.width = 300
    page.window.height = 400
    page.padding = 10
    page.spacing = 10
    
    def update_display(e):
        current = display.value
        if current == "0" or clear_on_next_input:
            current = ""
        display.value = current + e.control.data
        display.update()

    def calculate(e):
        try:
            display.value = str(eval(display.value))
            display.update()
        except:
            display.value = "Error"
            display.update()
    
    def clear_display(e):
        display.value = "0"
        display.update()

    def handle_clear_next_input(e):
        nonlocal clear_on_next_input
        clear_on_next_input = True

    clear_on_next_input = False

    display = ft.TextField(
        value="0", 
        text_align=ft.TextAlign.RIGHT, 
        width=290, 
        height=60, 
        read_only=True, 
        border_radius=10, 
        bgcolor=ft.colors.WHITE,
        style=ft.TextStyle(size=24)
    )
    
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"]
    ]
    
    page.add(display)

    for row in buttons:
        button_row = []
        for label in row:
            if label == "=":
                btn = ft.Button(text=label, data=label, on_click=calculate, bgcolor=ft.colors.GREEN, border_radius=5, width=60, height=60)
            else:
                btn = ft.Button(text=label, data=label, on_click=update_display, border_radius=5, width=60, height=60)
            button_row.append(btn)
        page.add(ft.Row(controls=button_row, spacing=10, alignment=ft.MainAxisAlignment.CENTER))

    clear_button = ft.Button(text="C", on_click=clear_display, bgcolor=ft.colors.RED, border_radius=5, width=60, height=60)
    page.add(ft.Row(controls=[clear_button], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)

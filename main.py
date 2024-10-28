import flet as ft
import controls


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        global search_bar, dd, data_table, data
        selected_files.value = e.files[0].name if e.files else 'Cancelled!'
        selected_files.update()
        data = controls.read_table(e.files[0].path)
        dd = ft.Dropdown(
            width=100,
            options=[
                ft.dropdown.Option(column_name) for column_name in data.columns
            ],
            value=data.columns[0],
        )
        search_bar = ft.TextField(label="Search", on_change=handle_search, width=650)
        data_table = controls.update_table(data)
        page.add(
            ft.Row(
                [
                    dd,
                    search_bar,
                    # ft.ElevatedButton("Search", on_click=handle_search)
                ]
            ),
            data_table
        )
        page.update()

    def handle_search(e):
        if search_bar.value:
            data_table = controls.filter_table(data, dd.value, search_bar.value)
            page.controls.pop()
            page.add(data_table)
            page.update()
        else:
            data_table = controls.update_table(data)
            page.controls.pop()
            page.add(data_table)
            page.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.title = 'Searching'
    page.overlay.append(pick_files_dialog)
    page.scroll = True
    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick file",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )


ft.app(target=main, assets_dir='assets')

import flet as ft

def main(page: ft.Page):

    class Task(ft.UserControl):
        def __init__(self, input_text, delete_task):
            super().__init__()
            self.input = input_text
            self.delete_task = delete_task
        def build(self):
            self.task_checkbox = ft.Checkbox(label = self.input, expand=True)
            self.edit_text_field = ft.TextField(value=self.input, expand=True)

            self.task_view = ft.Row(
                visible = True,
                controls = [
                    self.task_checkbox,
                    ft.IconButton(icon=ft.icons.CREATE_OUTLINED, on_click= self.edit),
                    ft.IconButton(icon=ft.icons.DELETE_OUTLINED, on_click= self.delete),
                ]
            )

            self.edit_task_view = ft.Row(
                visible = False,
                controls = [
                    self.edit_text_field,
                    ft.IconButton(icon=ft.icons.CHECK, on_click= self.save)
                ]
            )
            return ft.Column(
                controls = [
                    self.task_view,self.edit_task_view
                ]
            )

        def edit(self, e):
            self.task_view.visible = False
            self.edit_task_view.visible = True
            self.update()

        def delete(self, task):
            self.delete_task(task)

        def save(self, e):
            self.task_checkbox.label = self.edit_text_field.value
            self.task_view.visible = True
            self.edit_task_view.visible = False
            self.update()


    class Todo(ft.UserControl):
        def build(self):
            self.input = ft.TextField(hint_text='What should be done?', expand = True)
            self.tasks = ft.Column()
            view = ft.Column(
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ft.Text(value='ToDo', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.Row(
                        controls = [
                            self.input,
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_button_clicked)
                        ]
                    ),
                    self.tasks
                ]
            )
            return view

        def add_button_clicked(self, e):
            task = Task(self.input.value, self.delete_task)
            self.tasks.controls.append(task)
            self.input.value = ''
            self.update()

        def delete_task(self, task):
            self.tasks.controls.remove(task)
            self.update()

    page.window_height = 600
    page.window_width = 600
    page.title = "Flet App"

    todo = Todo()
    page.add(todo)

    page.update()

ft.app(target=main)

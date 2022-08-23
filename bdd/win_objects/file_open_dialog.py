from pywinauto import Application


class FileDialogObject:

    def __init__(self, root_application_title):
        self._root_application_title = root_application_title
        self._handler = root_application_title
        self._root_window = self.set_root_window()

    def set_root_window(self):
        app = Application(backend='uia')
        app.connect(handle=self._handler)
        return app.top_window()

    def set_file_name(self, file_name):
        file_open_dialog = self._root_window.child_window(control_type="Window")
        file_name_edit = file_open_dialog.child_window(title="File name:", control_type="Edit")
        file_name_edit.set_text(file_name)

    def click_open_button(self):
        file_open_dialog = self._root_window.child_window(control_type="Window")
        open_button = file_open_dialog.child_window(title="Open", auto_id="1", control_type="Button")
        open_button.click()

    def click_cancel_button(self):
        file_open_dialog = self._root_window.child_window(control_type="Window")
        cancel_button = file_open_dialog.child_window(title="Cancel", auto_id="2", control_type="Button")
        cancel_button.click()

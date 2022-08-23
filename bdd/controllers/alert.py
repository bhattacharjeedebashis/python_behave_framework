from bdd.controllers.base_controller import BaseController


class Alert(BaseController):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def accept_alert_if_present(self):
        if self.is_alert_displayed():
            alert = self._driver.switch_to_alert()
            alert.accept()

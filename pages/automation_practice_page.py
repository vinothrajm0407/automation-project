from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class AutomationPracticePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    RADIO1 = (By.XPATH, "//input[@value='radio1']")
    NAME_BOX = (By.ID, "autocomplete")
    DROPDOWN = (By.ID, "dropdown-class-example")
    CHECKBOX1 = (By.XPATH, "//input[@value='option1']")
    OPEN_WINDOW = (By.ID, "openwindow")
    OPEN_TAB = (By.ID, "opentab")
    NAME_ALERT = (By.ID, "name")
    ALERT_BTN = (By.ID, "alertbtn")
    HOVER_BTN = (By.ID, "mousehover")
    TOP_LINK = (By.LINK_TEXT, "Top")

    # Actions
    def select_radio1(self):
        self.driver.find_element(*self.RADIO1).click()

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_BOX).send_keys(name)

    def select_dropdown_option(self, text):
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        dropdown.select_by_visible_text(text)

    def click_checkbox(self):
        self.driver.find_element(*self.CHECKBOX1).click()

    def open_new_window(self):
        self.driver.find_element(*self.OPEN_WINDOW).click()

    def open_new_tab(self):
        self.driver.find_element(*self.OPEN_TAB).click()

    # def trigger_alert(self, text):
    #     self.driver.find_element(*self.NAME_ALERT).send_keys(text)
    #     self.driver.find_element(*self.ALERT_BTN).click()

    def trigger_alert(self, name):
        self.driver.find_element(By.ID, "name").clear()
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "alertbtn").click()

    def hover_and_click_top(self):
        actions = ActionChains(self.driver)
        hover = self.driver.find_element(*self.HOVER_BTN)
        actions.move_to_element(hover).perform()
        self.driver.find_element(*self.TOP_LINK).click()

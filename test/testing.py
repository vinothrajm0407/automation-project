from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_radio_button(driver):
    radio = driver.find_element(By.XPATH, "//input[@value='radio1']")
    radio.click()
    assert radio.is_selected()


def test_send_keys(driver):
    name_box = driver.find_element(By.ID, "autocomplete")
    name_box.send_keys("Vinoth")
    assert name_box.get_attribute("value") == "Vinoth"


def test_dropdown(driver):
    dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
    dropdown.select_by_visible_text("Option2")
    assert dropdown.first_selected_option.text == "Option2"


def test_checkbox(driver):
    checkbox = driver.find_element(By.XPATH, "//input[@value='option1']")
    checkbox.click()
    assert checkbox.is_selected()


def test_switch_window(driver):
    parent = driver.current_window_handle
    driver.find_element(By.ID, "openwindow").click()

    for window in driver.window_handles:
        if window != parent:
            driver.switch_to.window(window)
            break

    assert "Rahul Shetty" in driver.title


def test_switch_tab(driver):
    parent = driver.current_window_handle
    driver.find_element(By.ID, "opentab").click()

    for tab in driver.window_handles:
        if tab != parent:
            driver.switch_to.window(tab)
            break

    assert "Rahul Shetty" in driver.title


def test_alert(driver):
    driver.find_element(By.ID, "name").send_keys("python")
    driver.find_element(By.ID, "alertbtn").click()

    alert = driver.switch_to.alert
    assert "python" in alert.text
    alert.dismiss()


def test_mouse_hover(driver):
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    hover = wait.until(EC.element_to_be_clickable((By.ID, "mousehover")))
    actions.move_to_element(hover).perform()

    top = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Top")))
    top.click()

    assert driver.current_url.endswith("#top")

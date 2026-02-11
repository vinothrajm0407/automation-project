import pytest
from pages.automation_practice_page import AutomationPracticePage

@pytest.mark.flaky(reruns=2)
def test_radio_button(driver):
    page = AutomationPracticePage(driver)
    page.select_radio1()
    assert driver.find_element(*page.RADIO1).is_selected()
@pytest.mark.flaky(reruns=2)
@pytest.mark.smoke
@pytest.mark.regression
def test_send_keys(driver):
    page = AutomationPracticePage(driver)
    page.enter_name("Vinoth")
    assert driver.find_element(*page.NAME_BOX).get_attribute("value") == "Vinoth"

@pytest.mark.smoke
@pytest.mark.regression
def test_dropdown(driver):
    page = AutomationPracticePage(driver)
    page.select_dropdown_option("Option2")
    selected = driver.find_element(*page.DROPDOWN)
    assert selected is not None

@pytest.mark.regression
def test_checkbox(driver):
    page = AutomationPracticePage(driver)
    page.click_checkbox()
    assert driver.find_element(*page.CHECKBOX1).is_selected()

@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.parametrize("name", ["python", "java","js"])  #@pytest.mark.parametrize("name", ["python", "java", "js"])
def test_alert(driver, name):
    page = AutomationPracticePage(driver)
    page.trigger_alert(name)
    alert = driver.switch_to.alert
    assert name in alert.text
    alert.accept()

@pytest.mark.regression
def test_hover(driver):
    page = AutomationPracticePage(driver)
    page.hover_and_click_top()
    assert driver.current_url.endswith("#top")

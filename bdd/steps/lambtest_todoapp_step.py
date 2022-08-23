import time

from behave import given, when, then

from bdd.verify import Verify as verify
from bdd.page_objects.lambtest_todoapp import ToDoAppPage


@given('I go to 4davanceboy to add item')
def initialize(context):
    context.helperfunc.open('https://lambdatest.github.io/sample-todo-app/')
    context.helperfunc.maximize()


@then('I Click on first checkbox and second checkbox')
def click_on_checkboxes(context):
    web_page = ToDoAppPage(context.helperfunc.get_driver())
    web_page.select_checkbox_one()
    web_page.select_checkbox_two()
    verify.log_message(context, "Test Message")


@when(u'I enter item "{item}" to add')
def enter_item_name(context, item):
    web_page = ToDoAppPage(context.helperfunc.get_driver())
    web_page.enter_item_name(item)
    verify.capture_screenshot(context, 'enter')


@when('I click add button')
def click_on_add_button(context):
    web_page = ToDoAppPage(context.helperfunc.get_driver())
    web_page.click_add_btn()


@then('I should verify the added item')
def see_login_message(context):
    web_page = ToDoAppPage(context.helperfunc.get_driver())
    added_item = web_page.get_result()
    time.sleep(2)
    verify.contains(context, "Yey, Let's add it to list", added_item, "'Yey, Let's add it to list' not added to list")

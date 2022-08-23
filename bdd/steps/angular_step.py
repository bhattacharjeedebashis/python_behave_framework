from behave import given, when, then

from bdd.page_objects.angular_web_page import AngularWebPage


@given(u'the user is on "{url}"')
def step_impl(context, url):
    context.helperfunc.open(url)
    context.helperfunc.maximize()


@when(u'user enters "{operand_value}" as "{operand_type}" operand')
def step_impl(context, operand_value, operand_type):
    web_page = AngularWebPage(context.helperfunc.get_driver())
    if operand_type.lower() == 'first':
        web_page.set_first_operand(operand_value)
    else:
        web_page.set_second_operand(operand_value)


@when(u'user selects "{operator}" as operator')
def step_impl(context, operator):
    web_page = AngularWebPage(context.helperfunc.get_driver())
    web_page.select_operator(operator)


@when(u'user clicks on go button')
def step_impl(context):
    web_page = AngularWebPage(context.helperfunc.get_driver())
    web_page.submit_operation()


@then(u'correct expression and result should be displayed')
def step_impl(context):
    web_page = AngularWebPage(context.helperfunc.get_driver())
    actual_result = web_page.get_result_value()
    expected_result = eval(web_page.get_result_expression())
    assert int(expected_result) == int(actual_result), f"Result doesn't match; expected {expected_result}"


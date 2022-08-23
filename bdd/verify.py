class Verify(object):

    @staticmethod
    def true(context, condition, message_on_fail):
        try:
            assert condition, message_on_fail
        except AssertionError as err:
            context.helperfunc.capture_screenshot(context, 'Screen grab')
            assert False, message_on_fail

    @staticmethod
    def false(context, condition, message_on_fail):
        try:
            assert not condition, message_on_fail
        except AssertionError as err:
            context.helperfunc.capture_screenshot(context, 'Screen grab')
            assert False, message_on_fail

    @staticmethod
    def contains(context, expected, actual, message_on_fail):
        try:
            assert expected in actual, message_on_fail
        except AssertionError as err:
            context.helperfunc.capture_screenshot(context, 'Screen grab')
            assert False, message_on_fail

    @staticmethod
    def equals(context, expected, actual, message_on_fail):
        try:
            assert expected == actual, message_on_fail
        except AssertionError as err:
            context.helperfunc.capture_screenshot(context, 'Screen grab')
            assert False, message_on_fail

    @staticmethod
    def capture_screenshot(context, name):
        context.helperfunc.capture_screenshot(context, name)

    @staticmethod
    def log_message(context, message):
        context.embed(mime_type="text/plain", data=message, caption="PrintData")

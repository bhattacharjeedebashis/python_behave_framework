import glob
import os
from configparser import ConfigParser
from pathlib import Path

from helper.helper_web import get_browser


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
    screenshot_path = Path(os.path.join(os.path.join(os.getcwd(), 'reports'), 'screenshots'))
    if not screenshot_path.exists():
        os.mkdir(screenshot_path)
    for json_report in glob.iglob(os.path.join(os.path.join(os.getcwd(), 'reports'), '*.json')):
        os.remove(json_report)
    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func

    def embed_data(mime_type, data, caption):
        # If data is empty we want to finish html tag with at least one character
        non_empty_data = " " if not data else data
        for formatter in context._runner.formatters:
            formatter.embedding(mime_type=mime_type, data=non_empty_data, caption=caption)
            return

    context.embed = embed_data


def after_all(context):
    context.helperfunc.close()


# def after_scenario(context, scenario):
#     image_location = "/tmp/screenshot.png"
#     data_base64 = base64.b64encode(open(image_location, "rb").read())
#     data = data_base64.decode("utf-8").replace("\n", "")
#     context.embed(mime_type="image/png", data=data, caption="Screenshot")


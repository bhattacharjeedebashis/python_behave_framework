import argparse
import subprocess

if __name__ == '__main__':
    parameters = argparse.ArgumentParser()
    parameters.add_argument('--testdir', required=False, help="File path")
    parameters.add_argument('--tags', required=False, help="File path")
    arguments = parameters.parse_args()
    testdir = arguments.testdir
    tags = arguments.tags
    command = f'behave --no-capture {testdir} '
    if tags:
        command = command + f'--tags {tags} '
    command = command + f'-f html -o reports/behave-report.html ' \
                        f'--junit --junit-directory reports ' \
                        f'-f allure_behave.formatter:AllureFormatter -o reports ' \
                        f'-D behave.formatter.html.report_name="My Report Name"'
    s = subprocess.run(command, shell=True, check=True)

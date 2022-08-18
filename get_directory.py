import configparser
import os


class DirectoryPath:
    cwd = os.path.dirname(__file__)

    def get_driver_path(self):
        download_path = os.path.join(self.cwd, 'Driver/chromedriver')
        return download_path

    def get_config_ini(self):
        config = configparser.RawConfigParser()
        config.read(os.path.join(self.cwd,"Configurations/config.ini"))

    def get_functional_report(self):
        func_report = os.path.join(self.cwd, 'Reports/Functional_Reports/Functional_Result.html')
        return func_report

    def get_regression_report(self):
        regression_report = os.path.join(self.cwd, 'Reports/Regression_Reports/Regression_Result.html')
        return regression_report

    def get_smoke_report(self):
        smoke_report = os.path.join(self.cwd, 'Reports/Smoke_Reports/Smoke_Result.html')
        return smoke_report

    def get_download_dir(self):
        download_path = os.path.join(self.cwd, 'Downloads')
        return download_path

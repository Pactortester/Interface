import TestCase.test_weather
from Config.HTMLTestReportCN import HTMLTestRunner
import getcwd
import os
import Common.my_email

import unittest
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase.test_weather.weather('test_weather'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path,'report\\接口自动化测试报告.html')
    fp = open(file_path,'wb')
    runner = HTMLTestRunner(
        stream = fp,
        title = '接口自动化测试报告',
        description = '报告中描述部分',
        tester = '测试者'
    )
    runner.run(suite)
    fp.close()
    Common.my_email.mail()
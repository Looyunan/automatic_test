import time
import unittest

from datetime import datetime

import requests

from business.api_method import ApiMethod
from common.general_assert import GeneralAssert
from common.yamlRead import YamlRead
from common.logs import class_case_decoration, info
from business.BusinessRe import BusinessRe
from data.data import Url


@class_case_decoration
class RemindInput(unittest.TestCase):
    apiConfig = YamlRead().api_config()['remind']
    envConfig = YamlRead().env_config()
    user_id1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    url = host + apiConfig['path']
    ga = GeneralAssert()
    api = ApiMethod()
    ba = BusinessRe()

    def setUp(self):
        """前置数据清理"""
        # 删除所有便签
        ApiMethod.delete_notes(userid=self.user_id1, sid=self.sid1)
        # 删除所有分组
        ApiMethod.delete_groups(userid=self.user_id1, sid=self.sid1)

    def testCase01_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime缺失"""
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {

            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase02_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindEndTime缺失"""
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase03_Remind_input(self):
        """查看日历便签接口，input必填项校验：startIndex缺失"""
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase04_Remind_input(self):
        """查看日历便签接口，input必填项校验：rows缺失"""
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase05_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为“” """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": "",
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase06_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindEndTime值为”“ """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": "",
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase07_Remind_input(self):
        """查看日历便签接口，input必填项校验：startIndex值为”“ """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": "",
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase08_Remind_input(self):
        """查看日历便签接口，input必填项校验：rows值为”“ """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": ""}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase09_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为None """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": None,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase010_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindEndTime值为None """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": None,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase11_Remind_input(self):
        """查看日历便签接口，input必填项校验：startIndex值为None """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": None,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase12_Remind_input(self):
        """查看日历便签接口，input必填项校验：rows值为None """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": None}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase13_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为字符型数字 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": str(start_timestamp),
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase14_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为1.5 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": 1.5,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase15_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为0 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": 0,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase16_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为-1 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": -1,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase17_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindEndTime值为字符型数字 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": str(end_timestamp),
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase18_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindEndTime值为1.5 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": 1.5,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg":"remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase19_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为0 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": 0,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase20_Remind_input(self):
        """查看日历便签接口，input必填项校验：remindStartTime值为-1 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": -1,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase21_Remind_input(self):
        """查看日历便签接口，input必填项校验：startIndex值为字符型数字 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": str(0),
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase22_Remind_input(self):
        """查看日历便签接口，input必填项校验：startIndex值为1.5 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 1.5,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg":"remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase23_Remind_input(self):
        """查看日历便签接口，input必填项校验：startIndex值为-1 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": -1,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase24_Remind_input(self):
        """查看日历便签接口，input必填项校验：rows值为字符型数字 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": str(50)}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase25_Remind_input(self):
        """查看日历便签接口，input必填项校验：rows值为1.5 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 1.5}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg":"remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase26_Remind_input(self):
        """查看日历便签接口，input必填项校验：rows值为-1 """
        info("新建日历便签A")
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": -1}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "errorCode": -7, "errorMsg": "remindTime Requested!"
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

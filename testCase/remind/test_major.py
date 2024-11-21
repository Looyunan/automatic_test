
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
class RemindMajor(unittest.TestCase):
    apiConfig = YamlRead().api_config()['remind']
    envConfig = YamlRead().env_config()
    user_id1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    url = host + apiConfig['path']
    ga = GeneralAssert()
    ba = BusinessRe()
    api = ApiMethod()

    def setUp(self):
        """前置数据清理"""
        # 删除所有便签
        ApiMethod.delete_notes(userid=self.user_id1, sid=self.sid1)
        # 删除所有分组
        ApiMethod.delete_groups(userid=self.user_id1, sid=self.sid1)

    def testCase01_Remind_major(self):
        """查询日历便签接口，主流程：新建一条日历便签A，查询到A的数据"""
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
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
                "responseTime": int,
                "webNotes": [
                    {
                        "noteId": note_id,
                        "createTime": int,
                        "star": 0,
                        "remindTime": remind_time,
                        "remindType": 1,
                        "infoVersion": 1,
                        "infoUpdateTime": int,
                        "groupId": None,
                        "title": "test",
                        "summary": "test",
                        "thumbnail": None,
                        "contentVersion": 1,
                        "contentUpdateTime": int
                    }
                ]
            }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase02_Remind_major(self):
        """查询日历便签接口，主流程：没有数据时直接查询，返回空列表"""
        info("查询便签A")
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "responseTime": int,
            "webNotes": []
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)


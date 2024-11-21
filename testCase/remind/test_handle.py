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
class RemindHandle(unittest.TestCase):
    apiConfig = YamlRead().api_config()['remind']
    envConfig = YamlRead().env_config()
    user_id1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    user_id2 = envConfig['userid2']
    sid2 = envConfig['sid2']
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

    def testCase01_Remind_handle(self):
        """查询日历便签接口，handle层数值限制：startIndex=3超出便签数量1，返回空列表"""
        info("新建日历便签A")
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 3,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "responseTime": int,
            "webNotes": []
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase02_Remind_handle(self):
        """查询日历便签接口，handle层数值限制：新建两条日历便签，rows为1，返回最新一条"""
        info("新建日历便签A")

        remind_time = int(datetime.now().timestamp() * 1000)
        notes = self.api.create_notes(num=2, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        note_id = notes[1]["noteId"]
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 1,
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

    def testCase03_Remind_handle(self):
        """查询日历便签接口，handle层越权：用户A创建一条日历便签，用户B查询"""
        info("新建日历便签A")
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("查询便签A")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id2,
                              sid=self.sid2)
        expect = {
            "errorCode": -2010, "errorMsg": ""
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)

    def testCase04_Remind_handle(self):
        """查询日历便签接口，handle层状态变化：新建日历便签后移除日历，查询不到返回空列表"""
        info("新建日历便签A")
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        note_id = note[0]["noteId"]
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("移除便签A，更新便签主体为普通便签")
        body = {
            'noteId': note_id,
            'star': 0,
            'remindTime': 0,
            'remindType': 0
        }
        res = BusinessRe.post(url=Url.url_note_info, body=body, userid=self.user_id1,
                              sid=self.sid1)
        info("查询日历便签")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "responseTime": int,
            "webNotes": []}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase05_Remind_handle(self):
        """查询日历便签接口，handle层状态变化：新建普通便签后改成日历便签，可以查询到该条便签"""
        info("新建普通便签A")
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("更新便签主体为日历便签")
        body = {
            'noteId': note_id,
            'star': 0,
            'remindTime': remind_time,
            'remindType': 1
        }
        res = BusinessRe.post(url=Url.url_note_info, body=body, userid=self.user_id1,
                              sid=self.sid1)
        info("查询日历便签")
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
            ]}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase06_Remind_handle(self):
        """查询日历便签接口，handle层状态变化：新建日历便签后删除便签，查询不到返回空列表"""
        info("新建普通便签A")
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("删除便签")
        body = {
            'noteId': note_id
        }
        res = BusinessRe.post(url=Url.url_delete_note, body=body, userid=self.user_id1,
                              sid=self.sid1)
        info("查询日历便签")
        body = {
            "remindStartTime": start_timestamp,
            "remindEndTime": end_timestamp,
            "startIndex": 0,
            "rows": 50}
        res = BusinessRe.post(url=Url.url_remind, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {
            "responseTime": int,
            "webNotes": []}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase07_Remind_handle(self):
        """查询日历便签接口，handle层状态变化：新建日历便签后删除便签再恢复，可以查询到该条便签"""
        info("新建日历便签A")
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        note_id = note[0]["noteId"]
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        info("删除便签")
        body = {
            'noteId': note_id
        }
        res = BusinessRe.post(url=Url.url_delete_note, body=body, userid=self.user_id1,
                              sid=self.sid1)
        info("恢复回收站的便签")
        url = self.host + f'/v3/notesvr/user/{self.user_id1}/notes'
        body = {
            "userId": self.user_id1,
            "noteIds": [note_id]
        }
        self.ba.patch(url=url, body=body, userid=self.user_id1, sid=self.sid1)

        info("查询日历便签")
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
                    "infoVersion": 3,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": "test",
                    "summary": "test",
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }
            ]}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase08_Remind_handle(self):
        """查询日历便签接口，handle层处理数量：新建三条日历便签后删除三条便签，查询不到返回空列表"""
        info("新建三条日历便签")
        remind_time = int(datetime.now().timestamp() * 1000)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        notes = self.api.create_notes(num=3, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        info("删除所有便签")
        ApiMethod.delete_notes(userid=self.user_id1, sid=self.sid1)
        info("查询日历便签")
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

    def testCase09_Remind_handle(self):
        """查询日历便签接口，handle层处理数量：新建三条日历便签后移除日历三条便签，查询不到返回空列表"""
        info("新建三条日历便签")
        remind_time = int(datetime.now().timestamp() * 1000)
        start_timestamp, end_timestamp = self.ba.get_month_timestamp(datetime.now())
        notes = self.api.create_notes(num=3, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)

        info("所有便签更改为普通便签")
        for i in range(3):
            note_id = notes[i]["noteId"]
            body = {
                'noteId': note_id,
                'star': 0,
                'remindTime': 0,
                'remindType': 0
            }
            res = BusinessRe.post(url=Url.url_note_info, body=body, userid=self.user_id1,
                                  sid=self.sid1)
        info("查询日历便签")
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
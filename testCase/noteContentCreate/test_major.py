import time
import unittest
from datetime import datetime

import requests

from business.api_method import ApiMethod
from common.general_assert import GeneralAssert
from common.yamlRead import YamlRead
from common.logs import class_case_decoration
from business.BusinessRe import BusinessRe
from data.data import Url


@class_case_decoration
class NoteContentCreateMajor(unittest.TestCase):
    apiConfig = YamlRead().api_config()['note_create_content']
    envConfig = YamlRead().env_config()
    user_id1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    url = host + apiConfig['path']
    ga = GeneralAssert()
    api = ApiMethod()

    def setUp(self):
        """前置数据清理"""
        # 删除所有便签
        ApiMethod.delete_notes(userid=self.user_id1, sid=self.sid1)
        # 删除所有分组
        ApiMethod.delete_groups(userid=self.user_id1, sid=self.sid1)

    def testCase01_NoteContentCreate_major(self):
        """上传/更新便签内容接口， 主流程：上传普通便签内容"""
        # 上传便签主体
        note_id = str(int(time.time() * 1000))
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {
            'noteId': note_id,
            'star': 0
        }
        res = requests.post(url=Url.url_note_info, headers=headers, json=body)
        # 上传便签内容
        body = {"title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int,
                  "contentVersion": 1,
                  "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

        # 数据源校验（查询这条便签内容）
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_note_body, headers=headers, body=body, userid=self.user_id1, sid=self.sid1)
        expect = {
                    "responseTime": int,
                    "noteBodies": [
                        {
                            "summary": "test",
                            "noteId": note_id,
                            "infoNoteId": str,
                            "bodyType": 0,
                            "body": "test",
                            "contentVersion": 1,
                            "contentUpdateTime": int,
                            "title": "test",
                            "valid": 1
                        }
                    ]
                }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase02_NoteContentCreate_major(self):
        """上传/更新便签内容接口， 主流程：上传日历便签内容"""
        # 上传便签主体
        note_id = str(int(time.time() * 1000))
        remind_time = int(datetime.now().timestamp() * 1000)
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {
            'noteId': note_id,
            'star': 0,
            'remindTime': remind_time,
            'remindType': 0
        }
        res = requests.post(url=Url.url_note_info, headers=headers, json=body)
        # 上传便签内容
        body = {"title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "noteId": note_id,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int,
                  "contentVersion": 1,
                  "contentUpdateTime": int}

        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)
        # 数据源校验（查询这条便签内容）
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_note_body, headers=headers, body=body, userid=self.user_id1, sid=self.sid1)
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": "test",
                    "noteId": note_id,
                    "infoNoteId": str,
                    "bodyType": 0,
                    "body": "test",
                    "contentVersion": 1,
                    "contentUpdateTime": int,
                    "title": "test",
                    "valid": 1
                }
            ]
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase03_NoteContentCreate_major(self):
        """上传/更新便签内容接口， 主流程：上传分组便签内容"""
        # 上传便签主体
        note_id = str(int(time.time() * 1000))
        group_id = int(datetime.now().timestamp() * 1000)
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {
            'noteId': note_id,
            'star': 0,
            'groupId': group_id
        }
        res = requests.post(url=Url.url_note_info, headers=headers, json=body)

        # 上传便签内容
        body = {"title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "noteId": note_id,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int,
                  "contentVersion": 1,
                  "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

        # 数据源校验（查询这条便签内容）
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_note_body, headers=headers, body=body, userid=self.user_id1, sid=self.sid1)
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": "test",
                    "noteId": note_id,
                    "infoNoteId": str,
                    "bodyType": 0,
                    "body": "test",
                    "contentVersion": 1,
                    "contentUpdateTime": int,
                    "title": "test",
                    "valid": 1
                }
            ]
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase04_NoteContentCreate_major(self):
        """上传/更新便签内容接口， 主流程：更新普通便签内容"""
        # 新建便签A
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        # 更新便签A内容
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int,
                  "contentVersion": 2,
                  "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

        # 数据源校验（查询这条便签内容）
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_note_body, headers=headers, body=body, userid=self.user_id1, sid=self.sid1)
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": "test1",
                    "noteId": note_id,
                    "infoNoteId": str,
                    "bodyType": 0,
                    "body": "test1",
                    "contentVersion": 2,
                    "contentUpdateTime": int,
                    "title": "test1",
                    "valid": 1
                }
            ]
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase05_NoteContentCreate_major(self):
        """上传/更新便签内容接口， 主流程：更新日历便签内容"""
        # 新建便签A
        remind_time = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, remind_time=remind_time)
        note_id = note[0]["noteId"]

        # 更新便签A内容
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int,
                  "contentVersion": 2,
                  "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

        # 数据源校验（查询这条便签内容）
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_note_body, headers=headers, body=body, userid=self.user_id1, sid=self.sid1)
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": "test1",
                    "noteId": note_id,
                    "infoNoteId": str,
                    "bodyType": 0,
                    "body": "test1",
                    "contentVersion": 2,
                    "contentUpdateTime": int,
                    "title": "test1",
                    "valid": 1
                }
            ]
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase06_NoteContentCreate_major(self):
        """上传/更新便签内容接口， 主流程：更新分组便签内容"""
        # 新建便签A
        group_id = int(datetime.now().timestamp() * 1000)
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1, group_id=group_id)
        note_id = note[0]["noteId"]
        # 更新便签A内容
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int,
                  "contentVersion": 2,
                  "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

        # 数据源校验（查询这条便签内容）
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_note_body, headers=headers, body=body, userid=self.user_id1, sid=self.sid1)
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": "test1",
                    "noteId": note_id,
                    "infoNoteId": str,
                    "bodyType": 0,
                    "body": "test1",
                    "contentVersion": 2,
                    "contentUpdateTime": int,
                    "title": "test1",
                    "valid": 1
                }
            ]
        }
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)



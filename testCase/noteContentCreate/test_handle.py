import time
import time
import unittest


import requests

from business.api_method import ApiMethod
from common.general_assert import GeneralAssert
from common.yamlRead import YamlRead
from common.logs import class_case_decoration, info
from business.BusinessRe import BusinessRe
from data.data import Url


@class_case_decoration
class NoteContentCreateHandle(unittest.TestCase):
    apiConfig = YamlRead().api_config()['note_create_content']
    envConfig = YamlRead().env_config()
    user_id1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    user_id2 = envConfig['userid2']
    sid2 = envConfig['sid2']
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

    def testCase01_NoteContentCreate_handle(self):
        """上传/更新便签内容接口，数值限制: 第一次上传便签内容时localContentVersion值为1"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')
        note_id = str(int(time.time() * 1000))
        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {
            'noteId': note_id,
            'star': 0
        }
        res = requests.post(url=Url.url_note_info, headers=headers, json=body)
        # 上传便签内容
        body = {"noteId": note_id,
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 1,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase02_NoteContentCreate_handle(self):
        """上传/更新便签内容接口，数值限制: 更新便签内容时传入localContentVersion值为4"""
        # 新建便签A
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        # 更新便签A内容
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 4,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -1003, "errorMsg": "content version not equal!"}
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase03_NoteContentCreate_handle(self):
        """上传便签内容接口，handle层越权：用户A新建1条便签A，用户B更新便签A的内容"""
        # 新建便签A
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        # 更新便签A内容
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, body=body, userid=self.user_id2,
                              sid=self.sid2)
        expect = {"errorCode": -2010, "errorMsg": ""}
        self.ga.http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)

    def testCase04_NoteContentCreate_handle(self):
        """上传便签内容接口，handle层越权：用户A新建1条便签A，用户A的userid+用户B的sid更新便签A的内容"""
        # 新建便签A
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        # 更新便签A内容
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, body=body, userid=self.user_id1,
                              sid=self.sid2)
        expect = {"errorCode": -2010, "errorMsg": ""}
        self.ga.http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)

    def testCase05_NoteContentCreate_handle(self):
        """上传便签内容接口，handle层越权：用户A新建1条便签A，用户B的userid+用户A的sid更新便签A的内容"""
        # 新建便签A
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        # 更新便签A内容
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, body=body, userid=self.user_id2,
                              sid=self.sid1)
        expect = {"errorCode": -2010, "errorMsg": ""}
        self.ga.http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)

    def testCase06_NoteContentCreate_handle(self):
        """上传便签内容接口，handle层状态转变：新建便签A后删除，更新便签A内容"""
        info("新建便签A后删除")
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        body = {"noteId": note_id}
        res = BusinessRe.post(url=Url.url_delete_note, body=body, userid=self.user_id1,
                              sid=self.sid1)
        info("更新便签A内容")
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -2010, "errorMsg": ""}
        self.ga.http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)

    def testCase07_NoteContentCreate_handle(self):
        """上传便签内容接口，handle层状态转变：新建便签A后删除并清空回收站，更新便签A内容"""
        info("新建便签A后删除并清空回收站")
        note = self.api.create_notes(num=1, userid=self.user_id1, sid=self.sid1)
        note_id = note[0]["noteId"]
        body = {"noteId": note_id}
        res = BusinessRe.post(url=Url.url_delete_note, body=body, userid=self.user_id1,
                              sid=self.sid1)
        body = {"noteIds": [note_id]}
        res = BusinessRe.post(url=Url.url_clean_recyclebin, body=body, userid=self.user_id1,
                              sid=self.sid1)
        info("更新便签A内容")
        body = {"title": "test1",
                "summary": "test1",
                "body": "test1",
                "localContentVersion": 1,
                "noteId": note_id,
                "bodyType": 0}
        res = BusinessRe.post(url=Url.url_update_note_content, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -2010, "errorMsg": ""}
        self.ga.http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)
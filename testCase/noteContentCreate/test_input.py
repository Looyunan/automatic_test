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
class NoteContentCreateInput(unittest.TestCase):
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

    def testCase01_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项缺失: noteId"""
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
        body = {"title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase02_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项缺失: title"""
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
        body = {
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "noteId": note_id,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase03_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项缺失: summary"""
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
        body = {
                "title": "test",
                "body": "test",
                "localContentVersion": 0,
                "noteId": note_id,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase04_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项缺失: body"""
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
        body = {"summary": "test",
                "title": "test",
                "localContentVersion": 0,
                "noteId": note_id,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -1012, "errorMsg": "Note body Requested!"}
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase05_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项缺失: localContentVersion"""
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
        body = {"summary": "test",
                "title": "test",
                "body": "test",
                "noteId": note_id,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase06_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项缺失: bodyType"""
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
        body = {"summary": "test",
                "title": "test",
                "body": "test",
                "noteId": note_id,
                "localContentVersion": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase07_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为None: noteId"""
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
        body = {"noteId": None,
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase08_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为None: title"""
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
                "title": None,
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase09_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为None: summary"""
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
                "summary": None,
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase10_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为None: body"""
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
                "body": None,
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -1012, "errorMsg": "Note body Requested!"}
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase11_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为None: localContentVersion"""
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
                "localContentVersion": None,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase12_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为None: bodyType"""
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
                "localContentVersion": 0,
                "bodyType": None}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase13_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为"": noteId"""
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
        body = {"noteId": "",
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase14_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为"": title"""
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
                "title": "",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase15_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为"": summary"""
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
                "summary": "",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase16_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为"": body"""
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
                "body": "",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -1012, "errorMsg": "Note body Requested!"}
        self.ga.http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase17_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为"": localContentVersion"""
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
                "localContentVersion": "",
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase18_NoteContentCreate_input(self):
        """上传/更新便签内容接口，必填项值为"": bodyType"""
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
                "localContentVersion": 0,
                "bodyType": ""}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase19_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: noteId有特殊字符"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')
        note_id = str(int(time.time() * 1000)) + '@$%&!*'
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
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase20_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: noteId为特殊值-1"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')

        headers = BusinessRe.headers_post(self.user_id1, self.sid1)
        body = {
            'noteId': '-1',
            'star': 0
        }
        res = requests.post(url=Url.url_note_info, headers=headers, json=body)
        # 上传便签内容
        body = {"noteId": '-1',
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase21_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: noteId包含大写字母"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')
        note_id = str(int(time.time() * 1000)) + 'ALINLHU'
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
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase22_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: title长度超长"""
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
                "title": "test3woeinr'emgpwejfpwjwprephtpjep讷gipwhirthwprhtrigoetuoegnwobgorugbowruth",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase23_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: title包含中英文"""
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
                "title": "test3准备中",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase24_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: title包含特殊字符"""
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
                "title": "test3#@%￥",
                "summary": "test",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase25_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: summary长度超出"""
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
                "summary": "testtest3woeinr'emgpwejfpwjwprephtpjep讷gipwhirthwprhtrigoetuoegnwobgorugbowruth",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase26_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: summary包含特殊字符"""
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
                "summary": "testtest3#@%￥",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase27_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: summary包含中英文"""
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
                "summary": "testtest准备中",
                "body": "test",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase28_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: body长度超长"""
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
                "body": "testpwoerjtpwngoereiouhgoerhutohug'qwpenfpwqnowgbq维诺维护我hqtbogrenqrhbovfbguotgq",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase29_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: body包含特殊字符"""
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
                "body": "test%￥#！@&*",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase30_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: body包含中英文"""
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
                "body": "test准备好零售户改机票价格",
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"responseTime": int, "contentVersion": 1, "contentUpdateTime": int}
        self.ga.http_assert(expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase31_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: localContentVersion值为-1"""
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
                "localContentVersion": -1,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase32_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: bodyType值为-1"""
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
                "localContentVersion": 0,
                "bodyType": -1}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase33_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: noteId值为数字"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')
        note_id = int(time.time() * 1000)
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
                "localContentVersion": 0,
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase34_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: localContentVersion值为字符型数字”0“"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')
        note_id = int(time.time() * 1000)
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
                "localContentVersion": "0",
                "bodyType": 0}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase35_NoteContentCreate_input(self):
        """上传/更新便签内容接口，类型校验: bodyType值为字符型数字”0“"""
        # 上传便签主体
        info('用户A请求上传便签主体接口')
        note_id = int(time.time() * 1000)
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
                "localContentVersion": 0,
                "bodyType": "0"}

        res = BusinessRe.post(url=Url.url_update_note_content, headers=headers, body=body, userid=self.user_id1,
                              sid=self.sid1)
        expect = {"errorCode": -7, "errorMsg": "参数不合法！"}
        self.ga.http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

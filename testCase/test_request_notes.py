import copy
import unittest
from business.api_method import ApiMethod
from common.general_assert import GeneralAssert
from data.data import Basic, Url
from common.logs import class_case_decoration
from business.BusinessRe import BusinessRe


@class_case_decoration
class RequestNotes(unittest.TestCase):
    note_id1 = ''
    expect = {"responseTime": int,
              "webNotes":
                  [
                        {
                            "noteId": note_id1,
                            "createTime": int,
                            "star": 0,
                            "remindTime": 0,
                            "remindType": 0,
                            "infoVersion": 1,
                            "infoUpdateTime": int,
                            "groupId": None,
                            "title": str,
                            "summary": str,
                            "thumbnail": None,
                            "contentVersion": 1,
                            "contentUpdateTime": int
                        }
                    ]
              }
    web_notes_copy = copy.deepcopy(expect["webNotes"][0])

    def setUp(self):
        """前置处理：清理所有脏数据"""
        # 删除所有便签
        ApiMethod.delete_notes(userid=Basic.userid1, sid=Basic.sid1)
        # 删除所有分组
        ApiMethod.delete_groups(userid=Basic.userid1, sid=Basic.sid1)

    def testCase01_major(self):
        """查询首页便签接口，主流程：新建一条便签A然后查询"""

        # 新建便签A
        note_a = ApiMethod.create_notes(num=1, userid=Basic.userid1, sid=Basic.sid1)

        self.note_id1 = note_a[0]["noteId"]

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"][0]["noteId"] = self.note_id1

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase02_major(self):
        """查询首页便签接口，主流程：无数据时查询，期望返回0条数据"""

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"] = []

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase03_handle_startindex(self):
        """查询首页便签接口，Handle层startindex数值限制：新建两条便签A、B，查询时传入startindex为1,期望返回便签A的数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)
        note_a = notes_list[0]["noteId"]

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/1/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        print(self.expect["webNotes"])
        self.expect["webNotes"][0]["noteId"] = note_a

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase04_handle_startindex(self):
        """查询首页便签接口，Handle层startindex数值限制：新建两条便签A、B，查询时传入startindex为5,期望返回0条便签数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/5/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"] = []

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase05_handle_rows(self):
        """查询首页便签接口，Handle层rows数值限制：新建两条便签A、B，查询时传入rows为0,期望返回0条便签数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/0/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"] = []

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase06_handle_rows(self):
        """查询首页便签接口，Handle层rows数值限制：新建两条便签A、B，查询时传入rows为0,期望返回0条便签数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/0/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"] = []

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase07_handle_rows(self):
        """查询首页便签接口，Handle层rows数值限制：新建两条便签A、B，查询时传入rows为1,期望返回便签B数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)
        note_b = notes_list[1]["noteId"]
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/1/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"][0]["noteId"] = note_b

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase08_handle_rows(self):
        """查询首页便签接口，Handle层rows数值限制：新建两条便签A、B，查询时传入rows为2,期望返回便签A、B数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)
        note_a = notes_list[0]["noteId"]
        note_b = notes_list[1]["noteId"]

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/2/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)

        self.expect["webNotes"].append(self.web_notes_copy)
        self.expect["webNotes"][0]["noteId"] = note_b
        self.expect["webNotes"][1]["noteId"] = note_a

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase09_handle_rows(self):
        """查询首页便签接口，Handle层rows数值限制：新建两条便签A、B，查询时传入rows为1000,期望返回便签A、B数据"""
        # 新建两条便签A、B
        notes_list = ApiMethod.create_notes(num=2, userid=Basic.userid1, sid=Basic.sid1)
        note_a = notes_list[0]["noteId"]
        note_b = notes_list[1]["noteId"]
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/1000/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)

        self.expect["webNotes"].append(self.web_notes_copy)
        self.expect["webNotes"][0]["noteId"] = note_b
        self.expect["webNotes"][1]["noteId"] = note_a

        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase010_handle_over_permission(self):
        """查询便签接口，handle层越权：用户A新建1条便签A，用户B查询"""
        # 新建便签A
        notes_list = ApiMethod.create_notes(num=1, userid=Basic.userid1, sid=Basic.sid1)

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid2}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid2, sid=Basic.sid2, body=None)
        expect = {
                    "errorCode": -2010,
                    "errorMsg": ""
                    }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=401, actual_status_code=res.status_code)

    def testCase11_handle_status(self):
        """查询便签接口，handle层状态转变：新建一条便签A然后删除，期望：查询时返回0条数据"""
        # 新建便签A
        note = ApiMethod.create_notes(num=1, userid=Basic.userid1, sid=Basic.sid1)
        note_id = note[0]['noteId']
        # 删除便签A
        ApiMethod.delete_notes(userid=Basic.userid1, sid=Basic.sid1, note_ids=[note_id])
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"] = []
        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase12_handle_status(self):
        """查询便签接口，handle层状态转变：新建一条便签A并移动到分组中，期望：查询时返回0条数据"""
        # 新建便签A、分组A
        note = ApiMethod.create_notes(num=1, userid=Basic.userid1, sid=Basic.sid1)
        note_id = note[0]['noteId']
        group = ApiMethod.create_groups(num=1, userid=Basic.userid1, sid=Basic.sid1)
        group_id = group[0]['groupId']
        # 把便签移动到分组中
        body = {"noteId": note_id, "groupId": group_id}
        res = BusinessRe.post(url=Url.url_note_info, user_id=Basic.userid1, sid=Basic.sid1, body=body)

        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{Basic.userid1}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        self.expect["webNotes"] = []
        GeneralAssert().http_assert(self.expect, res.json(), expect_status_code=200, actual_status_code=res.status_code)

    def testCase13_input_must_key(self):
        """查询便签接口，input必填项：userid传入None"""
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/None/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
                    "errorCode": -7,
                    "errorMsg": "参数类型错误！"
                    }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase14_input_must_key(self):
        """查询便签接口，input必填项：userid传入空字符串"""
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/""/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "errorCode": -7,
            "errorMsg": "参数类型错误！"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase15_input_must_key(self):
        """查询便签接口，input必填项：userid缺失"""
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "timestamp": str,
            "status": 404,
            "error": "Not Found",
            "message": "No message available",
            "path": "/v3/notesvr/user/home/startindex/0/rows/50/notes"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=404, actual_status_code=res.status_code)

    def testCase16_input_type(self):
        """查询便签接口，input类型校验：userid长度超出"""
        userid = int(str(Basic.userid1) + '123')
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{userid}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "errorCode": -1011, "errorMsg": "user change!"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase17_input_type(self):
        """查询便签接口，input类型校验：userid长度不足"""
        userid = int(str(Basic.userid1)[:-2])
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/{userid}/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "errorCode": -1011, "errorMsg": "user change!"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase18_input_type(self):
        """查询便签接口，input类型校验：userid为0"""
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/0/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "errorCode": -1011, "errorMsg": "user change!"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=412, actual_status_code=res.status_code)

    def testCase19_input_type(self):
        """查询便签接口，input类型校验：userid为-1"""
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/-1/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "errorCode": -7,
            "errorMsg": "参数类型错误！"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)

    def testCase20_input_type(self):
        """查询便签接口，input类型校验：userid为小数2.5"""
        # 测试主流程
        url = Basic.host + f'/v3/notesvr/user/2.5/home/startindex/0/rows/50/notes'
        res = BusinessRe.get(url=url, user_id=Basic.userid1, sid=Basic.sid1, body=None)
        expect = {
            "errorCode": -7,
            "errorMsg": "参数类型错误！"
        }
        GeneralAssert().http_assert(expect, res.json(), expect_status_code=500, actual_status_code=res.status_code)
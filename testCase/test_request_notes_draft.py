import unittest
import uuid

import time


class RequestNotes(unittest.TestCase):
    host = 'http://note-api.wps.cn'
    userid1 = 380493413
    sid1 = 'V02SLhq3OBmoksCi_G89b13NGYSK8bo00a6f3d6f0016adde65'

    def test001_major(self):
        """查询首页便签接口，主流程：新建一条便签A然后查询"""
        # note_id1 = str(int(time.time() * 1000))
        # a = ApiMethod()
        # # a.create_note(note_id1)
        #
        # # 测试主流程
        # url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/50/notes'
        # headers = {'Cookie': f'wps_sid={self.sid1}',
        #            'X-user-key': str(self.userid1),
        #            'Content-Type': 'application/json'}
        # body = {}
        # res = requests.get(url=url, headers=headers, json=body)
        # # print(res.json()['webNotes'])
        # # print(type(res.json()['webNotes']))
        # # print(res.status_code)
        # # print(res.json())
        # # self.assertEqual(200, res.status_code, '状态码校验失败')
        # # self.assertTrue(len(res.json()['webNotes']) == 4)
        # # self.assertTrue(res.json()['webNotes'][0]['noteId'] == note_id1, 'noteId校验失败')
        #
        # a.delete_note(note_id1)
        #
        # print(res.json())
    # def tearDown(self):
    #     """清理数据"""
    #     url = self.host + ' /v3/notesvr/delete'
    #     headers = {'Cookie': f'wps_sid={self.sid1}',
    #                'X-user-key': str(self.userid1),
    #                'Content-Type': 'application/json'}
    #     body = {'noteId': '1731329049615'}
    #     res = requests.post(url, headers=headers, json=body)

    # expect = [
    #     {'noteId': '1731329049615'},
    #     {'responseTime': int, "ig": {'k': [str, str]}}
    # ]
    #
    # actual = [
    #     {'noteId': '1731329049615'},
    #     {'responseTime': 12, "ig": {'k': ['s', 'abc']}}
    # ]
    #
    # ak = GeneralAssert()
    # ak.http_assert(expect, actual)


if __name__ == '__main__':
    note_id1 = str(int(time.time() * 1000)) + str(uuid.uuid4())
    print(note_id1)

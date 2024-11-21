import time
import unittest

import requests
from data.data import Url, Basic
from datetime import datetime, timedelta
from business.BusinessRe import BusinessRe


class ApiMethod(unittest.TestCase):
    """封装常用方法：新建便签、新建分组、清空便签、删除分组"""
    @staticmethod
    def create_notes(num, userid, sid, group_id=None, remind_time=None):
        """通用的新建便签方法"""
        note_lists = []
        for i in range(num):
            note_id = str(int(time.time() * 1000))
            # 新建便签主体
            headers = BusinessRe.headers_post(userid, sid)
            if remind_time:   # 日历便签
                body = {
                    'noteId': note_id,
                    'star': 0,
                    'remindTime': remind_time,
                    'remindType': 1
                }
            elif group_id:   # 分组便签
                body = {
                    'noteId': note_id,
                    'star': 0,
                    'groupId': group_id
                }
            else:
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
            res = requests.post(Url.url_update_note_content, headers=headers, json=body)
            note_lists.append(body)
        return note_lists

    @staticmethod
    def delete_notes(userid, sid, note_ids=None, clear=True):
        """通用的清空便签方法，适用于所有类型的便签"""
        headers_post = BusinessRe.headers_post(userid, sid)
        headers_get = BusinessRe.headers_get(userid, sid)

        if note_ids is None:
            note_ids = []
            # step1 获取首页便签，提取noteId
            url = Basic.host + f'/v3/notesvr/user/{userid}/home/startindex/0/rows/50/notes'
            res = requests.get(url=url, headers=headers_get)
            for note in res.json()['webNotes']:
                note_ids.append(note['noteId'])
            # step2 获取日历便签，提取noteId
            # 获取当前月份，拿到开始和结束的时间戳
            now = datetime.now()

            # 获取当前月份的第一天
            first_day_of_month = now.replace(day=1)

            # 获取下个月的第一天
            # 如果当前月份是12月，则下个月就是明年的1月
            if now.month == 12:
                next_month_first_day = datetime(now.year + 1, 1, 1)
            else:
                next_month_first_day = datetime(now.year, now.month + 1, 1)

            # 获取当前月份的最后一天
            last_day_of_month = next_month_first_day - timedelta(days=1)

            # 将datetime对象转换为毫秒级时间戳
            start_timestamp = int(first_day_of_month.timestamp() * 1000)
            end_timestamp = int(last_day_of_month.timestamp() * 1000)

            # 构建数据格式
            body = {
                "remindEndTime": end_timestamp,
                "remindStartTime": start_timestamp,
                "startIndex": 0,
                "rows": 50
            }
            res = requests.post(url=Url.url_remind, headers=headers_post, json=body)
            for note in res.json()['webNotes']:
                note_ids.append(note['noteId'])
            # step3 获取分组便签，提取noteId
            # 获取分组列表
            body = {"excludeInValid": False}
            res = requests.post(url=Url.url_get_groups, headers=headers_post, json=body)
            if res.json()['noteGroups']:
                group_ids = []
                for group in res.json()['noteGroups']:
                    group_ids.append(group['groupId'])
                for group in group_ids:
                    body = {
                        "groupId": group,
                        "starIndex": 0,
                        "rows": 50
                    }
                    res = requests.post(url=Url.url_get_group_notes, headers=headers_post, json=body)
            # step4 循环noteId删除
            for note_id in note_ids:
                body = {"noteId": note_id}
                res = requests.post(url=Url.url_delete_note, headers=headers_post, json=body)
            # step5 清空回收站
            if clear:
                res = requests.post(url=Url.url_clean_recyclebin, headers=headers_post, json={"noteIds": ['-1']})

        else:
            for note_id in note_ids:
                body = {"noteId": note_id}
                res = requests.post(url=Url.url_delete_note, headers=headers_post, json=body)
            if clear:
                res = requests.post(url=Url.url_clean_recyclebin, headers=headers_post, json={"noteIds": ['-1']})

    @staticmethod
    def create_groups(num, userid, sid):
        """通用的新建分组方法"""
        group_list = []
        headers = BusinessRe.headers_post(userid, sid)
        for i in range(num):
            group_id = str(int(time.time() * 1000))
            body = {
                "groupId": group_id,
                "groupName": f'分组{i}',
                "order": 0
            }
            res = requests.post(url=Url.url_create_group, headers=headers, json=body)
            group_list.append(body)
        return group_list

    @staticmethod
    def delete_groups(userid, sid):
        """通用的删除分组方法"""
        # 查询到所有分组id
        group_list = []
        headers = BusinessRe.headers_post(userid, sid)
        body = {"excludeInValid": False}
        res = requests.post(url=Url.url_get_groups, headers=headers, json=body)
        if res.json()['noteGroups']:
            for group in res.json()['noteGroups']:
                group_list.append(group['groupId'])

        if group_list:
            for group_id in group_list:
                body = {'groupId': group_id}
                res = requests.post(url=Url.url_delete_group, headers=headers, json=body)



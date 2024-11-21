import calendar
from datetime import datetime

import requests
from common.logs import info, error


class BusinessRe:
    @staticmethod
    def post(url, userid, sid, body, headers=None):
        if headers is None:
            headers = {
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(userid),
                'Content-Type': 'application/json'
            }
        info(f'request url: {url}')
        info(f'request headers: {headers}')
        info(f'request body: {body}')
        try:
            res = requests.post(url, headers=headers, json=body, timeout=5)
        except TimeoutError:
            error(f'url: {url}, requests timeout!')
            return 'Request Timeout!'
        info(f'response code: {res.status_code}')
        info(f'response body: {res.text}')
        return res

    @staticmethod
    def get(url, userid, sid, body, headers=None):
        if headers is None:
            headers = {
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(userid)
            }
        info(f'request url: {url}')
        info(f'request headers: {headers}')
        info(f'request body: {body}')
        try:
            res = requests.get(url, headers=headers, json=body, timeout=5)
        except TimeoutError:
            error(f'url: {url}, requests timeout!')
            return 'Request Timeout!'
        info(f'response code: {res.status_code}')
        info(f'response body: {res.text}')
        return res

    @staticmethod
    def patch(url, userid, sid, body, headers=None):
        if headers is None:
            headers = {
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(userid)
            }
        info(f'request url: {url}')
        info(f'request headers: {headers}')
        info(f'request body: {body}')
        try:
            res = requests.patch(url, headers=headers, json=body, timeout=5)
        except TimeoutError:
            error(f'url: {url}, requests timeout!')
            return 'Request Timeout!'
        info(f'response code: {res.status_code}')
        info(f'response body: {res.text}')
        return res

    @staticmethod
    def headers_post(userid, sid):
        headers_post = {'Cookie': f'wps_sid={sid}',
                        'X-user-key': str(userid),
                        'Content-Type': 'application/json'}
        return headers_post

    @staticmethod
    def headers_get(user_id, sid):
        headers_get = {'Cookie': f'wps_sid={sid}',
                       'X-user-key': str(user_id)}
        return headers_get

    @staticmethod
    def get_month_timestamp(current):
        # 当前月份的开始时间
        first_day_of_month = datetime(current.year, current.month, 1)

        # 当前月份的结束时间
        last_day_of_month = datetime(current.year, current.month, calendar.monthrange(current.year, current.month)[1])

        # 转换为时间戳（以秒为单位）
        start_timestamp = int(first_day_of_month.timestamp() * 1000)
        end_timestamp = int(last_day_of_month.timestamp() * 1000)
        return start_timestamp, end_timestamp

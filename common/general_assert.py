import traceback
import unittest
from common.logs import error


class GeneralAssert(unittest.TestCase):
    def http_assert(self, expect, actual, expect_status_code, actual_status_code):
        """
        http返回体通用断言方法
        :param expect: dict or list，接口返回体的预期值
        :param actual: dict or list，实际结果的获取方式通常可以用 response.json()
        :param expect_status_code: int，预期状态返回码
        :param actual_status_code: int，实际状态返回码
        :return: True 断言成功，assert fail断言失败
        """
        try:
            self.assertEqual(expect_status_code, actual_status_code)
            if isinstance(expect, dict):
                self.assertEqual(len(expect.keys()), len(actual.keys()), msg=f'返回体字段长度不一致，实际返回的字段有:{list(actual.keys())}')
                for k, v in expect.items():
                    self.assertIn(k, actual.keys(), msg=f'{k}字段不在返回体中')
                    if isinstance(v, type):
                        self.assertEqual(v, type(actual[k]), msg=f'{k}字段类型与实际处理的类型不一致，实际返回的参数值: {actual[k]}')
                    elif isinstance(v, list):
                        self.assertEqual(len(expect[k]), len(actual[k]), msg=f'{k}列表元素长度不一致')
                        for index in range(len(expect[k])):
                            if isinstance(expect[k][index], type):
                                self.assertEqual(expect[k][index], type(actual[k][index]), msg=f'{actual[k][index]}类型与预期不一致')
                            elif isinstance(expect[k][index], dict):
                                self.http_assert(expect[k][index], actual[k][index], expect_status_code, actual_status_code)
                            else:
                                self.assertEqual(expect[k][index], actual[k][index], msg=f'返回值{actual[k][index]}与预期不一致')
                    elif isinstance(v, dict):
                        self.http_assert(expect[k], actual[k])
                    else:
                        self.assertEqual(v, actual[k], msg=f'{k}字段值不一致')

            else:
                self.assertEqual(len(expect), len(actual), msg=f'返回体字段长度不一致，实际返回的字段有:{list(actual)}')
                for index in range(len(expect)):
                    if isinstance(expect[index], type):
                        self.assertEqual(expect[index], type(actual[index]), msg=f'{actual[index]}类型与预期不一致')
                    elif isinstance(expect[index], dict):
                        self.http_assert(expect[index], actual[index], expect_status_code, actual_status_code)
                    elif isinstance(expect[index], list):
                        self.http_assert(expect[index], actual[index], expect_status_code, actual_status_code)
                    else:
                        self.assertEqual(expect[index], actual[index], msg=f'{actual[index]}的值与预期不一致')
        except Exception as e:
            error(f"An error occurred: {e}")
            # 打印完整的堆栈跟踪信息
            error(traceback.print_exc())

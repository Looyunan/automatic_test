from colorama import Fore
import functools
import time
import inspect
from datetime import datetime
import os
from main import DIR


def case(text):
    """
    打印用例信息并输出对应日志
    :param text: str 控制台要输出的内容或打印的日志文本数据
    :return:
    """
    formatted_time = datetime.now().strftime('%H:%M:%S:f')[:-3]  # 定义了日志的输出时间
    stack = inspect.stack()
    code_path = f'{os.path.basename(stack[1].filename)}:{stack[1].lineno}'  # 当前执行文件的绝对路径和执行代码行号
    content = f"[CASE]{formatted_time}-{code_path} >> {text}"
    print(Fore.LIGHTCYAN_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(Fore.LIGHTCYAN_EX + content + '\n')


def info(text):
    """
    打印用例运行时数据并输出对应日志
    :param text: str 控制台输出的内容或要打印的日志文本数据
    :return:
    """
    formatted_time = datetime.now().strftime('%H:%M:%S:f')[:-3]  # 定义了日志的输出时间
    stack = inspect.stack()
    code_path = f'{os.path.basename(stack[1].filename)}:{stack[1].lineno}'  # 当前执行文件的绝对路径和执行代码行号
    content = f"[INFO]{formatted_time}-{code_path} >> {text}"
    print(Fore.WHITE + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')


def error(text):
    formatted_time = datetime.now().strftime('%H:%M:%S:f')[:-3]  # 定义了日志的输出时间
    stack = inspect.stack()
    code_path = f'{os.path.basename(stack[1].filename)}:{stack[1].lineno}'  # 当前执行文件的绝对路径和执行代码行号
    content = f"[ERROR]{formatted_time}-{code_path} >> {text}"
    print(Fore.LIGHTRED_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(Fore.LIGHTRED_EX + content + '\n')
    with open(file=DIR + '\\logs\\' + f'{str_time}_error.log', mode='a', encoding='utf-8') as f:
        f.write(Fore.LIGHTRED_EX + content + '\n')


def case_decoration(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        class_name = args[0].__class__.__name__   # 获取类名
        method_name = func.__name__   # 获取方法名
        docstring = inspect.getdoc(func)   # 获取方法注释
        case('-------------------------------------------------------------')
        case(f"Method Name: {method_name}, Class Name: {class_name}")
        case(f"Test Description:{docstring}")
        result = func(*args, **kwargs)
        end = time.perf_counter()
        handle_time = end - start
        case('Case run time: %.2fs' % handle_time)
        return result
    return inner


def class_case_decoration(cls):
    """用例日志类级别装饰器"""
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name.startswith('testCase'):
            setattr(cls, name, case_decoration(method))
    return cls

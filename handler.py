import random
from time import sleep

from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all


xray_recorder.configure(service='My app')
# patch_all()


def handler1(event, context):
    # サブセグメント (1)
    subsegment = xray_recorder.begin_subsegment('my_subsegment')
    sleep(random.random())  # 何かしらの（計測対象にしたい）処理を実行する
    xray_recorder.end_segment()

    # サブセグメント (2)
    subsegment = xray_recorder.begin_subsegment('my_subsegment')
    sleep(random.random())  # 何かしらの（計測対象にしたい）処理を実行する
    xray_recorder.end_segment()

    return event


def handler2(event, content):
    return event

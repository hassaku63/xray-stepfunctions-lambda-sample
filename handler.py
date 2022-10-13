import random
from time import sleep

from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all


xray_recorder.configure(service='my-app')
# patch_all()


def handler1(event, context):
    # サブセグメント (1)
    subsegment_1 = xray_recorder.begin_subsegment('my_subsegment_1')
    sleep(random.random())  # 何かしらの（計測対象にしたい）処理を実行する
    subsegment_1.put_annotation('mykey', 'foo')
    xray_recorder.end_subsegment()

    # サブセグメント (2)
    subsegment_2 = xray_recorder.begin_subsegment('my_subsegment_2')
    sleep(random.random())  # 何かしらの（計測対象にしたい）処理を実行する
    xray_recorder.end_subsegment()

    return event


def handler2(event, content):
    return event

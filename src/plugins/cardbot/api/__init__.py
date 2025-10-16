from nonebot import get_bot
from nonebot.adapters import Bot, Event, Message
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent

from . import data

import os
script_path = os.path.split(os.path.realpath(__file__))[0]
import turso,re
connection = turso.connect(f"{script_path}/cardbot.db")
cursor = connection.cursor()


def reply(e:MessageEvent,msg:str) -> Message:
    """生成回复消息"""
    res=[{"type":"reply","data":{"id":str(e.message_id)}},{"type":"text","data":{"text":msg}}]
    return res

def sql(query,args=()) -> list:
    """这只是一个对sql进行简单封装的函数，确保每句sql都被预处理，不被坏人入侵"""
    res = cursor.execute(query, args)
    rows = res.fetchone()
    connection.commit()
    return rows

def getMuteTime(gid,uid) -> int:
    """获取禁言时间"""
    gt = f"G{gid}"
    try:
        return sql("select mutetime from ? WHERE uid == ?",(gt,uid))[0][0]
    except:
        return 0

def getAt(e:GroupMessageEvent) -> list:
    msg = str(e.raw_message)
    uid = re.findall("[0-9]{5,11}",msg)
    gt = f"G{e.group_id}"
    reg = sql("select mutetime from ? WHERE uid == ?",(gt,uid[0]))
    if len(reg) == 0:
        uid = []
    return uid
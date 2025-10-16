from nonebot import on_fullmatch, on_startswith, get_bot, on_message
from nonebot.adapters import Bot, Event, Message
from nonebot.matcher import Matcher
from nonebot.rule import is_type
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent

from api import sql
import time
authTime=on_message(is_type(GroupMessageEvent),priority=5,block=False)

@authTime.handle()
async def authFun(bot: Bot, e: GroupMessageEvent, matcher: Matcher):
    at = sql("select uid from auth WHERE gid == ?",(e.group_id,))
    if len(at) == 0:
        matcher.stop_propagation()
    else:
        sql(f"INSERT OR IGNORE INTO user \
                 (uid, time) values \
                 (?,?)",
                 (e.user_id,int(time.time)))
        sql(f"""CREATE TABLE IF NOT EXISTS G{e.group_id} (
                uid      INTEGER PRIMARY KEY,
                mutetime    INTEGER DEFAULT (0) NOT NULL,
                trapnum     INTEGER DEFAULT (0) NOT NULL,
                protecttime     INTEGER DEFAULT (0) NOT NULL
                )""")
        sql(f"INSERT OR IGNORE INTO G{e.group_id} \
                 (uid) values \
                 (?)",
                 (e.user_id,))
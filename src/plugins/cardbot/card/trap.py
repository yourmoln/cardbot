from nonebot import on_fullmatch, on_startswith, on_command
from nonebot.adapters import Bot, Event, Message
from nonebot.matcher import Matcher
from nonebot.rule import is_type
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent

from api import reply
card = {"/陷阱卡"}
cardTime=on_startswith(card,is_type(GroupMessageEvent),priority=20,block=True)

@cardTime.handle()
async def cardFun(bot: Bot, e: GroupMessageEvent, matcher: Matcher):
    msg=f"{card[0]}使用成功"
    msg_o=reply(e,msg)
    await bot.send_group_msg(group_id=str(e.group_id),message=msg_o)
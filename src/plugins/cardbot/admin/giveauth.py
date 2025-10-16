from nonebot import on_fullmatch, on_startswith
from nonebot.adapters import Bot, Event, Message
from nonebot.matcher import Matcher
from nonebot.rule import is_type
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent

from api import data,reply,sql
import time
cmd = {"/授权群聊"}
cmdTime=on_startswith(cmd,is_type(GroupMessageEvent),priority=3,block=True)
@cmdTime.handle()
async def cmdFun(bot: Bot, e: GroupMessageEvent, matcher: Matcher):
    if str(e.user_id) in data.admin.id or data.getWhite(e.user_id)>=2:
        cmd = str(e.get_message()).split(" ")
        if len(cmd)==1 or cmd[1] == '-h':
            msg='/授权群聊 [群号]'
        elif len(cmd)==2:
            query = "INSERT INTO auth (gid, time) VALUES (?, ?)"
            args=(cmd[1],int(time.time()))
            rows = sql(query,args)
            msg=f'授权成功[{cmd[1]}]'
        else:
            msg=f"请输入正确的指令格式"
        msg_o=reply(e,msg)
        await bot.send_group_msg(group_id=str(e.group_id),message=msg_o)
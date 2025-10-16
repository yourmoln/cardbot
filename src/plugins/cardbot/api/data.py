#此处的类型注释为数据库中的类型，虽然这样写不太规范，但是懒得改了
class USER:
    #用户数据
    uid:int = 'uid'#qq号
    white:int = 'white'#白名单，1是好人，0是拉黑，2是管理员
    sign:int = 'sign'#上次签到时间
    time:int = 'time'#首次使用时间
class CARD:
    #卡片数量
    trap:int = 'trap'#陷阱卡
    mute:int = 'mute'#禁言卡
    adventure:int = 'adventure'#冒险卡
    protect:int = 'protect'#保护卡
    unmute:int = 'unmute'#解禁卡
    gift:int = 'gift'#赠礼卡
    thief:int = 'thief'#小偷卡
class AUTH:
    #授权数据
    gid:int = 'gid'#群号
    time:int = 'time'#授权时间
#非数据库数据
class admin:
    id:list = ['3402824831','617802189']#固定管理员
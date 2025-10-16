import sys,os
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)

import card,admin,api,auth

#数据表不存在则创建
api.sql("""CREATE TABLE IF NOT EXISTS user (
        uid      INTEGER PRIMARY KEY,
        white    INTEGER DEFAULT (1) NOT NULL,
        sign     INTEGER DEFAULT (0) NOT NULL,
        time     INTEGER DEFAULT (0) NOT NULL
    )""")
api.sql("""CREATE TABLE IF NOT EXISTS auth (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        gid  INTEGER NOT NULL,
        time INTEGER NOT NULL
    );""")
api.sql("""CREATE TABLE IF NOT EXISTS card (
        uid      INTEGER PRIMARY KEY,
        trap     INTEGER DEFAULT (0) NOT NULL,
        mute     INTEGER DEFAULT (0) NOT NULL,
        adventure   INTEGER DEFAULT (0) NOT NULL,
        protect  INTEGER DEFAULT (0) NOT NULL,
        unmute INTEGER DEFAULT (0) NOT NULL,
        thief INTEGER DEFAULT (0) NOT NULL,
        gift  INTEGER DEFAULT (0) NOT NULL
    )""")
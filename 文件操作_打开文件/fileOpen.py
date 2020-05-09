
@author: WANGLEI
"""

import win32api
#win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 0)      # 后台执行
#win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)      # 前台打开
#win32api.ShellExecute(0, 'open', 'notepad.exe', 'ne555.pdf', '', 1)   # 打开文件
#win32api.ShellExecute(0, 'open', 'http://www.sohu.com', '', '', 1)  # 打开网页
#win32api.ShellExecute(0, 'open', 'D:\\Opera.mp3', '', '', 1)     # 播放视频
win32api.ShellExecute(0, 'open', 'C:\\Users\\WANGLEI\\Desktop\\我的gui\\09.28\\用户\\ne555.pdf', '', '', 1)     # 运行程序

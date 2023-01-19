## About
通过 telegram bot 发送屏幕截图，结合工作排程器或crontab功能可实现定时通知

## Feature

* 引用 pyautogui 库, 截取屏幕截图，将其保存到png文件中
* 通过 telegram bot 将屏幕截图发送到指定群组中
* 使用 send_screenshot.vbs 背景執行并将cmd命令窗口隐藏
* 配置文件设置chat_id和token

## Requires
Python 3.11.0  
pyautogui 0.9.53  
requests 2.28.1  
configparser 5.3.0  

## Usage
```
python main.py
```
![image](https://raw.githubusercontent.com/joanbabyfet/md_img/master/send_screenshot/display.jpg)

## Change Log
v1.0.0

## Maintainers
Alan

## LICENSE
[MIT License](https://github.com/joanbabyfet/send_screenshot/blob/master/LICENSE)
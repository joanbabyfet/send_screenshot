import pyautogui
import requests
import configparser
import os

# 配置文件
config_file = 'config.ini'

# 发送图片
def send_photo(img_url):
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='utf-8') # 这里要加utf-8, 否则会报错, 默认gbk
    config_section  = 'telegram_config'
    token   = conf.get(config_section, 'token') # 存取令牌
    chat_id = conf.get(config_section, 'chat_id') # 用户或群组id

    files = {
        'photo': open(img_url, 'rb') # rb用二进制格式打开1个文件用于只读
    }
    resp = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}', files = files)
    return resp.json()

def main():
    try:
        filename = 'capture.png'
        #screen = pyautogui.screenshot(region = (0, 0, 300, 400)) # 屏幕区域截图, 左上宽高
        screen = pyautogui.screenshot() # 屏幕截图
        screen.save(filename)           # 保存图片
        
        if os.path.exists(filename):
            send_photo(filename)      # 发送图片
            print(f'屏幕截图 {filename} 通知成功')
        else:
            print(f'屏幕截图 {filename} 不存在')
    except Exception as e:
        print(f'屏幕截图 {e} 通知失败')

if __name__ == '__main__': # 主入口
    main()
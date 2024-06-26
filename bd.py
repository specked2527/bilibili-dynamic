import json
import time
import requests

 
# 添加请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie':'buvid3=...; b_nut=...; _uuid=...; buvid4=...;' # 填写你的Cookie
}

# 原始的 print 函数
rewrite_print = print

# 定义新的 print 函数
def print(*arg):
    file_path = './data.json'
    
    # 打印到控制台
    rewrite_print(*arg)
    
    # 保存到文件
    rewrite_print(*arg, file=open(file_path, "a", encoding="utf-8"))
    
    #if __name__ == '__main__':
    #print(" ")    

def fetch_data(offset):
 
    # 每次请求时延时0.5秒
    time.sleep(0.5)
 
    # 请求的URL
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space"
 
    # 请求参数
    params = {
        "offset": offset,
        "host_mid": 698149922 # 填写你的up主id
    }
 
    # 发送请求
    response = requests.get(url, params=params, headers=headers)
 
    # 解析json数据
    data = response.json()
    jsonf = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    print(jsonf) # 保存为json对象
 
    # 检查是否有更多数据
    if data['data']['has_more']:
        # 如果有更多数据，使用新的offset发起新的请求
        fetch_data(data['data']['offset'])
 
# 从offset为空开始
fetch_data("")


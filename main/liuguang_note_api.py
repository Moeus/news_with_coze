import requests
import json
import time
# 获取当前时间的时间元组
current_time = time.localtime()
# 提取年、月、日
year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday

def get_png(content):
    # 目标 URL，需要替换为实际的接口地址
    target_url = "https://fireflycard-api.302ai.cn/api/saveImg"

    try:
        # 打开 JSON 文件，使用 'r' 模式以文本形式读取，并指定编码为 UTF-8
        with open("api.json", 'r', encoding='utf-8') as file:
            # 使用 json.load() 函数从文件对象中读取并解析 JSON 数据
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print("未找到指定的 JSON 文件。")
    except json.JSONDecodeError:
        print("JSON 文件解析错误，可能不是有效的 JSON 格式。")
    # 定义请求头，如果没有特殊需求，默认设置内容类型为 JSON
    data["content"]=content
    data["title"]=f"<p>👋{year}-{month}-{day}热点新闻😺💕</p>"
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # 发送 POST 请求，使用 json 参数传递 JSON 数据
        response = requests.post(target_url, json=data, headers=headers, timeout=100)
        # 检查响应状态码，如果不是 200 会抛出 HTTPError 异常
        response.raise_for_status()

        # 定义要保存的文件路径
        file_path = f'../output/{year}-{month}-{day}.png'
        # 以二进制写入模式打开文件
        with open(file_path, 'wb') as file:
            # 将响应的二进制内容写入文件
            file.write(response.content)
        print(f"图像已成功保存到 {file_path}")
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP 错误发生: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'连接错误发生: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'请求超时: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'请求发生未知错误: {req_err}')
    return 1
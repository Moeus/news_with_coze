"""
此示例描述了如何使用工作流接口进行聊天。
"""
import liuguang_note_api
import json
import os
# 我们官方的 Python 版 Coze SDK [cozepy](https://github.com/coze-dev/coze-py)
from cozepy import COZE_CN_BASE_URL

# 通过个人访问令牌或 OAuth 获取访问令牌。
coze_api_token = 'pat_yUmVBjZAhTbmF90GZjKcysB7UrTKQ4GevS33z5AadZQxqweT4Jni0ZdlDIiKBTLA'
# 默认访问地址是 api.coze.com，但如果你需要访问 api.coze.cn，
# 请使用 base_url 来配置要访问的 API 端点
coze_api_base = COZE_CN_BASE_URL

from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType 

try:
    # 通过访问令牌初始化 Coze 客户端。
    coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

    # 在 Coze 中创建一个工作流实例，从网页链接中复制最后一个数字作为工作流的 ID。
    workflow_id = '7475598695737229346'

    # 定义工作流运行的参数
    parameters = {
        "secret_key": "Moeus"
    }

    # 调用 coze.workflows.runs.create 方法来创建一个工作流运行实例
    # 是非流式聊天，将返回一个 WorkflowRunResult 类的对象。
    workflow = coze.workflows.runs.create(
        workflow_id=workflow_id,
        parameters=parameters  # 将参数添加到工作流运行中
    )
    print(type(workflow.data))
    print(workflow.data)
    result_json=json.loads(workflow.data)
    context = result_json["result"]
    context="".join(context.split("\n"))
    print(context)
    print(liuguang_note_api.get_png(content=context))
except Exception as e:
    print(f"发生错误: {e}")
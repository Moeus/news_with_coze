"""
This example describes how to use the workflow interface to chat.
"""

import os
# Our official coze sdk for Python [cozepy](https://github.com/coze-dev/coze-py)
from cozepy import COZE_CN_BASE_URL

# Get an access_token through personal access token or oauth.
coze_api_token = 'pat_yUmVBjZAhTbmF90GZjKcysB7UrTKQ4GevS33z5AadZQxqweT4Jni0ZdlDIiKBTLA'
# The default access is api.coze.com, but if you need to access api.coze.cn,
# please use base_url to configure the api endpoint to access
coze_api_base = COZE_CN_BASE_URL

from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  # noqa



try:
    # Init the Coze client through the access_token.
    coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

    # Create a workflow instance in Coze, copy the last number from the web link as the workflow's ID.
    workflow_id = '7475598695737229346'

    # Define the parameters for the workflow run
    parameters = {
        "secret_key": "Moeus"
    }

    # Call the coze.workflows.runs.create method to create a workflow run. The create method
    # is a non-streaming chat and will return a WorkflowRunResult class.
    workflow = coze.workflows.runs.create(
        workflow_id=workflow_id,
        parameters=parameters  # Add the parameters to the workflow run
    )

    print("workflow.data", workflow.data)
    context=workflow.data["result"]

except Exception as e:
    print(f"An error occurred: {e}")


# CosBucketDownload

帮助下载你在 CosBucket 中的文件夹，如果你有需要的话。

## 使用

修改 `config.json`，填入你的永久密钥信息（无临时密钥支持），注意 `folder` 在末尾添加 `/` 符号表示文件夹。

1. `pip install rich cos-python-sdk-v5`
2. `python download.py`

下载目录：`./{folder}`

# 使用 Ubuntu 最新版本作為基礎映像檔
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 設定工作目錄
WORKDIR /app

COPY . .

# # 安裝所需套件
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip install requests
RUN pip install playwright
RUN playwright install

CMD [ "python3", "main.py" ]
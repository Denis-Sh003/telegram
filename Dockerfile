#Telegram bot

FROM ubuntu

MAINTAINER w2r

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update && apt install iputils-ping curl vim python3 python3-pip -y
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/src/app
CMD [ "python3", "bot.py" ]

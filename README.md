# telegram
# install python-telegram-bot
pip3 install python-telegram-bot==12 --upgrade

# Creating a service for telegram bot
vim /etc/systemd/system/telegram-bot.service
```
[Unit]
Description=Telegram bot
After=network.target
[Service]
Environment=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/snap/bin:/home/pi/scripts/bot
ExecStart=/home/pi/scripts/bot/bot.sh
[Install]
WantedBy=multi-user.target
```
#We issue the necessary rights to the file.
chmod 664 /etc/systemd/system/telegram-bot.service

systemctl daemon-reload
systemctl enable telegram-bot.service
systemctl start telegram-bot.service
systemctl status telegram-bot.service

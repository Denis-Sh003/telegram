# telegram bot
This telegram bot can start a regular computer by emulating the power button presses.\
After installing it, the following commands will be available:
```
list of available commands:
     / id - user id
     / curlsh - find out ip telegram bot
     / powersh - simulate pressing the power button ~ 0.5c
     / longpowersh - simulate a long press of the power button ~ 8c
     / pingsh - check server availability via ping
```
install python-telegram-bot
pip3 install python-telegram-bot==12 --upgrade

Iron component. In my case, the irfz24n bridge was used
![image](https://user-images.githubusercontent.com/85823955/122686835-059ca000-d21c-11eb-87d1-cffb8d8cdc9b.png)

Работа транзистора в режиме «ключа»

При наличии на затворе транзистора (зелёный провод) уровня логического «0» (Uзи < 2 В), транзистор будет «закрыт» и ток через нагрузку Rн течь не будет.\
При наличии на затворе транзистора (зелёный провод) уровня логической «1» (Uзи > 4 В), транзистор будет «открыт» и через нагрузку Rн потечёт ток.\
При использовании сигнала ШИМ можно плавно увеличивать или уменьшать скорость вращения мотора или яркость свечения лампы (светодиода).\
Назначение элементов схемы\
Rн - нагрузка которой управляет транзистор (лампочки, мощные светодиоды, двигатели, сервоприводы и т.д.)\
Rз - ограничительный резистор цепи затвора, предназначен для ограничения тока перезаряда затвора. Если управление транзистором осуществляется при помощи Arduino и на одном \выходе Arduino находится только один транзистор, то резистор Rз можно исключить из схемы.\
Rзи - прижимающий резистор цепи затвора, гарантирует что при разрыве цепи управляющего напряжения транзистор закроется. Если в Вашей схеме невозможно отключение цепи \управляющего напряжения, то резистор Rзи можно исключить из схемы.

The control signal is connected to the 19th raspberry \
The ground of the raspberry must be connected to the ground of the power button.

When using a relay, everything is much easier. You just need to supply ground, + 5V and a control signal to the relay. On the other hand, just plug in the wires from the power button.

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
In path you need to add the path where the scripts are located. \
Specify the ExecStart path before the bot.sh file \
We issue the necessary rights to the file.
```
chmod 664 /etc/systemd/system/telegram-bot.service
```
```
systemctl daemon-reload
systemctl enable telegram-bot.service
systemctl start telegram-bot.service
systemctl status telegram-bot.service
```

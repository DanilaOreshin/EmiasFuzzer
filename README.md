# EmiasFuzzer

Данный скрипт создан для бронирования визита к доктору в системе ЕМИАС. Бывает ситуация, когда к некоторым специалистам свободные ячейки для записи разлетаются, как горячие пирожки, и ты не успеваешь нажать на кнопку. В системе ЕМИАС запись открывается примерно в 8 утра МСК (речь про московский регион). И как-то раз моя мама не могла долгое время записаться на прием, и данная проблема вылилась в создание этого скрипта :)

## Принцип работы
Скрипт просто пытается забронировать визит на первый попавшийся доступный интервал и продолжает попытки в цикле до тех пор, пока не получится.

## Инструкция
Необходимо в файле config.py прописать личные данные, запустить main.py и идти пить чай :)

## Предложения по улучшению
Можно переделать данный скрипт под Телеграм-бота, где можно будет конфигурировать данные через общение с ним. Плюс это дает возможность не запускать скрипт локально.

import logging

# personal data
omsNumber = '7700001111111111'  # Номер медицинского полиса
birthDate = '1992-03-11'  # Дата рождения
specialityId = '3'  # Идентификатор специальности врача, см. список ниже
doctorLastName = "ТЕСТ"  # Фамилия врача

# ----- specialityId list -----
#
# 200 - Участковый врач
# 2 - Уролог
# 3 - Хирург
# 2008 - Диспансеризация/Профилактический мед.осмотр
# 6 - Офтальмолог
# 2017 - Дежурный врач ОРВИ
# 2004 - Медицинский пост
# 603 - Оториноларинголог
# 2011 - Вакцинация от COVID-19


# script settings
delay_sec = 15

# logger config
log_level = logging.DEBUG
logger_message_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger_file_name = './logs/log.log'

# api params
jsonrpc = '2.0'
api_version = 'v1'
url = f'https://emias.info/api/emc/appointment-eip/{api_version}'

# jsonpath expressions
docIdJsonPath = f'$.result[?(@.mainDoctor.lastName == "{doctorLastName}")].id'
receptionTypeIdJsonPath = f'$.result[?(@.mainDoctor.lastName == "{doctorLastName}")].receptionType[:].code'
compResIdJsonPath = '$.result[?(@.id == {0})].complexResource[?(@.room)].id'
startTimeJsonPath = '$.result.scheduleOfDay[0].scheduleBySlot[0].slot[0].startTime'
endTimeJsonPath = '$.result.scheduleOfDay[0].scheduleBySlot[0].slot[0].endTime'
appointmentIdJsonPath = '$.result.appointmentId'

import time

import jsonpath

import utils.config as cfg
from utils.body import Body
from utils.logger import logger
from utils.sender import send
from utils.util import get_uuid

docInfoBodyObj = Body('getDoctorsInfo')
availableResInfoBodyObj = Body('getAvailableResourceScheduleInfo')
createAppointmentBodyObj = Body('createAppointment')


def reserve_any():
    data = []

    while True:
        # configure Body class object and send "getDoctorsInfo" request
        docInfoBodyObj.id = get_uuid()
        DocInfoRespBody = send(docInfoBodyObj.to_json()).json()
        logger.debug(f'Response body = {DocInfoRespBody}')

        # parsing response body
        doctorIds = jsonpath.jsonpath(DocInfoRespBody, cfg.docIdJsonPath)
        receptionTypeId = str(jsonpath.jsonpath(DocInfoRespBody, cfg.receptionTypeIdJsonPath)[0])

        for doctorId in doctorIds:
            tempResIds = jsonpath.jsonpath(DocInfoRespBody, cfg.compResIdJsonPath.format(str(doctorId)))
            if tempResIds:
                data.append({doctorId: tempResIds})

        # for each resource of each doctor do request
        if len(data) > 0:
            for data_dict in data:
                docId, currentDocResIds = list(data_dict.items())[0]
                availableResourceId = str(docId)
                for resId in currentDocResIds:
                    complexResourceId = str(resId)

                    # configure Body class object and send "getAvailableResourceScheduleInfo" request
                    availableResInfoBodyObj.id = get_uuid()
                    availableResInfoBodyObj.params["availableResourceId"] = availableResourceId
                    availableResInfoBodyObj.params["complexResourceId"] = complexResourceId
                    availableResInfoRespBody = send(availableResInfoBodyObj.to_json()).json()
                    logger.debug(f'Response body = {availableResInfoRespBody}')

                    # parsing response body
                    startTime = str(jsonpath.jsonpath(availableResInfoRespBody, cfg.startTimeJsonPath)[0])
                    endTime = str(jsonpath.jsonpath(availableResInfoRespBody, cfg.endTimeJsonPath)[0])

                    # configure Body class object and send "createAppointment" request
                    createAppointmentBodyObj.id = get_uuid()
                    createAppointmentBodyObj.params["availableResourceId"] = availableResourceId
                    createAppointmentBodyObj.params["complexResourceId"] = complexResourceId
                    createAppointmentBodyObj.params["startTime"] = startTime
                    createAppointmentBodyObj.params["endTime"] = endTime
                    createAppointmentBodyObj.params["receptionTypeId"] = receptionTypeId
                    createAppointmentRespBody = send(createAppointmentBodyObj.to_json()).json()
                    logger.debug(f'Response body = {createAppointmentRespBody}')

                    appointmentId = str(jsonpath.jsonpath(createAppointmentRespBody, cfg.appointmentIdJsonPath))
                    if appointmentId:
                        return

        time.sleep(cfg.delay_sec)


if __name__ == "__main__":
    reserve_any()

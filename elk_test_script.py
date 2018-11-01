import random
import time

while (1):
    lpu_code = [47002, 47003, 47004]
    ID_messge = random.randint(454, 999)
    numberOfMasstrok = random.randint(0, 1)
    numberOfLpucode = random.randint(0, 2)

    errStr = ''' ID: {}
	Response-Code: 200
	Encoding: UTF-8
	Content-Type: text/xml
	Payload: <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns3:changeSlotStateResponse xmlns:ns3="http://www.hostco.ru/portal" xmlns:ns2="http://www.hostco.ru/portal/types" xmlns="http://www.hostco.ru/types"><lpucode>{}</lpucode><ErrorCode>-1</ErrorCode><ErrorText>Портальный сервис : No records with "timeslotGuid"="636533" was found in table "Op Timeslot"</ErrorText></ns3:changeSlotStateResponse></soap:Body></soap:Envelope>\n'''

    okStr = """ID: {}
	Address: http://192.168.20.104:8080/PortalService/services/portal
	Encoding: UTF-8
	Http-Method: POST
	Content-Type: text/xml; charset=utf-8
	Headers: Accept=[text/xml, multipart/related], connection=[keep-alive], Content-Length=[795], content-type=[text/xml; charset=utf-8], host=[192.168.20.104:8080], SOAPAction=["http://www.hostco.ru/portal/changeSlotState"], user-agent=[JAX-WS RI 2.2.9-b130926.1035 svn-revision#5f6196f2b90e9460065a4c2f4e30e065b245e51e]
	Payload: <?xml version="1.0" ?><S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Header></SOAP-ENV:Header><S:Body xmlns="http://www.hostco.ru/types" xmlns:ns2="http://www.hostco.ru/portal/types" xmlns:ns3="http://www.hostco.ru/portal"><ns3:changeSlotStateRequest xmlns:ns3="http://www.hostco.ru/portal"><slotInfo><GUID>619278</GUID><SlotState>2</SlotState><lpucode>{}</lpucode><patientInfo><Lastname>андреева</Lastname><Firstname>людмила</Firstname><Middlename>геннадиевна</Middlename><birthDate>1971-02-01+03:00</birthDate><SNILS>01223237989</SNILS></patientInfo></slotInfo><status>2</status><slipNumber>2037970</slipNumber><appointmentSource>1</appointmentSource></ns3:changeSlotStateRequest></S:Body></S:Envelope>\n"""

    masStrok = [errStr, okStr]

    f = open('elk-test.log', 'a')  # флаг "a" про дозапись документа -  пишем в конец файла, как  >> в shell
    f.write(masStrok[numberOfMasstrok].format(ID_messge, lpu_code[numberOfLpucode]))
    f.close()
    print("Print messge")
    time.sleep(10)
    print("SLEEEP IS DONE")

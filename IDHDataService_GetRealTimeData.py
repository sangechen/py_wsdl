import zeep

client = zeep.Client('http://10.163.228.141:8103/Emerson/DHDataService?wsdl')
print(client.service.GetRealTimeData(''))

#Param为空字符串：获取所有动环所有设备的实时数据，示例如下：
#   GetRealTimeData (“”)
#Param为局站Id：获取某一局站所有设备的实时数据
#   GetRealTimeData (“10000043”)
#Param为局站Id加设备id：获取某一设备的实时数据
#   GetRealTimeData (“10000002.10000006”)


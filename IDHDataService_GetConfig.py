import zeep

client = zeep.Client('http://10.163.228.141:8103/Emerson/DHDataService?wsdl')
print(client.service.GetConfig(''))

#Param为空字符串：获取所有动环所有配置，示例如下：
#   GetConfig(“”)
#Param为局站Id：获取某一局站的所有配置
#   GetConfig(“10000043”)
#Param为局站Id加设备id：获取某一设备的所有配置
#   GetConfig(“10000002.10000006”)

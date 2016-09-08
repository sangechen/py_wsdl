import zeep

client = zeep.Client('http://10.163.228.141:8103/Emerson/DHDataService?wsdl')
print(client.service.IsRuning())


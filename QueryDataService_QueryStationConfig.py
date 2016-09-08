import zeep

client = zeep.Client('http://localhost:1771/QueryDataService.asmx?wsdl')
print(client.service.QueryStationConfig())


import zeep

client = zeep.Client('http://localhost:1771/QueryDataService.asmx?wsdl')
print(client.service.QueryStationRealData('{"LscID": 2,"StationId": 2}'))


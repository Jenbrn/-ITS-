from employee_dao import Impiegato, EmployeeDao
import json

dao = EmployeeDao()

for imp in dao.findImpiegati():
    print(imp)

#print(json.dumps(dao.findImpiegati()))
print(json.dumps([i.__dict__ for i in dao.findImpiegati()]))
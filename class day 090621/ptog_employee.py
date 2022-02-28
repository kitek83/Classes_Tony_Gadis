import employee

worker1 = employee.Employ('Sara Majewska','478899','bookkeeping','deputy director')
worker2 = employee.Employ('Marek Jankowski','39119','IT','Programmer')
worker3 = employee.Employ('Jan Kowalski','81774','Production','Engineer')

print(worker1.__str__())
print()
print(worker2.__str__())
print(worker3.__str__())
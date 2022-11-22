import datetime

CurrentDate = str(datetime.datetime.now())
CurrentDate = datetime.datetime.strptime(CurrentDate, "%d/%m/%Y")
print(CurrentDate)

ExpectedDate = "9/8/2015"
ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y")
print(ExpectedDate)

if CurrentDate > ExpectedDate:
    print("Date missed")
else:
    print("Date not missed")
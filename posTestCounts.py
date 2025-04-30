#final project
#program for finding covid test counts from csv file

posTests = 0
negTests = 0
totalTests=0
data = open("covidCasesByDate.csv", "r")
data = data.readlines()
data = data[1:]
for line in data:
    parts = line.split(",")
    count = int(parts[1])
    result = parts[2][:1]
    totalTests += count
    if(result=="p"):
        posTests+=count
    else:
        negTests+=count
    
print("Positive: "+str(posTests))
print("Negative: "+str(negTests))
print("Total: "+str(totalTests))


    

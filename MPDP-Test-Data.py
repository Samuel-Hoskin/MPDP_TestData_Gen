import pandas as pd
import requests
import random


df = pd.DataFrame()
numParticipants = 10
# max years is 5
numYears = 5

apiName = "https://random-data-api.com/api/v2/users"
apiPostCode = "https://api.postcodes.io/random/postcodes"

activity_level=""

print("Generating sample data in CSV & SQL insert file")
for x in range(numParticipants):
    print("*",end="")
    nameQuery = requests.get(apiName)
    postCodeQuery = requests.get(apiPostCode)

    firstNameResult = nameQuery.json()['first_name']
    lastNameResult = nameQuery.json()['last_name']
    nameResult = firstNameResult + " " + lastNameResult
    nameResult = nameResult.replace("\'","''")

    postCodeResult = postCodeQuery.json()['result']

    town = str(postCodeResult['parish'])
    town = town.replace("\'","''")
    parliamentary_constituency = str(postCodeResult['parliamentary_constituency'])
    admin_county = str(postCodeResult['admin_county'])
    outcode = str(postCodeResult['outcode'])

    numFYears = (random.randint(1,numYears)-1)
    numSchemes = random.randint(1,6)
    for x in range(numFYears):
        financial_year = ""
        if x == 0:
            financial_year = "21/22"
        if x == 1:
            financial_year = "22/23"
        if x == 2:
            financial_year = "23/24"
        if x == 3:
            financial_year = "24/25"
        if x == 4:
            financial_year = "25/26"    
        for x in range(numSchemes):
            schemes = random.randint(1,16)
            if schemes == 1:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Pilot Participation Payment"
                amount = 1250
            if schemes == 2:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Arable and Horticultural Land"
                amount = random.randint(1250,5000)
            if schemes == 3:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Arable and Horticultural Soils"
                amount = random.randint(1250,5000)
            if schemes == 4:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Hedgerow"
                amount = random.randint(1250,5000)
            if schemes == 5:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Improved Grassland"
                amount = random.randint(1250,5000)  
            if schemes == 6:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "On farm woodland"
                amount = random.randint(1250,5000)   
            if schemes == 7:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Low and no input Grassland"
                amount = random.randint(1250,5000)     
            if schemes == 8:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Waterbody Buffering"
                amount = random.randint(1250,5000)     
            if schemes == 9:
                scheme = "Sustainable Farming Incentive Pilot"
                scheme_detail = "Improved Grassland soils"
                amount = random.randint(1250,5000)     
            if schemes == 10:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "Horticulture"
                amount = random.randint(1250,5000)     
            if schemes == 11:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "Forestry"
                amount = random.randint(1250,5000)     
            if schemes == 12:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "Resource Management"
                amount = random.randint(1250,5000)     
            if schemes == 13:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "Precision and Analysis"
                amount = random.randint(1250,5000)     
            if schemes == 14:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "Livestock Handling and weighing equipment"
                amount = random.randint(1250,5000)     
            if schemes == 15:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "Other Livestock equipment"
                amount = random.randint(1250,5000)     
            if schemes == 16:
                scheme = "Farming Equipment and Technology Fund"
                scheme_detail = "General"
                amount = random.randint(1250,5000)
            new_row = {'payee_name': nameResult, 'part_postcode': outcode, 'town': town, 'county_council': admin_county, 'parliamentary_constituency': parliamentary_constituency, 'scheme': scheme, 'scheme_detail': scheme_detail, 'activity_level': activity_level, 'financial_year': financial_year, 'amount': amount}
            df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)

df.to_csv('testData.csv', index=False)
start = 'INSERT INTO '+'public."payment_activity_data"'+' ('+ str(', '.join(df.columns))+ ') VALUES '
value = ""
for index, row in df.iterrows():       
        values = str(tuple(row.values)) + "," + '\n'
        value = value + values
value = value[:-1]
value = value[:-1]
value = value + ";"
value = value.replace("\"","'")
sqlScript = start + value

with open('sqlScript.sql', 'w') as f:
    f.write(sqlScript)

print("\nSample data generation complete")
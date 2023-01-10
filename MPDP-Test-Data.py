
import pandas as pd
import requests
import random

df = pd.DataFrame()
numParticipants = 255

apiName = "https://random-data-api.com/api/v2/users"
apiPostCode = "https://api.postcodes.io/random/postcodes"

for x in range(numParticipants):

    nameQuery = requests.get(apiName)
    postCodeQuery = requests.get(apiPostCode)

    firstNameResult = nameQuery.json()['first_name']
    lastNameResult = nameQuery.json()['last_name']
    nameResult = firstNameResult + " " + lastNameResult


    postCodeResult = postCodeQuery.json()['result']

    town = postCodeResult['parish']
    parliamentary_constituency = postCodeResult['parliamentary_constituency']
    admin_county = postCodeResult['admin_county']
    outcode = postCodeResult['outcode']

    numSchemes = random.randint(1,6)

    for x in range(numSchemes):
        schemes = random.randint(1,16)
        if schemes == 1:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Pilot Participation Payment"
            amount = 1250
        if schemes == 2:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Arable and Horticultural Land"
            amount = random.randint(1250,5000)
        if schemes == 3:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Arable and Horticultural Soils"
            amount = random.randint(1250,5000)
        if schemes == 4:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Hedgerow"
            amount = random.randint(1250,5000)
        if schemes == 5:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Improved Grassland"
            amount = random.randint(1250,5000)  
        if schemes == 6:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "On farm woodland"
            amount = random.randint(1250,5000)   
        if schemes == 7:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Low and no input Grassland"
            amount = random.randint(1250,5000)     
        if schemes == 8:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Waterbody Buffering"
            amount = random.randint(1250,5000)     
        if schemes == 9:
            scheme = "Sustainable Farming Incentive Pilot"
            activity_detail = "Improved Grassland soils"
            amount = random.randint(1250,5000)     
        if schemes == 10:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "Horticulture"
            amount = random.randint(1250,5000)     
        if schemes == 11:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "Forestry"
            amount = random.randint(1250,5000)     
        if schemes == 12:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "Resource Management"
            amount = random.randint(1250,5000)     
        if schemes == 13:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "Precision and Analysis"
            amount = random.randint(1250,5000)     
        if schemes == 14:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "Livestock Handling and weighing equipment"
            amount = random.randint(1250,5000)     
        if schemes == 15:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "Other Livestock equipment"
            amount = random.randint(1250,5000)     
        if schemes == 16:
            scheme = "Farming Equipment and Technology Fund"
            activity_detail = "General"
            amount = random.randint(1250,5000)
        df = df.append({'payee_name':nameResult, 'part_postcode':outcode, 'town':town, 'county_council':admin_county, 'parliamentary_constituency':parliamentary_constituency, 'scheme':scheme, 'scheme_detail':activity_detail, 'amount':amount}, ignore_index=True)

df.to_csv('testData.csv', index=False)

start = 'INSERT INTO '+'public."payment_activity_data"'+' ('+ str(', '.join(df.columns))+ ') VALUES '
value = ""
for index, row in df.iterrows():       
        values = str(tuple(row.values)) + "," + '\n'
        value = value + values
value = value[:-1]
value = value[:-1]
value = value + ";"
sqlScript = start + value


with open('sqlScript.sql', 'w') as f:
    f.write(sqlScript)





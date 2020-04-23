import requests
import pprint,json


def getDeathnewapi(ccode):
    url="https://api.covid19api.com/total/dayone/country/"+str(ccode)+"/status/confirmed"
    resp=requests.get(url).json()
    dates=[]
    confirmed=[]
    for x in resp:
        d= x["Date"]
        c= x["Cases"]
        dates.append(d[0:10])
        confirmed.append(c)
    dc=dict(zip(dates,confirmed))
    #print(dates)
    #print(confirmed)
    return dc

def pieDetails(ccode):
    url = "https://covid-19-data.p.rapidapi.com/country"
    
    if ccode=="united-kingdom":
        ccode="uk"
    elif ccode=="united-states":
        ccode="USA"

    querystring = {"format":"json","name":str(ccode)}

    headers = {'x-rapidapi-host': "covid-19-data.p.rapidapi.com",'x-rapidapi-key': "377af2c941msh5d768188774c56ap124f9cjsnb9ea50b8b9e1"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    resp=json.loads(response.text)
    confirmed=int(resp[0]['confirmed'])
    deaths=int(resp[0]['deaths'])
    recovered=int(resp[0]['recovered'])
    active=(confirmed-deaths)-recovered
    labels = ['Active','Death','Recovered']
    values =[active,deaths,recovered]
    return labels,values
import requests

def lambda_handler(event, context):

    url = "https://latest-stock-price.p.rapidapi.com/price"

    querystring = {"Indices":"NIFTY 100"}

    headers = {
    	"X-RapidAPI-Key": "fed62b8ef4mshbafa40f0a6f3ea7p1c0c9cjsn570332e03248",
    	"X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    
    return {
    	'statusCode' : 200,
    	'body' : response.json()
    }
import json

def lambda_handler(event, context):
    # TODO implement
    #1 Get the bucketname
    bucket=event['Records'][0]['s3']['bucket']['name']

    #2 Get the file/key name
    key=urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding='utf-8')
     
    try:
        #3-fetch teh file from s3
        response=s3.get_object(Bucket=bucket,Key=key)

        #4 -Deserialize the file's content
        text=response['Body'].read().decode()
        data=json.loads(text)

        #5 -Print the context 
        print(data)

        #6-parse and print the transactions
        transactions=data['transactions']
        for record in transactions:
            print(record['transType'])
        return 'Success!'

    except Exception as e :
        print(e)
        raise e 

        




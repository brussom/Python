<<<<<<< HEAD

import boto3

if __name__ == "__main__":
    fileName='ddn-15-krenko-mob-boss.jpg'
    bucket='pythonmtgcards'
    
    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})
                        
    textDetections=response['TextDetections']
    print ('Detected text')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
=======

import boto3

if __name__ == "__main__":
    fileName='ddn-15-krenko-mob-boss.jpg'
    bucket='pythonmtgcards'
    
    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})
                        
    textDetections=response['TextDetections']
    print ('Detected text')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
>>>>>>> 16e93d9beb5cb02bc019b91a7d5777294b6ab9e8
            print
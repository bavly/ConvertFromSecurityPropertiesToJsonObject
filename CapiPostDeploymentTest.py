#!/usr/bin/python
import time
import hashlib
import hmac
import base64
import requests
import sys

def currentTime():
    currentTimeInMs = int(time.time()*1000.0 /1000.0)
    currentTime = str(currentTimeInMs)
    #print (currentTime);
    return currentTime

def authorization(publickeys,privateKeys):
  
    currentTimes = currentTime()
    toHash = str.format( str(currentTimes) + ":" + str(publickeys) );
    message = bytes(toHash , 'utf-8')
    secret = bytes(privateKeys, 'utf-8')
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    #did some manipulation to string removed first 2 charachters like "b'" then at last remove charachter "'""
    authorizationResult = str(signature)[2:-1]
    return authorizationResult


def putRequest(keyPublic, keyPrivate , url):

    currentTimeInMs = currentTime()
    authentication = authorization(keyPublic, keyPrivate)
    header = {'Content-Type' : 'application/json' , 'X-GO-CLIENT'  : keyPublic , 
              'Authorization': authentication , 'X-GO-DATE' : currentTimeInMs }
    #url = 'http://stgcapi01.corporate.intra:8083/actuator/utility/refreshPageEntitySet'
    response = requests.put(url , headers=header )
    print("Response body of the request is : " + response.text)
    print("Response Status Code of the request is : " + str(response.status_code) )
    return response.text


#authorization()
if len (sys.argv) != 4 :
    # reminder that 0 is the application name so that we need to check the lenght of size 4
    print (" Please check agian Publickey , privatekey , URL is messing")
    sys.exit (1)

#print (str(sys.argv[1]))
#print (str(sys.argv[2]))
#print (str(sys.argv[3]))

putRequest(str(sys.argv[1]) , str(sys.argv[2]) , str(sys.argv[3]))

#python CapiPostDeploymentTest.py go UFLEUUPYWSKLROCFXNKDPYWFZMTYPKIU http://stgcapi01.corporate.intra:8083/actuator/utility/refreshPageEntitySet
#python CapiPostDeploymentTest.py go UFLEUUPYWSKLROCFXNKDPYWFZMTYPKIU http://stgcapi02.corporate.intra:8083/actuator/utility/refreshPageEntitySet
#python CapiPostDeploymentTest.py go CXYMWRQVFUXQOYDBNREQEIAPYSKFMWRK http://corpweb06.corporate.intra:8083/actuator/utility/refreshPageEntitySet
#python CapiPostDeploymentTest.py go CXYMWRQVFUXQOYDBNREQEIAPYSKFMWRK http://corpweb07.corporate.intra:8083/actuator/utility/refreshPageEntitySet

import requests

from stdqdrantendpoint import collections_api_endpoint

class Collection:
    def __init__(self,size,distance):
        self.size = size
        self.distance = distance

    def create(self,host,name_collection,apikey):
        
        data_create = {"vectors":{"size":int(self.size),"distance":self.distance}}
        
        if apikey == None:            
            requests.put(host+"/"+name_collection,data_create,headers={"Content-Type":"application/json"})
        else:
            requests.put(host+"/"+name_collection,data_create,headers={"Content-Type":"application/json","api-key":apikey})    

    def delete(self,host,name_collection,apikey):
        
        if apikey == None:            
            requests.delete(host+"/"+name_collection)
        else:
            requests.put(host+name_collection,headers={"Content-Type":"application/json","api-key":apikey})  

    def list(self,host,apikey):
        
        if apikey == None:            
            requests.get(host+collections_api_endpoint)
        else:
            requests.put(host+collections_api_endpoint,headers={"Content-Type":"application/json","api-key":apikey})   

    def get_collection_details(self,host,apikey,collection_name):
        
        if apikey == None:            
            requests.get(host+collections_api_endpoint+"/"+collection_name)
        else:
            requests.put(host+collections_api_endpoint+"/"+collection_name,headers={"Content-Type":"application/json","api-key":apikey})                      
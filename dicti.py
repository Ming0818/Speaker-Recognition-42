import json

def signup(un,ps):
    with open('data.json','r') as fp:
        data=json.load(fp)
    data[un]=ps
    with open('data.json','w') as fp:
        json.dump(data,fp)
  
def signin(un,ps):
    with open('data.json','r') as fp:
        data=json.load(fp)
    x=data.get(un,"Sorry")
    if x==ps:
        return "PASS"
    else:
        return "Sorry"
    
signup("aaa","aaa")
#z=signin("abhinav006","abhay")
#print(z)
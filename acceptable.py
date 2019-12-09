import requests
import json
class TaoBao:
    lastpage=1
url="https://rate.tmall.com/list_detail_rate.htm"
header={"cookie":"cna=eGXNFRhRSkkCAbfhJLKH8aWp; _m_h5_tk=7d827b7269161b2bec1e75221f12e13b_1565891528974; _m_h5_tk_enc=7a2b5c3133447a619a160b42f8bb9335; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTaHoqcxosmvA%3D%3D; uc3=nk2=1DsN4FjjwTp04g%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UondHPobpDVKHQ%3D%3D&vt3=F8dBy3K1GcD57BN%2BveY%3D; t=8d194ab804c361a3bb214233ceb1815c; tracknick=%5Cu4F0F%5Cu6625%5Cu7EA22013; lid=%E4%BC%8F%E6%98%A5%E7%BA%A22013; uc4=nk4=0%401up5I07xsWKbOPxFt%2Bwto8Y%2BdFcW&id4=0%40UOE3EhLY%2FlTwLmADBuTc%2BcF%2B4cKo; lgc=%5Cu4F0F%5Cu6625%5Cu7EA22013; enc=JY20EEjZ0Q4Aw%2BRncd1lfanpSZcoRHGHdAZmqrLUca8sEI9ku3vIBCYdT4Lvd9KJMVpk%2F1TnijPlCpUrJ2ncRQ%3D%3D; _tb_token_=553316e3ee5b5; cookie2=17126dd7c1288f31dc73b09697777108; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=cBj2amlRqUrFkhhjBOfgZuI8as7O6CvWGsPzw4_GjICP9H5cIxnlWZeaTSLkCnGVL6Dyr3RhSKO4B8YZjPathZXRFJXn9MpO.; isg=BBMTUm-GSmBFQQYmiWpbMPIdtpf9YKfi0yhVD8U0EzPgRD_mR5uf2DzSfvSPZP-C",
"referer":"https://detail.tmall.com/item.htm",
"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.37"}
params={"itemId":"0","sellerId":"2616970884","currentPage":"1","orther":"1","callback":"jsonp2359"}
def __int__(self,id:str):
    self.params['itemId']=id
def getPageData(self,pageIndex:int):
    self.params["currentPage"]=str(pageIndex)
    req=requests.get(self.url,self.params,headers=self.header,timeout = 2).content.decode('utf-8')
    req=req[req.find('{'):req.rfind('}')+1]
    return json.loads(req)
def setOrder(self,way:int):
    self.params["order"]=way;
def getAllData(self):
    Data=self.getPageData(1)
    self.lastPage= Data['rateDetail']['paginator']['lastPage']
    for i in range(2,self.lastPage+1):
        Data['rateDetail']['rateList'].extend(self.getPageData(i)['rateDetail']['rateList'])
    taobao=TaoBao("555082135230")
    k=taobao.getPageData(1)
    print(k)
   

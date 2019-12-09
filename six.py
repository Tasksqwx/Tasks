import requests
import json
url="https://rate.tmall.com/list_detail_rate.htm"
header={"cookie":"cna=EYnEFeatJWUCAbfhIw4Sd0GO; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTaHYecARKhrA%3D%3D; uc3=vt3=F8dBy32hRyZzP%2FF7mzQ%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&nk2=1DsN4FjjwTp04g%3D%3D&id2=UondHPobpDVKHQ%3D%3D; t=ad1fbf51ece233cf3cf73d97af1b6a71; tracknick=%5Cu4F0F%5Cu6625%5Cu7EA22013; lid=%E4%BC%8F%E6%98%A5%E7%BA%A22013; uc4=nk4=0%401up5I07xsWKbOPxFt%2BwuLaZ8XIpO&id4=0%40UOE3EhLY%2FlTwLmADBuTfmfBbGpHG; lgc=%5Cu4F0F%5Cu6625%5Cu7EA22013; enc=ieSqdE6T%2Fa5hYS%2FmKINH0mnUFINK5Fm1ZKC0431E%2BTA9eVjdMzX9GriCY%2FI2HzyyntvFQt66JXyZslcaz0kXgg%3D%3D; _tb_token_=536fb5e55481b; cookie2=157aab0a58189205dd5030a17d89ad52; _m_h5_tk=150df19a222f0e9b600697737515f233_1565931936244; _m_h5_tk_enc=909fba72db21ef8ca51c389f65d5446c; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=cBa4gFrRqYHNUtVvBOfiquI8a17O4IJ51sPzw4_G2ICP9B5DeMDOWZezto8kCnGVL6mpR3RhSKO4BYTKIPaTlZXRFJXn9MpO.; isg=BI6ORhr9X6-NrOuY33d_XmZFy2SQp1Ju1qe4XLjXJRHsGyp1IJ9IG0kdUwfSA0oh",
"referer":"https://detail.tmall.com/item.htm",
"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36"}
params={"itemId":"596285864342","sellerId":"2616970884","currentPage":"1","orther":"1","callback":"jsonp2359",}
req=requests.get(url,params,headers=header).content.decode('utf-8')[12:-1];
result=json.loads(req);
print(result)

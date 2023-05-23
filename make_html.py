import sqlite3
import numpy as np

print('starting..')
cnn = None


try:
    cnn = sqlite3.connect('merito.db')
    print('database connected..')
    sql = (" Select Title, Company, Link,Mode,Experience,Location"
           " From jobs"
           )
    cs = cnn.cursor()
    cs.execute(sql)
    rst = cs.fetchall()
    print('records selected..')
    html = "<html><title>Output</title><body><table >"
    for row in rst:
        html+="<tr><td>Title</td>"
        html+="<td>Company</td><td>Link</td><td>Mode</td><td>Experience</td><td>Location</td></tr>"
        html += "<tr><td>"+row[0] +"</td>"+"<td>"+row[1] +"</td>"+"<td>"+row[2] +"</td><td>"+row[3] +"</td>"+"<td>"+row[4] +"</td>"+"<td>"+row[5] +"</td>"
        html += "</tr>"
    html += "</table></body></html>"
    file = open("my_html.html", "w")
    file.write(html)
    file.close()
# except Error as e:
#     print(e)
finally:
    if cnn:
        cnn.close()
print('done.')
    

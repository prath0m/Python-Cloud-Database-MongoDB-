
import pymysql
conn = pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')

curs=conn.cursor()

curs.execute("select * from accounts")
data=curs.fetchmany(5) # fetch as a number passed 
print(data)
conn.close()

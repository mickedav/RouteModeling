import dbUtil
import googleRoutes

#Connect to DB
user = 'mms'
password = '001'
#user = input('User: ')
#password = input('Password: ')
user = "'" + user + "'"
password = "'" + password + "'"

cur = dbUtil.dbConnect("'mode'", user, password)

#Fetch data from db
time_periods = dbUtil.getTimePeriods(cur)
node_list = dbUtil.getNodeList(cur)
od_list = dbUtil.getOdList(cur)

#Start collecting routes from Google
time_period = 1

routes = googleRoutes.getGoogleRoutes(od_list, node_list, time_period)

print(routes)

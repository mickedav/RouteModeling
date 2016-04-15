import time
import dbUtil
import sys
#import os

#os.system('export DYLD_FALLBACK_LIBRARY_PATH=/Library/PostgreSQL/9.5/lib:$DYLD_FALLBACK_LIBRARY_PATH')


user = "'" + user + "'"
password = "'" + password + "'"

[cur, conn] = dbUtil.dbConnect("'mode'", user, password)

distinct_routes = dbUtil.getDistinctSteps(cur, conn)

lines = []
start_time = time.time()
counter = 0

print('Createing: ', len(distinct_routes), ' unique steps')
for index, route in enumerate(distinct_routes):

    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:
        sys.stdout.write("\r%d%%" % ((counter/len(distinct_routes)*100)))
        sys.stdout.flush()

    start = route[0]
    end = route[1]
    start_wkt = route[2]
    end_wkt = route[3]

    start_node = dbUtil.getClosestSource(cur, conn, start)
    end_node = dbUtil.getClosestSource(cur, conn, end)
    lines.append((index, start_node[0][0], start_node[0][1], end_node[0][0], end_node[0][1], start_wkt, end_wkt))
    counter = counter + 1

dbUtil.storeUniqueSteps(cur, conn, lines)
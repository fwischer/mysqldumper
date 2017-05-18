#!/usr/bin/env python

import subprocess
import datetime


class SqlExport:
    dumpDir = ''
    filename = ''

    def __init__(self, dump_dir, filename):
        self.dumpDir = dump_dir
        self.filename = filename

    def dump_sql(self, hour):
        thetime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        if datetime.time(hour):
            subprocess.call(
                "mysqldump -h localhost -uroot -ppassword > " + self.dumpDir +"" + self.filename + "" + thetime + ".sql",
                shell=True)
            subprocess.call("gzip " + self.dumpDir + "" + self.filename + "" + thetime + ".sql", shell=True)


sqlexport = SqlExport('/Users/fwischer/Download/dump/', 'baufuchs_db_', )
sqlexport.dump_sql(12)

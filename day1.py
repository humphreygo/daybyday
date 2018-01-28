#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:55:39 2018

@author: pi
"""

#day 1

import os
import logging
logging.basicConfig(level = logging.info)

from datetime import datetime

#当前目录
path = os.path.dirname(__file__)
db_file = 'db.txt'
db_path = os.path.join(path,db_file)

if not os.path.exists(db_path):
    file = open(db_path, 'w')
    file.write('日期    姓名    金额\n')
    file.close()
    
with open(db_path, 'a') as f:
    logging.info('write ok')
    f.write('dkfjdsalfjdalsf' + '\n')

dateinput = (input(r'input you date:'))
logging.info(dateinput)
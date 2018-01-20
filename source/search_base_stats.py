# -*- coding: utf-8 -*-
import sys

ld = open("../config/base_stats.conf")
lines = ld.readlines()
ld.close()

print "No.,ポケモン名,HP,攻撃,防御,特攻,特防,素早,合計"
for arg in sys.argv:
  for line in lines:
    if line.find(arg) >= 0:
      print line[:-1]

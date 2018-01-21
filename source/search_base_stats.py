# -*- coding: utf-8 -*-
import os
import sys

def main():
  source_file_path = os.path.dirname(os.path.abspath(__file__))
  config_file_path = os.path.normpath(os.path.join(source_file_path, '../config/base_stats.conf'))

  ld = open(config_file_path)
  lines = ld.readlines()
  ld.close()

  print "No.,ポケモン名,HP,攻撃,防御,特攻,特防,素早,合計"

  for arg in sys.argv:
    for line in lines:
      if arg in line:
        print line[:-1]

if __name__ == '__main__':
  main()

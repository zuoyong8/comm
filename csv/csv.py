# -*- coding:utf-8 -*-
import csv
import os
import sys

MAIL_SUFFIX = {"bccto.me":1,
				"bccto.me":2,
				"www.bccto.me":3,
				"4057.com":4,
				"dawin.com":5,
				"chaichuang.com":6,
				"oiizz.com":7,
				"vedmail.com":8,
				"3202.com":9,
				"sltmail.com":10,
				"819110.com":11,
				"wca.cn.com":12,
				"cr219.com":13,
				"jnpayy.com":14,
				"yidaiyiluwang.com":15,
				"a7996.com":16, 
				"jiaxin8736.com":17,
				"gbf48123.com":18,
				"juyouxi.com":19
				}


def csv_find_files():
	all = os.listdir(".")
	files = []
	for a in all:
		if a.find(".csv")>=0:
			files.append("./"+a)
	return files

def csv_write_files(read_files):
	wfiles = []
	for r in read_files:
		i = r.find(".csv")
		wfiles.append(r[:i] + "_update.csv")
	return wfiles

def csv_operation(read_files,write_files):
	count = 0 
	for index,rf in enumerate(read_files):
		csv_rf = open(rf,"r")
		csv_wf = open(write_files[index],"w",newline = "")
		csv_reader = csv.reader(csv_rf)
		csv_writer = csv.writer(csv_wf)
		csv_writer.writerow(["序号","邮箱账号","购买BNC的数量","换算成ENC的数量"])
		for item in csv_reader:
			ss = item[1].split('@')
			if len(ss) == 2:
				try:
					if MAIL_SUFFIX[ss[1]] >0:
						count = count + 1
				except:
					csv_writer.writerow(item)
	return count

def csv_check_invalid(read_files):
	count = 0 
	for rf in read_files:
		csv_rf = open(rf,"r")
		csv_reader = csv.reader(csv_rf)
		for item in csv_reader:
			ss = item[1].split('@')
			if len(ss) == 2:
				try:
					if MAIL_SUFFIX[ss[1]] >0:
						count = count+1
				except:
					pass
	return count



if __name__ == "__main__":
	cff = csv_find_files()
	# print(csv_operation(fs,csv_write_files(fs)))
	print(csv_check_invalid(cff))
	# print(fs)

# -*- coding:utf-8 -*-

import sys
import os

'''
    对比花名册中的学号和指定文件夹下的文件名中的学号判断未交作业名单
'''

'''
    花名册文件内容格式：
'''
'''
张三,2017007700
李四,2017007701
王五,2017007702
'''

'''
	静态文件
'''
staticRoster = {
	# 学号：姓名
	'2017007700': '王浩',
	'2017007701': '王浩'
}

# 读花名册文件
def readRoster(filename):
	f = open(filename, 'r', encoding='utf-8')
	roster = {}
	line = f.readline()
	while line:
		line = line.split(',')
		line[1] = line[1][0:10]
		roster[line[1]] = line[0]
		line = f.readline()
	f.close()
	return roster

# 对比花名册与文件夹下文件列表
def diff(idRosker, files):
	fileRoster = []
	for f in files:
		try:
			idIndex = f.index('2017')
		except:
			continue
		fileRoster.append(f[idIndex:idIndex+10])
	return list(set(idRosker).difference(set(fileRoster)))

# 程序执行
if __name__ == '__main__':
	argvs = sys.argv
	if argvs[1] == 'help':
		print()
		print('帮助：')
		print('    使用示例： python3 whoNotSubmit.py  rosterFilePath  homeworkFolderPath')
		print('        参数1： 花名册文件路径，花名册文件内容格式：')
		print()
		print('            2017007700,王浩')
		print('            2017007700,王浩')
		print('            2017007700,王浩')
		print('              ..........')
		print()
		print('        参数2：存放作业的文件夹路径')
		print()
		os._exit(1)
	if len(argvs) == 2:
		roster = staticRoster
		filePath = argvs[1]
	elif len(argvs) == 3:
		rosterFileName = argvs[1]
		filePath = argvs[2]
		try:
			roster = readRoster(rosterFileName)
		except FileNotFoundError:
			print('Fail: 花名册文件没找到！')
			os._exit(1)
	else:
		print('Fail: 参数错误；示例： python3 whoNotSubmit.py  rosterFilePath  homeworkFolderPath')
		os._exit(1)

	# 查找文件夹
	try:
		files = os.listdir(filePath)
	except FileNotFoundError:
		print('Fail: 存作业的文件夹没找到！')
		os._exit(1)
	# 没交作业名单
	idRoster = roster.keys()
	notSubmits = diff(idRoster, files)
	notSubmits.sort()
	# 打印结果
	print('   # \t学号\t姓名\n')
	for i in range(len(notSubmits)):
		print('-> {}:\t{}\t{}'.format(i+1, notSubmits[i], roster[notSubmits[i]]))
	print('\n未交作业人数： {}'.format(len(notSubmits)))

	
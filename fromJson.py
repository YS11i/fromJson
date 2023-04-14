import json
import requests
import jsonpath
import argparse
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -u/-f url/file -p param -o result.txt")
    parser.add_argument("-u", "--url", help="json url")
    parser.add_argument("-p", "--param", help="find param")
    parser.add_argument("-f", "--file", help="local file")
    parser.add_argument("-o", "--output", help="output result")
    parser.add_argument("-k", "--key", help="getkeys input 1")


    return parser.parse_args()

def fromHttp(url,findStr):
	status = True
	resStr = []

	MyUa = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
	try:
		headers = {'User-Agent': MyUa,'Connection': 'close'}
		r = requests.get(url=url, verify=False, headers=headers, timeout=10)
	except:
		print("Connect Error!")
		status = False
		return status


	try:
		jsonData = json.loads(r.text)
		#print(jsonData,type(jsonData))

	except Exception as e:
		print(e)
		status = False
		return status

	
	resStr = jsonpath.jsonpath(jsonData, "$..{}".format(findStr))
	if resStr == False:
		print("Can't find this node!")
		status = False
		return status
	else:
		return resStr

def fromFile(path,findStr):
	status = False
	resStr = []
	file_json = None

	try:
		with open(path,'r',encoding="utf-8") as jsonFile:
			jsonFile = jsonFile.read().replace("\n","").replace("\t","").strip() #不要获取每行输入
			file_json = json.loads(jsonFile)
			#print(jsonFile)
	except:
		print("Can't open local file!")

	resStr = jsonpath.jsonpath(file_json, "$..{}".format(findStr))
	return resStr
	
def outputRes(resStr,fileName):

	with open('{}'.format(fileName),'w',newline='') as csvf:
		#print(resStr)
		for line in resStr:
			line = str(line)
			line = line + '\n'
			csvf.writelines(line)
			#print(line)
		csvf.close()






if __name__ == '__main__':
	args = parse_args()
	path = None
	url = None
	findStr = None
	fileName = None
	key = None

	path = args.file
	url = args.url
	findStr = args.param
	fileName = args.output
	key = args.key

	if path == None and url == None and fileName == None:
	    print('\tExample: \r\npython3 ' + sys.argv[0] + " -u/-f url/file -p param")
	    exit()

	if url == None and path != None and findStr != None:
		resStr = fromFile(path,findStr)
		if fileName != None:
			outputRes(resStr,fileName)		
		#print(resStr)
		for i in resStr:
			if isinstance(i,dict):
				if key != None:
					#print(list(i.keys()))
					for j in list(i.keys()): #获取非末端节点的key值
						print(j)
					#exit()
				print(i)
			elif isinstance(i,int) or isinstance(i,float) or isinstance(i,complex) or isinstance(i,str):
				print(i)
			elif isinstance(i,list):
				for j in i:
					print(j)



			
	elif url != None and path == None and findStr != None:
		resStr = fromHttp(url,findStr)
		if fileName != None:
			outputRes(resStr,fileName)		
		#print(resStr)
		for i in resStr:
			if isinstance(i,list) or isinstance(i,dict):
				if key != None :
					#print(list(i.keys()))
					for j in list(i.keys()): #获取非末端节点的key值
						print(j)
					exit()
				print(i)
			elif isinstance(i,int) or isinstance(i,float) or isinstance(i,complex) or isinstance(i,str):
				print(i)

			elif isinstance(i,list):
				for j in i:
					print(j)			

	else:
		print("输入参数异常...")
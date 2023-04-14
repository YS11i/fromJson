# fromJson

从指定json文件（远程获取或者本地json文件）中查找指定节点
```
usage: fromJson.py [-h] [-u URL] [-p PARAM] [-f FILE] [-o OUTPUT] [-k KEY]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     json url
  -p PARAM, --param PARAM
                        find param
  -f FILE, --file FILE  local file
  -o OUTPUT, --output OUTPUT
                        output result
  -k KEY, --key KEY     getkeys input 1

Example: python3 .\fromJson.py -u/-f url/file -p param -o result.txt
```
查找非末端节点会返回对应key的字典，使用-k 1参数获取对应字典的key

查找末端节点会返回对应key的value



-k参数筛选key
查找的参数中不能出现`.`目前还没有好的解决方法--

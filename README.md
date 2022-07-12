# fromJson

从指定json文件（远程获取或者本地json文件）中查找指定节点
```
usage: fromJson.py [-h] [-u URL] [-p PARAM] [-f FILE] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     json url
  -p PARAM, --param PARAM
                        find param
  -f FILE, --file FILE  local file
  -o OUTPUT, --output OUTPUT
                        output result

Example: python3 .\fromJson.py -u/-f url/file -p param -o result.txt
```

查找的参数中不能出现`.`目前还没有好的解决方法--

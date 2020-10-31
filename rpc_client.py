from xmlrpc.client import ServerProxy

if __name__ == '__main__':
    server = ServerProxy("http://localhost:8888") # 初始化服务器
    print (server.get_string("oldboy_python6666")) # 调用函数并传参

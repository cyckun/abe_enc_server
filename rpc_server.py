from xmlrpc.server import SimpleXMLRPCServer

# 调用函数
def respon_string(str):
    return "get string:%s"%str


if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 8888)) # 初始化
    server.register_function(respon_string, "get_string") # 注册函数
    print ("Listening for Client")
    server.serve_forever() # 保持等待调用状态

import socket


def get_ip():
    result = []
    # 获取本机电脑名
    user_name = socket.getfqdn(socket.gethostname())
    result.append(user_name)
    # 获取本机ip 这是内网的ip !!!
    user_ip = socket.gethostbyname(user_name)
    # result[1] = user_ip
    result.append(user_ip)
    return result


#  阿什顿发斯蒂芬
for item in get_ip():
    print(item)

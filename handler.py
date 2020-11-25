#!/bin/env python3

import socket

from minio import Minio
from minio.error import ResponseError

def ping(address,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address, port))
    if result == 0:
        return True
    else:
        return False

def test(address,port,keyId,key):
    minioClient = Minio("%s:%d"%(address,port),
                  access_key=keyId,
                  secret_key=key,
                  secure=False)
    
    try:
        bucket_list = minioClient.list_buckets()
        for bucket in bucket_list:
            print(bucket.name, bucket)
        return True
    except ResponseError as err:
        return False

def main(args):
    addr = args.get("address","127.0.0.1")
    port = args.get("port",9000)
    key =args.get("key","")
    secret = args.get("secret","")
    print("running ping")
    pTest =ping(addr,port)
    print("pinging", pTest)
    print("minio connection test")
    mTest = test(addr,port,key,secret)
    print("minio Test",mTest)
    return {"pTest":pTest,"mTest":mTest}

import sys
import requests
import basicauth
import json
import time
import datetime

#temp
nodeIPs = ['192.168.0.1', '192.168.0.2']
syncGatewayIPs = []
username = "admin"
password = "Hunter01"
errors = []

def main():
    grabstats()


def grabstats():
    #gather node stats and verify them online
    for ip in nodeIPs:
        req = getReq(ip, '8091', '/pools/nodes/')
        print(req['code'])
        if (req['code'] == 200 or req['code'] == 201):
            body = json.loads(req['res'])
            for node in body['nodes']:
                print(node)
        else:
            #Could not reach node, handle, add to list of errors
            print(f'request failed for server {ip}!')


def getReq(ip, port, url):
    try:
        req = requests.get(f'http://{ip}:{port}{url}', auth=(username, password))
        return {"res": req.text, "code": req.status_code}
    except requests.exceptions.RequestException as e:
        print(e)
        return {"res": None, "code": 500}
    #print(req.status_code)


def postReq(ip, port, url, body):
    return


if __name__ == "__main__":
    main()



from time import sleep
import json

from bottle import route, run, template, response

@route('/v1.15/info')
def info():
    return {    "ID": "2OOA:CYFR:DZUF:2WIB:XM46:QSOA:HTKH:2EWV:FV53:FUYY:ZK4J:AAAA",
                "Containers": 0,
                "Images": 0,
                "Driver": "aufs",
                "DriverStatus": [["Root Dir", "/var/lib/docker/aufs"], ["Backing Filesystem", "extfs"], ["Dirs", "895"], ["Dirperm1 Supported", "false"]],
                "MemoryLimit": True,
                "SwapLimit": True,
                "CpuCfsPeriod": True,
                "CpuCfsQuota": True,
                "IPv4Forwarding": True,
                "BridgeNfIptables": True,
                "BridgeNfIp6tables": True,
                "Debug": False,
                "NFd": 24,
                "OomKillDisable": True,
                "NGoroutines": 22,
                "SystemTime": "2015-10-22T14:23:19.52749887-05:00",
                "ExecutionDriver": "native-0.2",
                "LoggingDriver": "json-file",
                "NEventsListener": 1,
                "KernelVersion": "3.13.0-58-generic",
                "OperatingSystem": "Ubuntu 14.04.3 LTS",
                "IndexServerAddress": "https://index.docker.io/v1/",
                "RegistryConfig": {"InsecureRegistryCIDRs": ["127.0.0.0/8"], 
                                   "IndexConfigs": {"docker.io":
                                                        {"Name": "docker.io",
                                                         "Mirrors": None,
                                                         "Secure": True,
                                                         "Official": True
                                                        }
                                                   },
                                   "Mirrors": None},
                "InitSha1": "1f4a3c648015cae3b3d76c5ba2980d8c1f88f388",
                "InitPath": "/usr/lib/docker/dockerinit",
                "NCPU": 22,
                "MemTotal": 22222222,
                "DockerRootDir": "/var/lib/docker",
                "HttpProxy": "",
                "HttpsProxy": "",
                "NoProxy": "",
                "Name": "mock-docker",
                "Labels": ["mock=true"],
                "ExperimentalBuild": False
            }

@route('/v1.15/version')
def version():
    return {   "Version": "1.8.2",
               "ApiVersion": "1.20",
               "GitCommit": "0a8c2e3",
               "GoVersion": "go1.4.2",
               "Os": "linux",
               "Arch": "amd64",
               "KernelVersion": "3.13.0-58-generic",
               "BuildTime": "Thu Sep 10 19:19:00 UTC 2015"
            }
    
@route('/v1.15/containers/json')
def containers():
    response.content_type = 'application/json'
    return "[]"
    
@route('/v1.15/images/json')
def images():
    response.content_type = 'application/json'
    return "[]"
    
@route('/v1.15/volumes')
@route('/v1.15/networks')    
@route('/v1.15/events')
def empty_resp():
    response.content_type = 'application/json'
    return
    
@route('/v1.15/containers/create', method='POST')
def containers_create():
    sleep(2000)
    response.content_type = 'application/json'
    return
    
run(host='localhost', port=8889, debug=True)

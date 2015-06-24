#!/usr/bin/python
import os
import time
import json
import docker
import urllib2

rootdir = '/var/www/html/rune'

files = [
  {'src':'https://raw.githubusercontent.com/JosiahKerley/heimdall/master/rune/src/index.html','dst':rootdir+'/index.html'},
  {'src':'https://raw.githubusercontent.com/JosiahKerley/heimdall/master/rune/src/style.css','dst':rootdir+'/style.css'},
]

## Download file
def download(src,dst):
  response = urllib2.urlopen(src)
  html = response.read()
  with open(dst,'w') as f:
    f.write(html)

## Setup
def setup():
  if not os.path.isdir(rootdir):
    os.makedirs(rootdir)
  for i in files:
    download(i['src'],i['dst'])

## Poll
def poll():
  d = docker.Client(base_url='unix://var/run/docker.sock')
  sites = []
  for container in d.containers(all=True):
    proto = {
      "name":"",
      "icon":"",
      "description":"",
      "url":""
    }
    for i in container['Labels']:
      proto[i] = container['Labels'][i]
    sites.append(proto)
  try:
    with open(rootdir+'/defaults.json', 'r') as f:
      default = json.loads(f.read())
    sites += default
  except:
    pass
  with open(rootdir+'/sites.json', 'w') as f:
    f.write(json.dumps(sites,indent=2))

## Main
setup()
while True:
  poll()
  time.sleep(5)

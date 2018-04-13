#!/bin/bash
docker rm $(docker ps -a -q)
docker image rm -f python:smashbox2
docker build . -t python:smashbox2

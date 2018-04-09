#!/bin/bash
docker run -d  --name $1 -h $1  -v /saida:/saida python:smashbox2

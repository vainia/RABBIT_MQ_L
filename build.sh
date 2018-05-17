#!/usr/bin/env bash
docker build -t rmq-l .
docker run -v /etc/hostname:/srv/hostname -v /tmp:/tmp rmq-l:latest bash

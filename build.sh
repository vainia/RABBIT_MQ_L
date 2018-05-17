#!/usr/bin/env bash
docker build -t rmq-l .
docker run -d rmq-l:latest bash

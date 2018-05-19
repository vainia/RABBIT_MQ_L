# Overview

Main target is to manage tools which helps user to edit strings.
Service replacing chars in text(published into it by JSON message) with defined function in [performer.py](https://github.com/vainia/RABBIT_MQ_H/blob/master/performer.py).

Message must strictly adopted to JSON template:
```
{
   'NAME':'message'
}
```
Where `'NAME'` is static keyword required for micro-service(hereinafter "MS") and ``'message'`` - any string text defined by user.

 As output we got updated JSON with 'o' to 'a' first appeared letter replaced in `'message'` which sends towards to next MS queue.

# Requirements

* `pika==0.11.2` (because we need sometimes to feed our python with small rodents)

Pika has used for supplying pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ’s extensions. That module gives us ability to perform any manipulations with RabbitMQ.

# Run

All commands will be perform in terminal (`docker` must be installed).

First of all you need to raise up RabbitMQ server with command:
```ShellSession
docker run -d --hostname my-rabbit -p 0.0.0.0:5672:5672 -p 0.0.0.0:15672:15672  --name some-rabbit -e RABBITMQ_DEFAULT_USER=user_name -e RABBITMQ_DEFAULT_PASS=user_password rabbitmq:3-management
```

Ports ASMP:`5672` and HTTP:`15672` are defaults for backend(functional) and frontend(web) accordingly.
`0.0.0.0` means that RabbitMQ will listen for all hosts.

If you want to run single MS just run [build.sh](https://github.com/vainia/RABBIT_MQ_H/blob/master/build.sh) placed in primary folder titled with MS name.

# Configuration

File [config.py](https://github.com/vainia/RABBIT_MQ_H/blob/master/config.py) maintain configurations for MS:

```
SET = {
    'port':'5672', #default port
    'server':'0.0.0.0', #rabbit-mq server ip adres
    'name':'user_name', #name required for connection to server
    'passwd':'user_password', #password required for connection to server
    'queue_current':'RMQ-H-E', #name of the current queue, where initial JSON being preserved
    'queue_above':'RMQ-E-L' #name of the next queue, where JSON sends after processing
}
```

Everything above(excluding `queue set` and `server ip`) must be exactly the same as defined in command raising RabbitMQ server.

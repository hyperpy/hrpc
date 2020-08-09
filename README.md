# hrpc

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/hrpc/status.svg)](https://drone.autonomic.zone/hyperpy/hrpc)

## Simple RPC with Protobuf Services

## Install

```sh
$ pip install hrpc
```

## Example

> **TLDR; See the [example](./example/) directory**

Define an RPC service in a `schema.proto`.

```protobuf
syntax = "proto2";

message EchoMsg {
  required string value = 1;
}

service Example {
  rpc Echo (EchoMsg) returns (EchoMsg) {}
}
```

Then generate the services and stubs with `hrpc`.

```sh
$ pip install hrpc
$ hrpc schema.proto
```

This creates `schema_gprc.py` (services) and `schema_pb2.py` (stubs) files.

You can then write a async-ready server and client like so.

```python
# server.py
```

```python
# client.py
```

And run them in separate terminals to see the output.

```
$ python server.py # terminal 1
$ python client.py # terminal 2
```

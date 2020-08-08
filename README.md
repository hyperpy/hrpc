# hrpc

## Simple RPC with Protobuf Services

## Install

```sh
$ pip install hrpc
```

## Example

Define an RPC service in a `schema.proto`.

```protobuf
message Echo {
  required string value = 1;
}

service Example {
  rpc Echo (Echo) returns (Echo) {}
}
```

Then generate the services and stubs with `hrpc`.

```sh
$ pip install hrpc
$ hrpc schema.proto
```

This creates `schema_gprc.py` (services) and `schema_pb2.py` (stubs) files.

You can write a simple server and client like so.

```python
# server.py
```

```python
# client.py
```

Then run them in separate terminals and see the output.

```
$ python server.py # terminal 1
$ python client.py # terminal 2
```

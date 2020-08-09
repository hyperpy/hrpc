# example

## What Is What

- **greeter.proto**: human-written protobuf definition
- **greeter_grpc.py**: machine-generated service code
- **greeter_pb2.py**: machine-generated stub code
- **server.py**: human-written server
- **client.py**: human-written client code

## Run It

```sh
$ pip install hrpc trio
$ python server.py  # terminal 1
$ python client.py  # terminal 2
```

Output:

```
Hello, World
Hello, 0
Hello, 1
Hello, 2
Hello, 3
Hello, 4
```

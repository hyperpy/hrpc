"""Greeter server."""

from greeter_grpc import GreeterServicer
from greeter_pb2 import HelloReply, HelloRequest
from purerpc import Server


class Greeter(GreeterServicer):
    async def SayHello(self, message):
        return HelloReply(message="Hello, " + message.name)

    async def SayHelloToMany(self, input_messages):
        async for message in input_messages:
            yield HelloReply(message=f"Hello, {message.name}")


if __name__ == "__main__":
    server = Server(50055)
    server.add_service(Greeter().service)
    try:
        server.serve(backend="trio")
    except KeyboardInterrupt:
        pass

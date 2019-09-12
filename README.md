# EchoServer

What this is an example of a grpc server that echos what ever message you send it. Even sets up TLS.

# Setting up the environment

```
python -m pip install virtualenv
virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install grpcio
python -m pip install grpcio-tools
```

# Compile gRPC

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. echoserver.proto

# Run server
python echoserver.py

# Call server
python echo.py <message>
example: python echo.py "Hello World"

# To enable SSL
openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

```
Country Name (2 letter code) []:US
State or Province Name (full name) []:WA
Locality Name (eg, city) []:Seattle
Organization Name (eg, company) []:
Organizational Unit Name (eg, section) []:
Common Name (eg, fully qualified host name) []:localhost
Email Address []:
```

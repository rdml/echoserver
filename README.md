# Setting up the environment

python -m pip install virtualenv
virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install grpcio
python -m pip install grpcio-tools

# Compile gRPC

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. echoserver.proto

# Run server
python echoserver.py

# Call server
python echo.py <message>
example: python echo.py "Hello World"

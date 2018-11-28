# Python chat

A client-server multi-user chat application written in Python.

___
## Requirements:
This application uses only built-in Python libraries, namely:
- Socket
- Threading
- Tkinter

___
## Usage
You first need to either describe the desired configurations in a `dev.env` file, or export the values in the environment (you can also keep the default values too).

To run the server part do:
```
make start_server
```
To run the client chat application do:
```
make run
```
___
## Environment variables

The application contains the following environment variables:
- `MAX_CONNECTIONS` - the maximal number of possible connections to the server
- `HOST` and `PORT` define the server host
- `BUFFSIZE` is the maximal buffer size
- `LOG_LEVEL` and `LOG_FORMAT` specify the level and format of the log messages respectively

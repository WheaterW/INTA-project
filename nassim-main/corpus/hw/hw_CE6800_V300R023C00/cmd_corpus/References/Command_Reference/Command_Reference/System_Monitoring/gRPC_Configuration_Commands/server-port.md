server-port
===========

server-port

Function
--------



The **server-port** command configures the number of a port to be listened by gRPC server.

The **undo server-port** command restores the default configuration.



By default, port 57400 is listened by gRPC server.


Format
------

**server-port** *port-number*

**undo server-port** [ *port-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the number of a port to be listened by the gRPC server. | The value is an integer ranging from 10000 to 57999. |



Views
-----

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, you can run the server-port command to configure a server port to be listened. A connection can then be established between the server and client.


Example
-------

# Set the port to be listened by gRPC IPv4 server during Telemetry dynamic subscription to port 20000.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server
[~HUAWEI-grpc-server] server-port 20000

```
idle-timeout
============

idle-timeout

Function
--------



The **idle-timeout** command sets an idle timeout period for the gRPC service.

The **undo idle-timeout** command restores the default configuration.



By default, the idle timeout period of the gRPC service is 10 seconds.


Format
------

**idle-timeout** *time*

**undo idle-timeout** [ *time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies an idle timeout period for the gRPC service. | The value is an integer ranging from 1 to 3600, in seconds. |



Views
-----

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, you can run the idle-timeout command to configure an idle timeout period for the gRPC service. If no RPC connection is established before the idle timeout period expires, the gRPC service is disconnected and waits for the client to connect to the server again.


Example
-------

# Set the idle timeout period of the gRPC service during Telemetry dynamic subscription to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server
[~HUAWEI-grpc-server] idle-timeout 30

```
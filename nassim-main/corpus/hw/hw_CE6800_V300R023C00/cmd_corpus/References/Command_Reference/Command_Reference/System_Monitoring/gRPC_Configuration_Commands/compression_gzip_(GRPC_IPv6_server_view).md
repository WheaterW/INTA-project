compression gzip (GRPC IPv6 server view)
========================================

compression gzip (GRPC IPv6 server view)

Function
--------



The **compression gzip** command configures the gRPC IPv6 server to transmit data in gzip compression mode.

The **undo compression gzip** command restores the default compression mode.



By default, the data transmitted by the gRPC IPv6 server is not compressed.


Format
------

**compression gzip**

**undo compression gzip**


Parameters
----------

None

Views
-----

GRPC IPv6 server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During dynamic telemetry subscription, after this command is run, data is uploaded to the gRPC IPv6 client in compressed mode, saving the upload link bandwidth.


Example
-------

# Set the compression mode of the gRPC IPv6 server to gzip.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server ipv6
[~HUAWEI-grpc-server-ipv6] compression gzip

```
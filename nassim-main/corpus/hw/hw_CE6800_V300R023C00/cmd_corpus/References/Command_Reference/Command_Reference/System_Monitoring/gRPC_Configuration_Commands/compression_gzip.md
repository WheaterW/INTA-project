compression gzip
================

compression gzip

Function
--------



The **compression gzip** command configures the gRPC server to transmit data in gzip compression mode.

The **undo compression gzip** command restores the default compression mode.



By default, the data transmitted by the gRPC server is not compressed.


Format
------

**compression gzip**

**undo compression gzip**


Parameters
----------

None

Views
-----

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During dynamic telemetry subscription, after this command is run, data is uploaded to the gRPC client in compressed mode, saving the upload link bandwidth.


Example
-------

# Set the compression mode of the gRPC server to gzip.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server
[~HUAWEI-grpc-server] compression gzip

```
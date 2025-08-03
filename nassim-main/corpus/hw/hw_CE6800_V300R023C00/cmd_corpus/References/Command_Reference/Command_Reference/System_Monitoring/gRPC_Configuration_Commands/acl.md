acl
===

acl

Function
--------



The **acl** command configures an ACL for the gRPC service.

The **undo acl** command deletes an ACL of the gRPC service.



By default, no ACL is configured for the gRPC service.


Format
------

**acl** *acl-name*

**acl** *acl-number*

**undo acl** [ *acl-name* ]

**undo acl** *acl-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-name* | Creates a named ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| *acl-number* | Creates a basic or numbered advanced ACL. | The value is an integer ranging from 2000 to 3999.   * A basic ACL number ranges from 2000 to 2999. * An advanced ACL number ranges from 3000 to 3999. |



Views
-----

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, you can run the acl command to configure an ACL for the gRPC service. This allows certain clients to connect to the server.

**Prerequisites**

An ACL has been created.


Example
-------

# Configure ACL 2018 for the gRPC IPv4 service during Telemetry dynamic subscription.
```
<HUAWEI> system-view
[~HUAWEI] acl 2018
[*HUAWEI-acl4-basic-2018] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server
[*HUAWEI-grpc-server] acl 2018

```
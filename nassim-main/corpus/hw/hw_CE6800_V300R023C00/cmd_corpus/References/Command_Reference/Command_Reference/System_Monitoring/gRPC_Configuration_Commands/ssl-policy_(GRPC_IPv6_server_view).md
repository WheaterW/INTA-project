ssl-policy (GRPC IPv6 server view)
==================================

ssl-policy (GRPC IPv6 server view)

Function
--------



The **ssl-policy** command configures an SSL policy for the gRPC IPv6 service.

The **undo ssl-policy** command deletes an SSL policy of the gRPC IPv6 service.



By default, no SSL policy is configured for the gRPC IPv6 service.


Format
------

**ssl-policy** *policy-name*

**undo ssl-policy** [ *policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of an SSL policy. The value must be the name of an existing SSL policy. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



Views
-----

GRPC IPv6 server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, you can configure an SSL policy for the gRPC IPv6 service. This ensures that a secure SSL connection can be established between the server and client.

**Prerequisites**

The SSL policy has been created.


Example
-------

# Configure the SSL policy named policy1 for the gRPC IPv6 service during Telemetry dynamic subscription.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server ipv6
[*HUAWEI-grpc-server-ipv6] ssl-policy policy1

```
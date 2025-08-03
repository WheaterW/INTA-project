protocol (Subscription view)
============================

protocol (Subscription view)

Function
--------



The **protocol** command configures a protocol and encryption mode for the target collector that is associated with the current subscription.

The **undo protocol** command deletes the protocol and encryption mode configured for the target collector that is associated with the current subscription.



By default, no protocol and encryption mode are configured for the target collector that is associated with the current subscription.


Format
------

**protocol** { **grpc** [ **no-tls** ] [ **compression** **gzip** ] | **udp** }

**undo protocol**

**undo protocol** { **grpc** [ **no-tls** ] [ **compression** **gzip** ] | **udp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **grpc** | Specifies gRPC as the data reporting protocol. | - |
| **no-tls** | Parameter indicating whether to use TLS encryption.   * If this parameter is set, TLS encryption is not used. * If this parameter is not set, TLS encryption can be used. | - |
| **compression** | Specifies the data reporting compression type. | - |
| **gzip** | Set the data compression type to gzip. | - |
| **udp** | Specifies UDP as the data reporting protocol. | - |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure a protocol and encryption mode for the target collector associated with a created subscription, run the protocol command.

**Precautions**

Both this command and the **ipv4-address port** command or ipv6-address port command in the Destination-group view can configure a protocol and encryption mode for the target collector. If the target collector is associated with the subscription, command configurations take effect based on the following rules:

* If this command has been run, the protocol and encryption mode configured by running this command in the Subscription view take effect.
* If this command is not run, the protocol and encryption mode configured by running the **ipv4-address port** command or ipv6-address port command in the Destination-group view take effect.


Example
-------

# Configure the gRPC protocol for the target collector associated with the subscription named a.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription a
[*HUAWEI-telemetry-subscription-a] protocol grpc

```
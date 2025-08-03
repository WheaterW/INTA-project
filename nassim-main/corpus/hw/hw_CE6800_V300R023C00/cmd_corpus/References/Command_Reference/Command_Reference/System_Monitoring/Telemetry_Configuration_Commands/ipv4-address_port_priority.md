ipv4-address port priority
==========================

ipv4-address port priority

Function
--------



The **ipv4-address port priority** command configures an IP address, a port number, a transport protocol, an encryption mode, and a priority for a destination collector.

The **undo ipv4-address port priority** command deletes the IP address, port number, transport protocol, encryption mode, and priority of a destination collector.



By default, no IP address, port number, transport protocol, encryption mode, or priority is configured for the destination collector.


Format
------

**ipv4-address** *ip-address-ipv4* **port** *port-value* [ **vpn-instance** *vpn-name* ] [ **protocol** **grpc** [ **no-tls** ] [ **compression** **gzip** ] ] **priority** { **low** | **medium** | **high** }

**undo ipv4-address** *ip-address-ipv4* **port** *port-value* [ **vpn-instance** *vpn-name* ] [ **protocol** **grpc** [ **no-tls** ] [ **compression** **gzip** ] ] **priority** { **low** | **medium** | **high** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address-ipv4* | Specifies an IPv4 address for the destination collector. | It is in dotted decimal notation. |
| *port-value* | Specifies a port number for the destination collector. | The value is an integer ranging from 1 to 65535. |
| **vpn-instance** *vpn-name* | Specifies a VPN instance name for the destination collector. | The value is a string of 1 to 31 characters. The value must be the name of an existing VPN instance. |
| **protocol** | Indicates the data sending protocol. | - |
| **grpc** | Specifies gRPC as the data reporting protocol. | - |
| **no-tls** | Indicates whether to use TLS encryption.   * If this parameter is set, TLS encryption is not used. * If this parameter is not set, TLS encryption can be used. | - |
| **compression** | Specifies the data reporting compression type. | - |
| **gzip** | Sets the data compression type to gzip. | - |
| **low** | Sets the priority of the destination collector to low. | - |
| **medium** | Sets the priority of the destination collector to medium. | - |
| **high** | Sets the priority of the destination collector to high. | - |



Views
-----

Destination group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a destination group is created, you can run this command to configure the IP address, port number, transport protocol, encryption mode, and priority of the destination collector.

**Prerequisites**

You can run the **work-mode priority** command to set the working mode of the destination group to priority.

**Precautions**

This command can be run no more than 40 times for each destination group.

Both this command and the protocol (subscription view) command can be used to configure a transport protocol and encryption mode for the destination collector. If the destination collector is associated with a subscription, the configuration takes effect based on the following rules:

If the protocol command has been run in the subscription view, the transport protocol and encryption mode configured in the subscription view take effect.If the protocol command has not been run in the subscription view, the transport protocol and encryption mode configured in the destination group view take effect.


Example
-------

# Set the IP address of an IPv4 destination collector to 10.1.1.1, port number to 10001, data reporting protocol to gRPC without TLS encryption, and priority to high.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] destination-group test
[*HUAWEI-telemetry-destination-group-test] work-mode priority
Info: In priority mode, only one connection is established.
[*HUAWEI-telemetry-destination-group-test] ipv4-address 10.1.1.1 port 10001 protocol grpc no-tls priority high

```
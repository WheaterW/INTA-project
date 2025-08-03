ipv6-address port
=================

ipv6-address port

Function
--------



The **ipv6-address port** command configures an IPv6 address, port number, transport protocol, and encryption mode for a destination collector.

The **undo ipv6-address port** command deletes the IPv6 address, port number, transport protocol, and encryption mode of the destination collector.



By default, no IP address, port number, transport protocol, or encryption mode is configured for the destination collector.


Format
------

**ipv6-address** *ip-address-ipv6* **port** *port-value* [ **vpn-instance** *vpn-name* ] [ **protocol** { **grpc** [ **no-tls** ] [ **compression** **gzip** ] | **udp** } ]

**undo ipv6-address** *ip-address-ipv6* **port** *port-value* [ **vpn-instance** *vpn-name* ] [ **protocol** { **grpc** [ **no-tls** ] [ **compression** **gzip** ] | **udp** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address-ipv6* | Specifies an IPv6 address for the destination collector. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *port-value* | Specifies a port number for the destination collector. | The value is an integer ranging from 1 to 65535. |
| **vpn-instance** *vpn-name* | Specifies a VPN instance name for the destination collector. | The value is a string of 1 to 31 characters. The value must be the name of an existing VPN instance on the device. |
| **protocol** | Indicates the data sending protocol. | - |
| **grpc** | Specifies gRPC as the data reporting protocol. | - |
| **no-tls** | Parameter indicating whether to use TLS encryption.   * If this parameter is set, TLS encryption is not used. * If this parameter is not set, TLS encryption can be used. | - |
| **compression** | Specifies the data reporting compression type. | - |
| **gzip** | Set the data compression type to gzip. | - |
| **udp** | Indicates that the data sending protocol is UDP. | - |



Views
-----

Destination group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a destination group is created, you can run this command to configure the IP address, port number, transport protocol, and encryption mode of the destination collector.

**Precautions**

* A maximum of 10 destination groups can be configured.
* A maximum of 10 IP addresses can be configured for each destination group. The total number of IPv4 and IPv6 addresses is 10.
* A maximum of 10 IP addresses can be configured globally. The total number of IPv4 and IPv6 addresses is 10.

Both this command and the protocol (Subscription view) command in the subscription view can be used to configure the transmission protocol and encryption mode for the destination collector. When the configured destination collector is associated with a subscription, the configuration takes effect based on the following rules:

* If the protocol (Subscription view) command is run in the subscription view, the transmission protocol and encryption mode configured in the subscription view take effect.
* If the protocol (Subscription view) command is not run in the subscription view, the transmission protocol and encryption mode configured in the destination group view take effect.

Example
-------

# Set the IP address of an IPv6 destination collector to 2001:DB8:2::1, port number to 10001, and data reporting protocol to gRPC with TLS encryption mode.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] destination-group test
[*HUAWEI-telemetry-destination-group-test] ipv6-address 2001:DB8:2::1 port 10001 protocol grpc

```
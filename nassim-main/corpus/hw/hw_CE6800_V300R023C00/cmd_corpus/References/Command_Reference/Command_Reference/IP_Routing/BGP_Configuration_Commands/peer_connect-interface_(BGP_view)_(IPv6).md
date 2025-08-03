peer connect-interface (BGP view) (IPv6)
========================================

peer connect-interface (BGP view) (IPv6)

Function
--------



The **peer connect-interface** command specifies a source interface from which BGP packets are sent, and a source address used for initiating a connection.

The **undo peer connect-interface** command restores the default setting.



By default, the outbound interface of a BGP packet serves as the source interface of a BGP packet.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **connect-interface** { *interface-name* | *ipv6-source-address* | *interface-type* *interface-number* | *interface-name* *ipv6-source-address* | *interface-type* *interface-number* *ipv6-source-address* }

**undo peer** *ipv6-address* **connect-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-bit hexadecimal string in the format of X:X:X:X:X:X:X:X. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *ipv6-source-address* | Specifies an IPv6 source address used for establishing a connection. | The value is a 32-bit hexadecimal string in the format of X:X:X:X:X:X:X:X. |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the **peer connect-interface** command to establish multiple peer relationships between two devices by using multiple links is recommended.If the physical interface has multiple IP addresses, the parameter ipv6-source-address is must in the command peer connect-interface.

**Prerequisites**

Peer relationships have been established using the **peer as-number** command.

**Configuration Impact**

If the **peer connect-interface** or **undo peer connect-interface** command is run, the peer session is disconnected and then re-established. Therefore, exercise caution when running this command.BGP in all address families on a device shares a TCP connection. Therefore, the connect-interface information configured in the BGP view can be inherited by both the IPv4 unicast address family and VPNv4 address family.

**Precautions**

To enable a device to send BGP messages even if a physical interface fails, you can configure a loopback interface as the source interface for sending BGP messages. When the loopback interface is used as the source interface for sending BGP messages to the peer, pay attention to the following points:

* Ensure that the loopback interface address of the BGP peer is reachable.
* In the case of an EBGP connection, you also need to run the **peer ebgp-max-hop** command to allow EBGP to establish the peer relationship in indirect mode.

Note:If the specified interface borrows the IP address of another interface and the IP address is changed, BGP still uses the borrowed IP address to maintain the connection and can send and receive data normally if BGP is not triggered to re-establish the connection. If the re-establishment of the connection is triggered, BGP uses the new IP address to establish the connection.By default, an interface on a device is a Layer 3 interface. After you run the **peer connect-interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.


Example
-------

# Specify a source interface for sending BGP packets for initiating a connection.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] ip address 10.1.1.1 32
[*HUAWEI-LoopBack0] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 connect-interface LoopBack 0

```
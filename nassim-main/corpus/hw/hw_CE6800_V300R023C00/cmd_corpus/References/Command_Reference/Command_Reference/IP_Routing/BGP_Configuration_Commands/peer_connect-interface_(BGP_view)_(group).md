peer connect-interface (BGP view) (group)
=========================================

peer connect-interface (BGP view) (group)

Function
--------



The **peer connect-interface** command specifies a source interface from which BGP packets are sent, and a source address used for initiating a connection.

The **undo peer connect-interface** command restores the default setting.



By default, the outbound interface of a BGP packet serves as the source interface of a BGP packet.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *group-name* **connect-interface** { *interface-name* | *ipv4-source-addr* | *ipv6-source-addr* | *interface-type* *interface-number* | *interface-name* *ipv4-source-addr* | *interface-name* *ipv6-source-addr* | *interface-type* *interface-number* *ipv4-source-addr* | *interface-type* *interface-number* *ipv6-source-addr* }

For CE6885-LL (low latency mode):

**peer** *group-name* **connect-interface** { *interface-name* | *ipv4-source-addr* | *interface-type* *interface-number* | *interface-name* *ipv4-source-addr* | *interface-type* *interface-number* *ipv4-source-addr* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**undo peer** *group-name* **connect-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *interface-name* | Specifies an interface name. | - |
| *ipv4-source-addr* | Specifies an IPv4 source address used for establishing a connection. | The value is in dotted decimal notation. |
| *ipv6-source-addr* | Specifies an IPv6 source address used for establishing a connection.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *interface-type* | Specifies the type of an interface. | - |
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

It is recommended that you run the **peer connect-interface** command when two devices establish multiple peer groups through multiple links.If a physical interface is configured with multiple IP addresses, you must specify ipv4-source-address in the **peer connect-interface** command.

**Prerequisites**

The corresponding peer group relationship has been established using the **group** command.

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
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test connect-interface LoopBack 0

```
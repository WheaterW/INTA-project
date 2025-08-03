peer connect-interface (BGP-VPN instance IPv4 address family view) (group)
==========================================================================

peer connect-interface (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer connect-interface** command specifies a source interface from which BGP packets are sent, and a source address used for initiating a connection.

The **undo peer connect-interface** command restores the default setting.



By default, the outbound interface of a BGP packet serves as the source interface of a BGP packet.


Format
------

**peer** *group-name* **connect-interface** { *interface-name* | *ipv4-source-addr* | *interface-type* *interface-number* | *interface-name* *ipv4-source-addr* | *interface-type* *interface-number* *ipv4-source-addr* }

**undo peer** *group-name* **connect-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *interface-name* | Specifies an interface name. | - |
| *ipv4-source-addr* | Specifies an IPv4 source address used for establishing a connection. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

BGP-VPN instance IPv4 address family view


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
[*HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group test
[*HUAWEI-bgp-vpn1] peer test connect-interface LoopBack 0

```
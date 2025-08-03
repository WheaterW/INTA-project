peer connect-interface (BGP-VPN instance view)(IPv4)
====================================================

peer connect-interface (BGP-VPN instance view)(IPv4)

Function
--------



The **peer connect-interface** command specifies a source interface from which BGP packets are sent, and a source address used for initiating a connection.

The **undo peer connect-interface** command restores the default setting.



By default, the outbound interface of a BGP packet serves as the source interface of a BGP packet.


Format
------

**peer** *ipv4-address* **connect-interface** { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-name* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }

**undo peer** *ipv4-address* **connect-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *ipv4-source-address* | Specifies an IPv4 source address used for establishing a connection. | The value is in dotted decimal notation. |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the **peer connect-interface** command to establish multiple peer relationships between two devices by using multiple links is recommended.If the physical interface has multiple IP addresses, the parameter ipv4-source-address must be in the command peer connect-interface.

**Prerequisites**

Peer relationships have been established using the **peer as-number** command.

**Configuration Impact**

If the **peer connect-interface** or **undo peer connect-interface** command is run, the peer session is disconnected and then re-established. Therefore, exercise caution when running this command.BGP in all address families on a device shares a TCP connection. Therefore, the connect-interface information configured in the BGP view can be inherited by both the IPv4 unicast address family and VPNv4 address family.


Example
-------

# Specify a source interface for sending BGP packets for initiating a connection.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 connect-interface LoopBack 1

```
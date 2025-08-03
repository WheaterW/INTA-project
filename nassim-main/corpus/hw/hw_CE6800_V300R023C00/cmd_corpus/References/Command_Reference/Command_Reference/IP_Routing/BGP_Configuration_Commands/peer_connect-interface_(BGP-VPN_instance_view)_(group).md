peer connect-interface (BGP-VPN instance view) (group)
======================================================

peer connect-interface (BGP-VPN instance view) (group)

Function
--------



The **peer connect-interface** command specifies a source interface from which BGP packets are sent, and a source address used for initiating a connection.

The **undo peer connect-interface** command restores the default setting.



By default, the outbound interface of a BGP packet serves as the source interface of a BGP packet.


Format
------

**peer** *group-name* **connect-interface** { *interface-name* | *ipv4-address* | *interface-type* *interface-number* | *interface-name* *ipv4-address* | *interface-type* *interface-number* *ipv4-address* }

**undo peer** *group-name* **connect-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *interface-name* | Specifies an interface name. | - |
| *ipv4-address* | Specifies an IPv4 source address used for establishing a connection. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface. | - |
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

It is recommended that you run the **peer connect-interface** command when two devices establish multiple peer groups through multiple links.If a physical interface is configured with multiple IP addresses, you must specify ipv4-source-address in the **peer connect-interface** command.

**Prerequisites**

The corresponding peer group relationship has been established using the **group** command.


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
[*HUAWEI-bgp-instance-vpn1] group test
[*HUAWEI-bgp-instance-vpn1] peer test connect-interface LoopBack 1

```
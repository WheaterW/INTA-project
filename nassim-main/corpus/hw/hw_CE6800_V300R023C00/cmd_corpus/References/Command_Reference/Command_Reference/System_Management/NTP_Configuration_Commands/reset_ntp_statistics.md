reset ntp statistics
====================

reset ntp statistics

Function
--------



The **reset ntp statistics** command deletes statistics about NTP packets, peers, or clocks.




Format
------

**reset ntp statistics packet** [ **ipv6** ]

**reset ntp statistics packet** [ **ipv6** ] **interface** { *interface-name* | *interface-type* *interface-number* | **all** }

**reset ntp statistics packet peer** [ [ *ip-address* [ **vpn-instance** *vpn-instance-name* ] ] | **ipv6** [ *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] ] | **domain** [ *domainName* [ **vpn-instance** *vpn-instance-name* ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *ipv6-address* | Indicates the IPv6 address of a peer. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv6** | IPv6 peer packet statistics. | - |
| **packet** | Packet statistics. | - |
| **interface** *interface-type* | Resets statistics about NTP packets on a specified interface. | - |
| **interface** *interface-number* | Resets statistics about NTP packets on a specified interface. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **interface** *interface-name* | Resets statistics about NTP packets on a specified interface. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **all** | Reset all statistics. | - |
| **peer** | Peer packet statistics. | - |
| *ip-address* | Specifies the IP address of a peer. | The value is an IPv4 address in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance associated with an NTP peer. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **domain** *domainName* | Specifies the domain name of a peer. | The value is a string of 1 to 255 characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command helps you repeatedly delete NTP statistics during debugging.Once deleted, statistics cannot be restored. Therefore, exercise caution when deleting statistics.


Example
-------

# Delete statistics about NTP packets.
```
<HUAWEI> reset ntp statistics packet

```

# Delete statistics about NTP peers.
```
<HUAWEI> reset ntp statistics packet peer

```

# Delete statistics about NTP interfaces.
```
<HUAWEI> reset ntp statistics packet interface all

```
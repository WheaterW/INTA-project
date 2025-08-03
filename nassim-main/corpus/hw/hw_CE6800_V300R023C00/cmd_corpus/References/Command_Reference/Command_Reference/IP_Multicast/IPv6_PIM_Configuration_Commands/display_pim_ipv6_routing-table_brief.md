display pim ipv6 routing-table brief
====================================

display pim ipv6 routing-table brief

Function
--------



The **display pim ipv6 routing-table brief** command displays brief information about an IPv6 PIM routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6** { **vpn-instance** *vpn-instance-name* | **all-instance** } **routing-table** **brief** [ *groupAddr* [ **mask** *group-mask-length* ] | *srcAddr* [ **mask** *source-mask-length* ] | **incoming-interface** { { *iif-port-type* *iif-port-num* | *iif-port-name* } | **register** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |
| *groupAddr* | Specifies the IPv6 address of a multicast group. | The address is in the format of X:X:X:X:X:X:X:X. |
| **mask** *group-mask-length* | Specifies the mask length of a multicast group. | The value is an integer ranging from 0 to 128. |
| **mask** *source-mask-length* | Specifies the mask length of a multicast source. | The value is an integer ranging from 0 to 128. |
| *srcAddr* | Specifies the IPv6 address of a multicast source. | The address is in the format of X:X:X:X:X:X:X:X. |
| **incoming-interface** *iif-port-type* *iif-port-num* | Displays the PIM routing entries with specified upstream interfaces. | - |
| *iif-port-name* | Displays the PIM routing entries with specified upstream interfaces. | - |
| **register** | Displays information about a register interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim ipv6 routing-table brief** command only the names of upstream interfaces and the number of downstream interfaces of IPv6 PIM routing entries are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about an IPv6 PIM routing table.
```
<HUAWEI> display pim ipv6 vpn-instance abc routing-table brief FF25::1
 VPN-Instance: abc
 Total 3 (*, G) entries; 3 (S, G) entries

 Total matched 1 (*, G) entry; 1 (S, G) entry

  00001. (2001:DB8:1::1, FF25::1)
       Upstream interface: 100GE1/0/1
       Number of downstreams: 2048
  00002. (*, FF25::1)
       Upstream interface: 100GE1/0/1
       Number of downstreams: 2048

```

**Table 1** Description of the **display pim ipv6 routing-table brief** command output
| Item | Description |
| --- | --- |
| Total 3 (\*, G) entries; 3 (S, G) entries | Total number of (S, G) entries and (\*, G) entries in an IPv6 PIM routing table. |
| Total matched 1 (\*, G) entry; 1 (S, G) entry | Total number of (S, G) entries and (\*, G) entries that meet specified conditions in an IPv6 PIM routing table. |
| Upstream interface | Name of upstream interface. |
| Number of downstreams | Number of downstream interfaces of an (S, G) entry or (\*, G) entry. |
| VPN-Instance | VPN instance to which PIM routing information belongs. |
| (2001:db8:1::1, FF25::1) | Number of an (S, G) entry. |
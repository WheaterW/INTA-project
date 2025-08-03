display pim ipv6 rp-info
========================

display pim ipv6 rp-info

Function
--------



The **display pim ipv6 rp-info** command displays information about the Rendezvous Point (RP) to which multicast groups correspond.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 rp-info** [ *ipv6-group-address* ]

**display pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **rp-info** [ *ipv6-group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies a multicast group address. | The value ranges from FF00:: to FFFF:FFFF:FFFF:FFFF: FFFF:FFFF:FFFF:FFFF, in hexadecimal notation. |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display pim ipv6 rp-info command is used to view information about static RPs and dynamic RPs, including the RP address, priority, addresses of groups that the RP serves, and the length of time during which the RP has been up.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the RP to which multicast group FF0E::1 corresponds.
```
<HUAWEI> display pim ipv6 rp-info ff0e::1
 VPN-Instance: public net
 BSR RP Address is: 2001:DB8:1::1
     Priority: 192
     Uptime: 00:00:52
     Expires: 00:01:38
     BIDIR: Y
 RP mapping for this group is: 2001:DB8:1::1 (local host)

```

**Table 1** Description of the **display pim ipv6 rp-info** command output
| Item | Description |
| --- | --- |
| BSR RP Address is | Address of the BootStrap router (BSR) RP. |
| RP mapping for this group is | Address of the RP to which a multicast group corresponds. |
| VPN-Instance | VPN instance to which RP information belongs. |
| Priority | Priority of the RP. |
| Uptime | Length of time the RP has been up. |
| Expires | Remaining time before the RP times out. |
| BIDIR | Whether the RP serves IPv6 Bidirectional Protocol Independent Multicast (BIDIR-PIM).   * Y: yes. * N: no. |
display pim ipv6 neighbor
=========================

display pim ipv6 neighbor

Function
--------



The **display pim ipv6 neighbor** command displays information about IPv6 PIM neighbors.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 neighbor** [ *nbrAddrValue* | **interface** { *ifName* | *ifType* *ifNum* } | **verbose** ] \*

**display pim ipv6** { **vpn-instance** *vpn-instance-name* | **all-instance** } **neighbor** [ *nbrAddrValue* | **interface** { *ifName* | *ifType* *ifNum* } | **verbose** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *nbrAddrValue* | Specifies the IPv6 link-local address of a neighbor. | The address is in the format of X:X:X:X:X:X:X:X. |
| **interface** *ifType* | Specifies the type of an interface. | - |
| *ifName* | Specifies the name of an interface. | - |
| *ifNum* | Specifies the number of an interface. | - |
| **verbose** | Displays detailed information about a neighbor. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about unicast routes in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

An interface can set up a PIM neighbor relationship with other Routers after being enabled with PIM-SM. The **display pim neighbor** command is used to view PIM neighbor information, including the IP address of a PIM neighbor, existing period of a neighbor, and Designated router (DR) priority.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about IPv6 PIM neighbors of 100GE1/0/1.
```
<HUAWEI> display pim ipv6 neighbor interface 100GE 1/0/1 verbose
VPN-Instance: public net

Total Number of Neighbors on this interface  = 1

Neighbor: FF80::FFE0:FFFF:FE4A:8E04
Interface: 100GE1/0/1
Uptime: 00:01:18
Expiry time: 00:01:31
DR Priority: 1
Generation ID: 0X7751638D
Holdtime: 105 s
LAN delay: 500 ms
Override interval: 2500 ms
Neighbor tracking: Disabled
     PIM BFD-Session: Y 
     PIM BFD-Session min-tx-interval: 100 ms 
     PIM BFD-Session min-rx-interval: 100 ms 
     PIM BFD-Session detect-multiplier: 3
PIM BIDIR: Y
Neighbor Secondary Address(es):
2001:DB8:1::1

```

**Table 1** Description of the **display pim ipv6 neighbor** command output
| Item | Description |
| --- | --- |
| Total Number of Neighbors on this interface | Total number of PIM neighbors on an interface. |
| Expiry time | Time before a PIM neighbor times out. |
| DR Priority | DR priority. |
| Generation ID | Random number of the PIM neighbor status. |
| LAN delay | Delay for transmitting Prune messages. |
| Override interval | Interval for overriding the Prune action. |
| Neighbor | Address of a PIM neighbor. |
| Neighbor tracking | Whether to enable neighbor tracking. |
| Neighbor Secondary Address(es) | IPv6 address of a neighbor. |
| PIM BFD-Session | Whether a PIM IPv6 BFD session is established between PIM neighbors. |
| PIM BFD-Session min-tx-interval | Actual interval for sending PIM IPv6 BFD packets. |
| PIM BFD-Session min-rx-interval | Actual interval for receiving PIM IPv6 BFD packets. |
| PIM BFD-Session detect-multiplier | Actual detection time multiplier of PIM IPv6 BFD packets. |
| PIM BIDIR | Whether IPv6 Bidirectional Protocol Independent Multicast (BIDIR-PIM) is enabled on an IPv6 PIM neighbor.   * Y: yes. * N: no. |
| VPN-Instance | VPN instance to which PIM neighbor information belongs. |
| Interface | Interface on which a PIM neighbor relationship is established. |
| Uptime | Existing time of a PIM neighbor. |
| Holdtime | Holdtime of a PIM neighbor. |
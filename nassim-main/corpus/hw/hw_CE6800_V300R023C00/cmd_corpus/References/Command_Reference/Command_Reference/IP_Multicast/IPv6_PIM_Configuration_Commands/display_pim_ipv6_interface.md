display pim ipv6 interface
==========================

display pim ipv6 interface

Function
--------



The **display pim ipv6 interface** command displays information about an IPv6 PIM interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 interface** [ *interface-name* | *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ]

**display pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **interface** [ *interface-name* | *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| **up** | Displays information about the IPv6 PIM interface whose protocol status is Up. | - |
| **down** | Displays information about the IPv6 PIM interface whose protocol status is Down. | - |
| **verbose** | Displays detailed information about an IPv6 PIM interface. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The interface enabled with PIM-SM is called a PIM interface. The **display pim ipv6 interface** command is used to display information about an IPv6 PIM interface, including the PIM status, number of PIM neighbors, interval for sending Hello messages, Designated router (DR) priority, and DR address.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed IPv6 PIM information on 100GE1/0/1.
```
<HUAWEI> display pim ipv6 interface 100GE 1/0/1 verbose
 VPN-Instance: public net
 Interface: 100GE1/0/1, FE80::2E0:3FFF:FE27:AE01
     PIM version: 2
     PIM mode: Sparse
     PIM state: up
     PIM DR: FE80::2E0:3FFF:FE27:AE01 (local)
     PIM DR Priority (configured): 1
     PIM neighbor count: 0
     PIM hello interval: 30 s
     PIM LAN delay (negotiated): 500 ms
     PIM LAN delay (configured): 500 ms
     PIM hello override interval (negotiated): 2500 ms
     PIM hello override interval (configured): 2500 ms
     PIM Silent: disabled
     PIM neighbor tracking (negotiated): disabled
     PIM neighbor tracking (configured): disabled
     PIM generation ID: 0X18FF94EC
     PIM require-GenID: disabled
     PIM hello hold interval: 105 s
     PIM assert hold interval: 180 s
     PIM triggered hello delay: 5 s
     PIM J/P interval: 60 s
     PIM J/P hold interval: 210 s
     PIM state-refresh capability on link: non-capable
    PIM BSR domain border: disabled
     PIM BFD: enabled
     PIM BFD min-tx-interval: 100 ms
     PIM BFD min-rx-interval: 100 ms
     PIM BFD detect-multiplier: 5
     PIM dr-switch-delay timer: not configured
     PIM offer-interval: 1 s
     PIM election-robust-count: 5
     PIM backoff-interval: 1 s
     Number of routers on link not using DR priority: 0
     Number of routers on link not using LAN delay: 0
     Number of routers on link not using neighbor tracking: 1
     ACL of PIM neighbor policy: myacl6
     ACL of PIM ASM join policy: 2000
     ACL of PIM SSM join policy: -
     ACL of PIM join policy: -
     PIM ipsec: disable

```

# Display IPv6 PIM information on 100GE1/0/1.
```
<HUAWEI> display pim ipv6 interface 100GE 1/0/1
VPN-Instance: public net
Interface           State NbrCnt HelloInt   DR-Pri     DR-Address
100GE1/0/1         up    0      30         1          FE80::2E0:8AFF: (local)

```

**Table 1** Description of the **display pim ipv6 interface** command output
| Item | Description |
| --- | --- |
| PIM version | Version of the PIM running on an interface. |
| PIM mode | PIM mode, which can be dense or sparse. |
| PIM state | Status of an IPv6 PIM interface:   * up: The interface starts normally. * down: An error occurs on the physical link of the interface. |
| PIM DR | DR address. |
| PIM DR Priority (configured) | DR priority. |
| PIM neighbor count | Number of PIM neighbors on an IPv6 PIM interface. |
| PIM hello interval | Interval for sending PIM Hello messages. |
| PIM LAN delay (negotiated) | Negotiated delay in transmitting packets on an IPv6 PIM interface. |
| PIM LAN delay (configured) | Configured delay in transmitting packets on an IPv6 PIM interface. |
| PIM hello override interval (negotiated) | Negotiated overriding interval on an IPv6 PIM interface. |
| PIM hello override interval (configured) | Configured overriding interval on an IPv6 PIM interface. |
| PIM Silent | Whether PIM silent is enabled on an IPv6 PIM interface. |
| PIM neighbor tracking (negotiated) | Whether PIM neighbor tracking is enabled on an IPv6 PIM interface through negotiation. |
| PIM neighbor tracking (configured) | Whether PIM neighbor tracking is configured on an IPv6 PIM interface. |
| PIM generation ID | Generation ID on an Pv6 PIM interface. |
| PIM require-GenID | Whether to check the generation ID option contained in the received messages. |
| PIM hello hold interval | Time during which a receiver of the Hello message holds the reachable state of its neighbor. |
| PIM assert hold interval | Interval for sending Assert messages. |
| PIM triggered hello delay | Maximum random delay in triggering Hello messages. |
| PIM J/P interval | Interval for sending Join/Prune messages. |
| PIM J/P hold interval | Time during which an IPv6 PIM interface holds the Join/Prune status. |
| PIM state-refresh capability on link | Whether the State-Refresh function is enabled on the link. |
| PIM BSR domain border | Whether a PIM BootStrap router (BSR) boundary is configured on an IPv6 PIM interface. |
| PIM BFD | Whether IPv6 BFD for PIM is enabled on an IPv6 PIM interface. |
| PIM BFD min-tx-interval | Minimum interval for sending PIM IPv6 BFD packets. |
| PIM BFD min-rx-interval | Minimum interval for receiving PIM IPv6 BFD packets. |
| PIM BFD detect-multiplier | Local detection time multiplier of PIM IPv6 BFD packets. |
| PIM dr-switch-delay timer | Delay in DR switchover. |
| PIM offer-interval | Interval at which the interface sends Offer messages. |
| PIM election-robust-count | Designated forwarder (DF) election robust variable of the interface. |
| Number of routers on link not using DR priority | Number of routers that have not used DR priorities in the network segment where an IPv6 PIM interface resides. |
| Number of routers on link not using LAN delay | Number of routers that have not used LAN delay in the network segment where an IPv6 PIM interface resides. |
| Number of routers on link not using neighbor tracking | Number of routers that have not used neighbor tracking in the network segments where an IPv6 PIM interface resides. |
| ACL of PIM neighbor policy | Neighbor filtering policy configured on an IPv6 PIM interface. |
| ACL of PIM join policy | Policy for filtering Join messages configured on an IPv6 PIM interface. |
| ACL of PIM ASM join policy | Policy for filtering Any-Source Multicast (ASM) Join messages configured on an IPv6 PIM interface. |
| ACL of PIM SSM join policy | Policy for filtering Source-Specific Multicast (SSM) Join messages configured on an IPv6 PIM interface. |
| Interface | Name of an IPv6 PIM interface. |
| State | Status of an IPv6 PIM interface:   * up: The interface starts normally. * down: An error occurs on the physical link of the interface. |
| NbrCnt | Number of PIM neighbors on an IPv6 PIM interface. |
| HelloInt | Interval for sending Hello messages. |
| DR-Pri | DR priority. |
| DR-Address | DR address. |
| VPN-Instance | VPN instance to which the output information belongs. |
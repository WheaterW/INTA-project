auto-defend protocol
====================

auto-defend protocol

Function
--------



The **auto-defend protocol** command specifies the types of protocol packets that the device monitors in attack source tracing.

The **undo auto-defend protocol** command deletes specified types of protocol packets that the device monitors in attack source tracing.



By default, attack source tracing is applied to ARP, DHCP, DHCPv6, DNS, ICMP, ICMPv6, IGMP, MLD, ND, TCP, TCPv6 and Telnet packets.

For the CE6885-LL in low latency mode, by default, attack source tracing is applied to ARP, DHCP, DNS, ICMP, IGMP, TCP, and Telnet packets.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-defend protocol** { { **arp** | **icmp** | **dhcp** | **igmp** | **ttl-expired** | **nd** | **telnet** | **icmpv6** | **dhcpv6** | **mld** | **tcp** | **udp** | **tcpv6** | **dns** } \* | **all** }

**undo auto-defend protocol** { { **arp** | **icmp** | **dhcp** | **igmp** | **ttl-expired** | **nd** | **telnet** | **icmpv6** | **dhcpv6** | **mld** | **tcp** | **udp** | **tcpv6** | **dns** } \* | **all** }

For CE6885-LL (low latency mode):

**auto-defend protocol** { { **arp** | **icmp** | **dhcp** | **igmp** | **ttl-expired** | **telnet** | **tcp** | **udp** | **dns** } \* | **all** }

**undo auto-defend protocol** { { **arp** | **icmp** | **dhcp** | **igmp** | **ttl-expired** | **telnet** | **tcp** | **udp** | **dns** } \* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp** | Adds Address Resolution Protocol (ARP) packets to the list of traced packets or deletes ARP packets from the list. | - |
| **icmp** | Adds Internet Control Message Protocol (ICMP) packets to the list of traced packets or deletes ICMP packets from the list. | - |
| **dhcp** | Adds Neighbor Discovery Protocol (DHCP) packets to the list of traced packets or deletes DHCP packets from the list. | - |
| **igmp** | Adds Internet Group Management Protocol (IGMP) packets to the list of traced packets or deletes IGMP packets from the list. | - |
| **ttl-expired** | Adds the packets with TTL or hop limit value being 1 to the traced packet list or deletes the packets with TTL or hop limit value being 1 from the list. | - |
| **nd** | Adds Neighbor Discovery Protocol (ND) packets to the list of traced packets or deletes ND packets from the list.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **telnet** | Adds telnet packets to the list of traced packets or deletes telnet packets from the list. | - |
| **icmpv6** | Adds ICMPv6 packets to the list of traced packets or deletes ICMPv6 packets from the list.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **mld** | Adds Internet Group Management Protocol (MLD) packets to the list of traced packets or deletes MLD packets from the list.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **tcp** | Adds Transmission Control Protocol (TCP) packets to the list of traced packets or deletes TCP packets from the list. | - |
| **udp** | Adds User Datagram Protocol (UDP) packets to the list of traced packets or deletes UDP packets from the list. | - |
| **tcpv6** | Adds Transmission Control Protocol Version 6 (TCPv6) packets to the list of traced packets or deletes TCPv6 packets from the list.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dns** | Adds DNS packets to the list of traced packets or deletes DNS packets from the list. | - |
| **all** | Specifies the type of attack source tracing packets that the device supports. | - |
| **dhcpv6** | Adds Neighbor Discovery Protocol (DHCPv6) packets to the list of traced packets or deletes DHCPv6 packets from the list.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The attack source tracing process consists of four phases: packet parsing, traffic analysis, attack source identification, and taking attack source punish actions. The auto-defend protocol command is applied to the packet parsing phase. When an attack occurs, you cannot identify the type of attack packets. The auto-defend protocol command allows you to flexibly specify the types of traced packets.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Precautions**



If a packet type is specified, when the device is attacked and the attack source is traced, you can run the **display auto-defend attack-source** command to view attack source information.If attack source tracing has been enabled using the **auto-defend enable** command, you cannot run the **undo auto-defend protocol** command to delete all source tracing protocols.




Example
-------

# Delete ARP packets from the list of traced packets.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] undo auto-defend protocol arp

```
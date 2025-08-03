auto-port-defend protocol threshold
===================================

auto-port-defend protocol threshold

Function
--------



The **auto-port-defend protocol threshold** command sets the protocol packet rate threshold for port attack defense.

The **undo auto-port-defend protocol threshold** command restores the default protocol packet rate threshold for port attack defense.



By default, the rate threshold for protocol packets in port attack defense is 80% of the default CAR value for the protocol.


Format
------

For CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **threshold** *threshold-value*

**undo auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **threshold**

For CE6885-LL (low latency mode):

**auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **icmp** | **igmp** | **ip-fragment** | **isis** | **lacp** | **ospf** | **pim** | **pim-mc** | **vrrp** } **threshold** *threshold-value*

**undo auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **icmp** | **igmp** | **ip-fragment** | **isis** | **lacp** | **ospf** | **pim** | **pim-mc** | **vrrp** } **threshold**

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-discovery** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **threshold** *threshold-value*

**undo auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-discovery** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp-request** | Specifies the rate threshold for ARP request packets. | - |
| **arp-request-uc** | Specifies the rate threshold for ARP request packets. | - |
| **arp-reply** | Specifies the rate threshold for ARP Reply packets. | - |
| **dhcp-discovery** | Applies port attack defense to DHCP Discovery packets or cancels port attack defense for DHCP Discovery packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **dhcp-request** | Specifies the rate threshold for DHCP server packets. | - |
| **dhcpv6-discovery** | Specifies the rate threshold for DHCPv6 discovery packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dhcpv6-request** | Specifies the rate threshold for DHCPv6 request packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **igmp** | Specifies the rate threshold for IGMP packets. | - |
| **isis** | Specifies the rate threshold for ISIS packets. | - |
| **isis-overlay** | Specifies the rate threshold for Overlay ISIS packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **nd** | Specifies the rate threshold for ND packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospf** | Specifies the rate threshold for OSPF packets. | - |
| **ospf-hello** | Specifies the rate threshold for OSPF Hello packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospfv3** | Specifies the rate threshold for OSPFv3 packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vrrp** | Specifies the rate threshold for VRRP packets. | - |
| **vrrp6** | Specifies the rate threshold for VRRP6 packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **lacp** | Specifies the rate threshold for LACP packets. | - |
| **pim** | Specifies the rate threshold for PIM packets. | - |
| **pim-mc** | Specifies PIM multicast packets. | - |
| *threshold-value* | Specifies the rate threshold for auto port defend. | The value is an integer in the range from 1 to 65535. |
| **dhcp-reply** | Specifies the rate threshold for DHCP client packets. | - |
| **dhcpv6-reply** | Specifies the rate threshold for DHCPv6 reply packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **icmp** | Specifies the rate threshold for ICMP packets. | - |
| **ip-fragment** | Specifies the rate threshold for IP fragment packets. | - |
| **ospf-overlay** | Specifies the rate threshold for Overlay OSPF packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospf-hello-overlay** | Specifies the rate threshold for Overlay OSPF hello packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospfv3-overlay** | Specifies the rate threshold for Overlay OSPFv3 packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After port attack defense is enabled on a port, the device calculates the rate of affected protocol packets received by the port. If the packet rate exceeds the protocol rate threshold, the device considers that an attack occurs. Then the device traces the source and limits the rate of attack packets on the port, and records a log. The device moves the packets within the protocol rate limit (CPCAR in attack defense policies) to the low-priority queue, and then sends them to the CPU. The device discards the excess packets.You need to set an appropriate rate threshold for port attack defense according to service requirements. If the CPU fails to process many protocol packets promptly after port attack defense is enabled, set a large packet rate threshold. If the CPU is busy processing the packets of a protocol, set a small rate threshold for this protocol to avoid impact on other services.

**Precautions**



If you run the **auto-port-defend protocol threshold** command multiple times in the same attack defense policy view, only the latest configuration takes effect.By default, the rate threshold for IP fragments in port attack defense is 1228 pps on common models.




Example
-------

# In the attack defense policy test, set the rate threshold for ARP Request packets to 40 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend protocol arp-request threshold 40

```
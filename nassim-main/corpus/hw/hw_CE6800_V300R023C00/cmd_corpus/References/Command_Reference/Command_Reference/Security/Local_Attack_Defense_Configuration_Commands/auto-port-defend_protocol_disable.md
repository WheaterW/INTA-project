auto-port-defend protocol disable
=================================

auto-port-defend protocol disable

Function
--------



The **auto-port-defend protocol disable** command disables the port-based automatic local attack defense function of specified type of protocol.

The **undo auto-port-defend protocol disable** command enables the port-based automatic local attack defense function of specified type of protocol.



By default, port-based automatic local attack defense of all supported protocols is enabled.


Format
------

For CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **disable**

**undo auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **disable**

For CE6885-LL (low latency mode):

**auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **icmp** | **igmp** | **ip-fragment** | **isis** | **lacp** | **ospf** | **pim** | **pim-mc** | **vrrp** } **disable**

**undo auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-request** | **dhcp-reply** | **icmp** | **igmp** | **ip-fragment** | **isis** | **lacp** | **ospf** | **pim** | **pim-mc** | **vrrp** } **disable**

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-discovery** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **disable**

**undo auto-port-defend protocol** { **arp-request** | **arp-request-uc** | **arp-reply** | **dhcp-discovery** | **dhcp-request** | **dhcp-reply** | **dhcpv6-discovery** | **dhcpv6-reply** | **dhcpv6-request** | **icmp** | **igmp** | **ip-fragment** | **isis** | **isis-overlay** | **lacp** | **nd** | **ospf** | **ospf-hello** | **ospf-overlay** | **ospf-hello-overlay** | **ospfv3** | **ospfv3-overlay** | **pim** | **pim-mc** | **vrrp** | **vrrp6** } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp-request** | Applies port attack defense to ARP Request packets or cancels port attack defense for ARP Request packets. | - |
| **arp-request-uc** | Applies port attack defense to Unicast ARP Request packets or cancels port attack defense for Unicast ARP request packets. | - |
| **arp-reply** | Applies port attack defense to ARP Reply packets or cancels port attack defense for ARP Reply packets. | - |
| **dhcp-discovery** | Applies port attack defense to DHCP Discovery packets or cancels port attack defense for DHCP Discovery packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **dhcp-request** | Applies port attack defense to DHCP Request packets or cancels port attack defense for DHCP Request packet. | - |
| **dhcpv6-discovery** | Applies port attack defense to DHCPv6 Discovery packets or cancels port attack defense for DHCPv6 Discovery packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dhcpv6-request** | Applies port attack defense to DHCPv6 Request packets or cancels port attack defense for DHCPv6 Request packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **isis** | Applies port attack defense to ISIS packets or cancels port attack defense for ISIS packets. | - |
| **isis-overlay** | Applies port attack defense to Overlay ISIS packets or cancels port attack defense for Overlay ISIS packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **nd** | Applies port attack defense to ND packets or cancels port attack defense for ND packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospf** | Applies port attack defense to OSPF packets or cancels port attack defense for OSPF packets. | - |
| **ospf-hello** | Applies port attack defense to OSPF Hello packets or cancels port attack defense for OSPF Hello packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospfv3** | Applies port attack defense to OSPFv3 packets or cancels port attack defense for OSPFv3 packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vrrp** | Applies port attack defense to VRRP packets or cancels port attack defense for VRRP packets. | - |
| **vrrp6** | Applies port attack defense to VRRP6 packets or cancels port attack defense for VRRP6 packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **lacp** | Applies port attack defense to LACP packets or cancels port attack defense for LACP packets. | - |
| **igmp** | Applies port attack defense to IGMP packets or cancels port attack defense for IGMP packets. | - |
| **pim** | Applies port attack defense to PIM packets or cancels port attack defense for PIM packets. | - |
| **pim-mc** | Applies port attack defense to PIM-MC packets or cancels port attack defense for PIM-MC packet. | - |
| **dhcp-reply** | Applies port attack defense to DHCP Reply packets or cancels port attack defense for DHCP Reply packets. | - |
| **dhcpv6-reply** | Applies port attack defense to DHCPv6 Reply packets or cancels port attack defense for DHCPv6 Reply packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **icmp** | Applies port attack defense to ICMP packets or cancels port attack defense for ICMP packets. | - |
| **ip-fragment** | Applies port attack defense to IP fragment packets or cancels port attack defense for IP fragment packets. | - |
| **ospf-overlay** | Applies port attack defense to Overlay OSPF packets or cancels port attack defense for Overlay OSPF packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospf-hello-overlay** | Applies port attack defense to Overlay OSPF Hello packets or cancels port attack defense for Overlay OSPF Hello packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospfv3-overlay** | Applies port attack defense to Overlay OSPFv3 packet packets or cancels port attack defense for Overlay OSPFv3 packet packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device calculates the rate of all protocol packets that can be defended against and are received by the interface, and traces the source and limits the rate of attack packets on the interface. If the device detects only a few types of attack packets, you can run the **auto-port-defend protocol disable** command to delete unnecessary types of attack packets. This prevents the device from limiting the rate of too many protocol packets and ensures normal services.

**Precautions**

After port attack defense is applied to a type of protocol packets, the **display auto-port-defend attack-source** command can display the attack source tracing information if the port is attacked by the specified protocol packets.


Example
-------

# In the attack defense policy view, disable port-based automatic local attack defense for ARP Request packets.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend protocol arp-request disable

```
cpu-defend host-car
===================

cpu-defend host-car

Function
--------



The **cpu-defend host-car** command specifies the types of packets to be limited in user-level rate limiting.

The **undo cpu-defend host-car** command deletes the configuration.



By default, user-level rate limiting can apply to ARP, ND, DHCP Request, and DHCPv6 Request packets.

For the CE6885-LL in low latency mode, by default, user-level rate limiting can apply to ARP and DHCP Request packets.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**cpu-defend host-car** { { **arp** | **dhcp-request** | **dhcpv6-request** | **nd** } \* | **all** }

**undo cpu-defend host-car** { { **arp** | **dhcp-request** | **dhcpv6-request** | **nd** } \* }

For CE6885-LL (low latency mode):

**cpu-defend host-car** { { **arp** | **dhcp-request** } \* | **all** }

**undo cpu-defend host-car** { { **arp** | **dhcp-request** } \* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp** | Applies user-level rate limiting to ARP packets. | - |
| **dhcp-request** | Applies user-level rate limiting to DHCP Request packets. | - |
| **dhcpv6-request** | Applies user-level rate limiting to DHCPv6 Request packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **nd** | Applies user-level rate limiting to ND packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **all** | Applies all user-level rate limiting packets. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After user-level rate limiting is enabled, the device limits the rate of ARP, ND, DHCP Request, and DHCPv6 Request packets based on user MAC addresses by default. If the number of the preceding types of packets received by the device from the same source MAC address exceeds the rate limit, the device discards the excess packets. To limit the rate of some types of packets, run this command to configure the types of packets for which user-level rate limiting is performed.



By default, user-level rate limiting can apply to ARP and DHCP Request packets.



**Precautions**

User-level rate limiting has been enabled using the **cpu-defend host-car enable** command.This command is an overriding one. For example, after the **cpu-defend host-car arp** command is run, user-level rate limiting takes effect only for ARP packets but not for DHCP Request packets.


Example
-------

# Configure user-level rate limiting for ARP, DHCP Request, and ND packets.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend host-car enable
[~HUAWEI] cpu-defend host-car arp dhcp-request nd

```

# Configure user-level rate limiting for ARP and DHCP Request packets.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend host-car enable
[~HUAWEI] cpu-defend host-car arp dhcp-request

```
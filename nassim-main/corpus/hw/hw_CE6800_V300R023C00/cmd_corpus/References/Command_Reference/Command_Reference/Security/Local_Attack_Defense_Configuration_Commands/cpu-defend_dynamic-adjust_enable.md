cpu-defend dynamic-adjust enable
================================

cpu-defend dynamic-adjust enable

Function
--------



The **cpu-defend dynamic-adjust enable** command enables adaptive CPCAR adjustment for protocol packets.

The **undo cpu-defend dynamic-adjust enable** command disables adaptive CPCAR adjustment for protocol packets and restores the default CPCAR values of protocol packets.



By default, adaptive CPCAR adjustment for protocol packets is enabled.


Format
------

For CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**cpu-defend dynamic-adjust** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-reply** | **dhcp-request** | **nd** } ] **enable**

**undo cpu-defend dynamic-adjust** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-reply** | **dhcp-request** | **nd** } ] **enable**

For CE6885-LL (low latency mode):

**cpu-defend dynamic-adjust** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-reply** | **dhcp-request** } ] **enable**

**undo cpu-defend dynamic-adjust** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-reply** | **dhcp-request** } ] **enable**

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**cpu-defend dynamic-adjust** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-discovery** | **dhcp-reply** | **dhcp-request** | **nd** } ] **enable**

**undo cpu-defend dynamic-adjust** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-discovery** | **dhcp-reply** | **dhcp-request** | **nd** } ] **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** | Specifies the packet type. | - |
| **arp-reply** | Specifies ARP reply packets. | - |
| **arp-request** | Specifies ARP request packets. | - |
| **arp-request-uc** | Specifies unicast ARP request packets. | - |
| **dhcp-discovery** | Specifies DHCP discovery packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **dhcp-reply** | Specifies DHCP reply packets. | - |
| **dhcp-request** | Specifies DHCP request packets. | - |
| **nd** | Specifies the ND packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the fixed default CPCAR value cannot meet the dynamic requirements on the rate at which protocol packets are sent, you can run this command to enable the switch to dynamically adjust the default CPCAR value for protocol packets.If adaptive adjustment of the default CPCAR value is enabled for a specific type of protocol packets, the device checks for packet loss of such protocol packets at a specified interval. When detecting a packet loss, the device dynamically adjusts the CPCAR value for the protocol packets based on the CPU usage. When the CPU usage is lower than 50%, increase the CPCAR value. The adjusted CPCAR value cannot exceed the maximum CPCAR value. When the CPU usage is higher than 68%, decrease the CPCAR value. The adjusted CPCAR value cannot be smaller than the default value. If packet loss occurs due to congestion in the queue where the detected protocol packets reside, the device restores the default CPCAR value for the protocol packets. You can run the **display cpu-defend dynamic-adjust history-record** command to view records of dynamic CPCAR adjustment.The following table lists the types of protocol packets for which CPCAR values can be dynamically adjusted and the maximum CPCAR values after adjustment.

* The adjusted maximum CPCAR value for ARP reply packets is twice the default value.
* The adjusted maximum CPCAR value for ARP request packets is twice the default value.
* The adjusted maximum CPCAR value for unicast ARP request packets is twice the default value.
* The adjusted maximum CPCAR value for DHCP reply packets is 1.5 times the default value.
* The adjusted maximum CPCAR value for DHCP request packets is 1.5 times the default value.
* The adjusted maximum CPCAR value for IPv6 ND packets is twice the default value.



For the CE6820H, CE6863H-K, CE6881H and CE6881H-K series, the adjusted maximum CPCAR value for DHCP discovery packets is 1.5 times the default value.



**Precautions**

This function takes effect only when the default CPCAR values of protocol packets are not manually modified.After adaptive CPCAR adjustment for protocol packets is enabled globally, this function takes effect for all supported types of protocol packets.


Example
-------

# Enable adaptive CPCAR adjustment for ARP request packets.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend dynamic-adjust packet-type arp-request enable

```
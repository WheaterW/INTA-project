reset ipv6 routing-table statistics protocol (User view)
========================================================

reset ipv6 routing-table statistics protocol (User view)

Function
--------



The **reset ipv6 routing-table statistics protocol** command clears statistics in the IPv6 routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 routing-table all-vpn-instance statistics protocol** { **all** | **bgp** | **direct** | **isis** | **ospfv3** | **ripng** | **static** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears the statistics of all IPv6 routing protocols in the routing table. | - |
| **bgp** | Clears the statistics of bgp route. | - |
| **direct** | Clears the statistics of direct route. | - |
| **isis** | Clears the statistics of isis route. | - |
| **ospfv3** | Clears the statistics of ospfv3 route. | - |
| **ripng** | Clears the statistics of ripng route. | - |
| **static** | Clears the statistics of static route. | - |
| **all-vpn-instance** | Clears the statistics in the IPv6 routing tables of all VPN instances. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The reset ipv6 routing-table statistics protocol command clears historical statistics about protocol routes in the IPv6 routing table. This command enables the device to re-collect statistics about protocol routes, facilitating route monitoring and fault location.

**Precautions**

Statistics in the IPv6 routing table cannot be restored after you clear them. Therefore, exercise caution when running the command.


Example
-------

# Clear the statistics in the IPv6 routing tables of all VPN instances.
```
<HUAWEI> reset ipv6 routing-table all-vpn-instance statistics protocol all

```
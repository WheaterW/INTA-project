vxlan (ECMP load balancing view)
================================

vxlan (ECMP load balancing view)

Function
--------



The **vxlan** command configures a load balancing mode for VXLAN packets in a load balancing profile.

The **undo vxlan** command deletes the load balancing mode of VXLAN packets in a load balancing profile or restores the default load balancing mode of VXLAN packets in a load balancing profile.



For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM and CE8851K, load balancing is performed based on the inner 5-tuple of VXLAN packets by default.

For other products, by default, tunnel packets are load balanced based on outer src-ip, dst-ip, l4-src-port and l4-dst-port.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan** { **inner-src-ip** | **inner-dst-ip** | **inner-l4-sport** | **inner-l4-dport** | **inner-protocol** | **src-interface** | **vni** } \*

**undo vxlan** { **inner-src-ip** | **inner-dst-ip** | **inner-l4-sport** | **inner-l4-dport** | **inner-protocol** | **src-interface** | **vni** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inner-src-ip** | Performs load balancing based on the inner source IP address. | - |
| **inner-dst-ip** | Performs load balancing based on the inner destination IP address. | - |
| **inner-l4-sport** | Performs load balancing based on the inner transport-layer source port. | - |
| **inner-l4-dport** | Performs load balancing based on the inner transport-layer destination port. | - |
| **inner-protocol** | Performs load balancing based on the inner transport-layer protocol. | - |
| **src-interface** | Performs load balancing based on the source interface. | - |
| **vni** | Performs load balancing based on the vni. | - |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

For vxlan packets, hash load sharing is performed according to the specified hash factor to meet the customer's ecmp load sharing requirements in the vxlan tunnel scenario.


Example
-------

# Configure load balancing based on the inner source IP address of VXLAN packets.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] vxlan inner-src-ip

```
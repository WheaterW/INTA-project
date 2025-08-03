ip-tunnel(ECMP load balancing view)
===================================

ip-tunnel(ECMP load balancing view)

Function
--------



The **ip-tunnel** command configures the load balancing mode of tunnel packets.

The **undo ip-tunnel** command restores the default load balancing mode of tunnel packets.



For the CE8855, CE6885, CE6885-T, and CE6885-LL in common forwarding mode and the CE6885-SAN and CE6885-LL in low-latency mode:

By default, tunnel packets are load balanced based on outer src-ip, dst-ip, l4-src-port, and l4-dst-port.

For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, CE8851K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

By default, tunnel packets are load balanced based on the inner inner-src-ip, inner-dst-ip, inner-l4-sport, and inner-l4-dport.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ip-tunnel** { **inner-src-ip** | **inner-dst-ip** | **inner-l4-sport** | **inner-l4-dport** | **inner-protocol** | **src-interface** | **include-erspan** } \*

**undo ip-tunnel** { **inner-src-ip** | **inner-dst-ip** | **inner-l4-sport** | **inner-l4-dport** | **inner-protocol** | **src-interface** | **include-erspan** } \*

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**ip-tunnel** { **inner-src-ip** | **inner-dst-ip** | **inner-l4-sport** | **inner-l4-dport** | **src-mac** | **dst-mac** } \*

**undo ip-tunnel** { **inner-src-ip** | **inner-dst-ip** | **inner-l4-sport** | **inner-l4-dport** | **src-mac** | **dst-mac** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inner-src-ip** | Performs load balancing based on the inner source IP address. | - |
| **inner-dst-ip** | Performs load balancing based on the inner destination IP address. | - |
| **inner-l4-sport** | Performs load balancing based on the inner transport-layer source port. | - |
| **inner-l4-dport** | Performs load balancing based on the inner transport-layer destination port. | - |
| **inner-protocol** | Performs load balancing based on the inner transport-layer protocol.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **src-interface** | Performs load balancing based on the source interface.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **include-erspan** | Performs load balancing based on the source IP address, destination IP address, source port, and destination port of ERSPAN inner packets.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **src-mac** | Performs load balancing based on the source mac.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **dst-mac** | Performs load balancing based on the destination mac.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device functions as an intermediate node of a tunnel and there is a load balancing link, you can run the ip-tunnel command to enable the device to perform load balancing based on the inner IP header fields of packets. This prevents uneven load balancing due to the use of the outer IP header for load balancing.

**Precautions**

Currently, GRE, 4over6, 6over4, VXLAN, and ERSPAN packets are supported.For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K:

* GRE, 4over6, 6over4, and VXLAN packets: Load balancing is performed based only on the inner IP header.
* ERSPAN packets: Load balancing is performed based only on the outer IP header.For the CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6863E-48S8CQ, CE6885-SAN, and CE6885-LL in low latency mode:
* Load balancing is performed based only on the inner IP header.


Example
-------

# Perform ECMP load balancing based on the inner source IP address of tunnel packets.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ip-tunnel inner-src-ip

```
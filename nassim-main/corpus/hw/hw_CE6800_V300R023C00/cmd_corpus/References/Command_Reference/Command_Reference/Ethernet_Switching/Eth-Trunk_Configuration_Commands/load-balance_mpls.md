load-balance mpls
=================

load-balance mpls

Function
--------



The **load-balance mpls** command configures a load balancing mode for MPLS packets.

The **undo load-balance mpls** command deletes the specified load balancing mode or restores the default load balancing mode of MPLS packets.



By default, MPLS packets are load balanced based on top-label and 2nd-label.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**load-balance mpls** [ **top-label** | **2nd-label** | **3rd-label** | **src-ip** | **dst-ip** | **src-interface** | **src-mac** | **dst-mac** | **l4-src-port** | **l4-dst-port** | **protocol** ] \*

**undo load-balance mpls** { **top-label** | **2nd-label** | **3rd-label** | **src-ip** | **dst-ip** | **src-interface** | **src-mac** | **dst-mac** | **l4-src-port** | **l4-dst-port** | **protocol** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **top-label** | Performs load balancing based on top labels. | - |
| **2nd-label** | Performs load balancing based on second labels. | - |
| **3rd-label** | Performs load balancing based on third labels. | - |
| **src-ip** | Performs load balancing based on the source IP address. | - |
| **dst-ip** | Performs load balancing based on the destination IP address. | - |
| **src-interface** | Performs load balancing based on the inbound interface. | - |
| **src-mac** | Performs load balancing based on the source MAC address. | - |
| **dst-mac** | Performs load balancing based on the destination MAC address. | - |
| **l4-src-port** | Performs load balancing based on the transport-layer source port number. | - |
| **l4-dst-port** | Performs load balancing based on the transport-layer destination port number. | - |
| **protocol** | Performs load balancing based on the protocol type. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, a device performs load balancing on MPLS packets based on their top label and second label. You can run the **load-balance mpls** command to enable the device to obtain specified fields from MPLS packets for hash calculation to achieve even load balancing.


Example
-------

# Configure Eth-Trunk 1 to perform load balancing for MPLS packets based on 2nd-label.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] load-balance mpls 2nd-label

```
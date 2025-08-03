load-balance ip
===============

load-balance ip

Function
--------



The **load-balance ip** command configures a load balancing mode for IP packets.

The **undo load-balance ip** command deletes the specified load balancing mode or restores the default load balancing mode for IP packets.



By default, IP packets are load balanced based on session-id, dest-qp, src-ip, dst-ip, l4-src-port, and l4-dst-port.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**load-balance ip** [ **src-ip** | **dst-ip** | **l4-src-port** | **l4-dst-port** | **protocol** | **src-mac** | **dst-mac** | **flowlabel** | **src-interface** | **dest-qp** | **session-id** ] \*

**undo load-balance ip** [ **src-ip** | **dst-ip** | **l4-src-port** | **l4-dst-port** | **protocol** | **src-mac** | **dst-mac** | **flowlabel** | **src-interface** | **dest-qp** | **session-id** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** | Performs load balancing based on the source IP address. | - |
| **dst-ip** | Performs load balancing based on the destination IP address. | - |
| **l4-src-port** | Performs load balancing based on the transport-layer source port number. | - |
| **l4-dst-port** | Performs load balancing based on the transport-layer destination port number. | - |
| **protocol** | Performs load balancing based on the protocol type. | - |
| **src-mac** | Performs load balancing based on the source MAC address. | - |
| **dst-mac** | Performs load balancing based on the destination MAC address. | - |
| **flowlabel** | Performs load balancing based on the flow label. | - |
| **src-interface** | Performs load balancing based on the inbound interface. | - |
| **dest-qp** | Performs load balancing based on the dest-qp of RoCEv2 packets. | - |
| **session-id** | Performs load balancing based on session IDs of PPPoE packets. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device performs load balancing based on session-id, dest-qp, src-ip, dst-ip, l4-src-port, and l4-dst-port after receiving IP packets. You can run the **load-balance ip** command to enable the device to extract related fields from IP packets and perform the hash operation to implement even load balancing.

**Precautions**

If you run the **load-balance ip** command multiple times, only the latest configuration takes effect.


Example
-------

# Configure a load balancing mode for IP packets on an Eth-Trunk interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] load-balance ip dst-mac

```
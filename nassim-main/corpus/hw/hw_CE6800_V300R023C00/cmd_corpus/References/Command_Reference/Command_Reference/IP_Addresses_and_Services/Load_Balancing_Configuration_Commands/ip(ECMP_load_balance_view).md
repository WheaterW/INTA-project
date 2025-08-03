ip(ECMP load balance view)
==========================

ip(ECMP load balance view)

Function
--------



The **ip** command sets a load balancing mode for IP packets in ECMP.

The **undo ip** command restores the default load balancing mode for IP packets in ECMP.



By default, IP packets are balanced based on src-ip, dst-ip, l4-src-port, and l4-dst-port.


Format
------

**ip** { **src-ip** | **dst-ip** | **vlan** | **l4-src-port** | **l4-dst-port** | **protocol** | **flow-label** | **src-interface** } \*

**undo ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** | Performs load balancing based on source IP addresses in IP packets. | - |
| **dst-ip** | Performs load balancing based on destination IP addresses in IP packets. | - |
| **vlan** | Performs load balancing based on VLAN IDs in IP packets. | - |
| **l4-src-port** | Performs load balancing based on transport-layer source port numbers in IP packets. | - |
| **l4-dst-port** | Performs load balancing based on transport-layer destination port numbers in IP packets. | - |
| **protocol** | Performs load balancing based on protocols in IP packets. | - |
| **flow-label** | Performs load balancing based on flow labels in IP packets. | - |
| **src-interface** | Performs load balancing based on physical source port numbers in IP packets. | - |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

IP packets that are not transmitted over tunnels are balanced based on any combination of a source IP address, destination IP address, VLAN ID, transport-layer source interface, transport-layer destination interface, protocol, flow label, and physical source interface. This meets ECMP load balancing requirements for service traffic outside tunnels.


Example
-------

# Perform ECMP load balancing on IP packets based on the source IP address and protocol number.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] ip src-ip protocol

```
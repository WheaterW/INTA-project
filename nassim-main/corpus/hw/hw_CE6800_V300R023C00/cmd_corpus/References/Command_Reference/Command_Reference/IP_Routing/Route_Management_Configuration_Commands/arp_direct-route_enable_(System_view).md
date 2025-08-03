arp direct-route enable (System view)
=====================================

arp direct-route enable (System view)

Function
--------



The **arp direct-route enable** command advertises ARP Vlink direct routes.

The **undo arp direct-route enable** command restores the default setting.



By default, ARP Vlink direct routes are not advertised.


Format
------

**arp direct-route enable**

**undo arp direct-route enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, devices on a network with VLANs use VLANIF interfaces to forward packets because these devices cannot generate IPv4 ARP Vlink direct routes. However, direct routes of VLAN users are required in some scenarios. For example, a device needs to apply a unique export policy for each VLAN user to import traffic from remote devices. In this scenario, the device obtains information about the Layer 3 interfaces using ARP and generates relevant routing entries for traffic forwarding.



**Follow-up Procedure**



Import advertised ARP Vlink direct routes to the routing table of each dynamic routing protocol on the device so that the ARP Vlink direct routes can be advertised by each dynamic routing protocol.




Example
-------

# Advertise ARP Vlink direct routes.
```
<HUAWEI> system-view
[*HUAWEI] arp direct-route enable

```
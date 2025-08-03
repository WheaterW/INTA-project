arp direct-route enable
=======================

arp direct-route enable

Function
--------



The **arp direct-route enable** command advertises ARP Vlink direct routes.

The **undo arp direct-route enable** command restores the default setting.



By default, ARP Vlink direct routes are not advertised.


Format
------

**arp direct-route enable** [ **route-policy** *name* ]

**undo arp direct-route enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *name* | Specifies the name of a route-policy that is used to filter ARP Vlink direct routes. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, ARP Vlink direct routes are only used for packet forwarding in the same VLAN and cannot be imported to dynamic routing protocols. This is because importing Vlink direct routes to dynamic routing protocols will increase the number of routing entries and affect routing table stability. In some cases, some operations need to be performed based on Vlink direct routes of VLAN users. For example, different VLAN users use different route exporting policies to guide traffic from the remote device. In this scenario, ARP Vlink direct routes are needed to be imported by a dynamic routing protocol and advertised to the remote device. After advertisement of ARP Vlink direct routes is enabled, these direct routes can be imported by a dynamic routing protocol (IGP or BGP) and advertised to the remote device.

**Configuration Impact**

After route-policy route-policy-name is specified in the arp direct-route enable command, only filtered ARP Vlink direct routes are advertised.

**Follow-up Procedure**

Import advertised ARP Vlink direct routes to the routing table of each dynamic routing protocol on the device so that the ARP Vlink direct routes can be advertised by each dynamic routing protocol.

**Precautions**

Route-policies can filter ARP Vlink direct routes only based on IPv4 or IPv6 route prefixes.Route-policy must be specified using the **route-policy** command. If the parameter is not specified, ARP Vlink direct routes cannot be filtered.


Example
-------

# Enable a VLANIF interface to advertise the ARP Vlink direct routes matching the route-policy named rp1 only when the corresponding ARP virtual IP address is obtained by ARP through probing based on learned ARP entries in an EVN scenario.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-Vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-Vlanif200] arp direct-route enable route-policy rp1

```
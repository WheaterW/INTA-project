import route-policy (VPN instance view)
=======================================

import route-policy (VPN instance view)

Function
--------



The **import route-policy** command associates the current VPN instance IPv4 address family with an import route-policy.

The **undo import route-policy** command disassociates the current VPN instance IPv4 address family from an import route-policy.



By default, the current VPN instance IPv4 address family is not associated with any import route-policy.


Format
------

**import route-policy** *policy-name*

**undo import route-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of the import route-policy to be associated with a VPN instance IPv4 address family. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no import route-policy is configured, the routes to be imported into the VPN instance IPv4 address family can be filtered only based on the export VPN targets of the routes and the import VPN targets of the VPN instances. To control the import of the routes into the VPN instance IPv4 address family more precisely, use an import route-policy. An import route-policy can filter the routes imported by the VPN instance IPv4 address family and set the attributes for routes that pass the filtering. Routes are filtered based on their export VPN targets and the import VPN targets of the VPN instance and then based on the import route-policy.The **import route-policy** command controls route leaking from the BGP-VPNv4 address family into a VPN instance. The peer route-policy or filter-policy configured in the BGP VPN instance IPv4 address family view filters the routes in the VPN instance IPv4 address family advertised to or received from CE peers.

**Prerequisites**



If the import route-policy to be associated with a VPN instance IPv4 address family does not exist, configure the import route-policy first.



**Configuration Impact**



The current VPN instance IPv4 address family can be associated with only one import route-policy. If the **import route-policy** command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Apply an import route-policy named poly-1 to the IPv4 address family of the VPN instance named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] route-policy poly-1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] import route-policy poly-1

```
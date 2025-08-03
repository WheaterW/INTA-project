export route-policy (VPN instance view)
=======================================

export route-policy (VPN instance view)

Function
--------



The **export route-policy** command associates the current VPN instance IPv4 address family with an export route-policy.

The **undo export route-policy** command disassociates the current VPN instance IPv4 address family from the export route-policy.



By default, the current VPN instance IPv4 address family is not associated with any export route-policy.


Format
------

**export route-policy** *policy-name* [ **add-ert-first** ]

**undo export route-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of the export route-policy to be associated with the VPN instance IPv4 address family. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **add-ert-first** | Adds ERTs to VPN routes before these routes are matched against an export routing policy. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To advertise the routes of a VPN instance IPv4 address family in a way more precise than the way based on the extended community attribute, use the export route-policy. An export route-policy can filter routes advertised by the VPN instance IPv4 address family and set the attributes for routes that pass the filtering.The **export route-policy** command controls the advertisement of local routes from the VPN instance IPv4 address family to the BGP-VPNv4 address family. The peer route-policy or filter-policy command run in the BGP VPN instance IPv4 address family view filters the routes in the VPN instance IPv4 address family advertised to or received from CE peers.By default, export VPN targets are added to VPN routes after these routes are matched against an export route-policy. If the export route-policy contains VPN target-related filtering rules, it cannot apply to VPN routes. If you want to apply the VPN target-related filtering rules defined in an export route-policy to VPN routes, configure the add-ert-first parameter for the device to add export VPN targets to VPN routes before matching these routes against the export route-policy.In local route leaking scenarios, you can run the **export route-policy** command to filter out locally leaked routes and set the attributes of these routes. Locally leaked routes include locally imported routes and routes learned from VPN peers.

**Prerequisites**



If the export route-policy to be associated with a VPN instance IPv4 address family does not exist, configure the export route-policy first.



**Configuration Impact**



The current VPN instance IPv4 address family can be associated with only one export route-policy. If the **export route-policy** command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Apply an export route-policy named poly-1 to the IPv4 address family of the VPN instance named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] route-policy poly-1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] export route-policy poly-1

```
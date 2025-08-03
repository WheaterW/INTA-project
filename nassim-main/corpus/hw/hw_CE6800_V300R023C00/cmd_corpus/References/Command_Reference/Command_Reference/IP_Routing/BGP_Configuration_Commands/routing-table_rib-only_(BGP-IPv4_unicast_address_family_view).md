routing-table rib-only (BGP-IPv4 unicast address family view)
=============================================================

routing-table rib-only (BGP-IPv4 unicast address family view)

Function
--------



The **routing-table rib-only** command prohibits BGP routes from being added to the IP routing table.

The **undo routing-table rib-only** command restores the default configuration.



By default, the preferred BGP routes are added to the IP routing table.


Format
------

**routing-table rib-only** [ **route-policy** *route-policy-name* ]

**undo routing-table rib-only**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a route reflector (RR) is used and preferred BGP routes do not need to be used during the forwarding, the **routing-table rib-only** command can be used to make BGP routes unable to be added to the IP routing table or the forwarding layer. This improves forwarding efficiency and the system capacity.When route-policy-name is specified in the command, the routes matching the policy are not added to the IP routing table, and the routes not matching the policy are added to the IP routing table.

**Configuration Impact**



After the **routing-table rib-only** command is run, the routes preferred by BGP are not added to the IP routing table.



**Precautions**



The **routing-table rib-only** command and the **active-route-advertise** command are mutually exclusive.




Example
-------

# Prohibit BGP routes from being advertised to the IP routing table.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] routing-table rib-only

```
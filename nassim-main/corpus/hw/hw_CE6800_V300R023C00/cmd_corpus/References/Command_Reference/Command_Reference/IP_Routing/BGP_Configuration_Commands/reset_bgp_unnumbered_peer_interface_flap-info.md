reset bgp unnumbered peer interface flap-info
=============================================

reset bgp unnumbered peer interface flap-info

Function
--------



The **reset bgp unnumbered peer interface flap-info** command clears the statistics of BGP route flapping of BGP unnumbered peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **flap-info**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset bgp ipv6 unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **flap-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **ipv6** | Indicates the IPv6 unicast address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The process of adding a route to and then deleting the route from a routing table is called route flapping.When route flapping occurs, the routing protocol sends Update messages to peers. The peers that receive the Update messages need to recalculate routes and modify its routing table. Frequent route flapping consumes extensive bandwidth and CPU resources and can even affect network operations.You can run the **reset bgp unnumbered peer interface flap-info** command to clear the flapping statistics about BGP routes of unnumbered peer. This allows the device to re-collect statistics about flapping routes, which helps you monitor route changes and locate network faults.

**Prerequisites**

You can use **display bgp routing-table flap-info** command to view the information about BGP route flapping.If there are a large number of flapping routes, you can define as-path-filter or regexp, and then clear the statistics of the matched flapping routes.

**Configuration Impact**

After the **reset bgp unnumbered peer interface flap-info** command is run, route flapping statistics are cleared and cannot be displayed.

**Follow-up Procedure**

After the flapping statistics of routes are cleared, run the **display bgp routing-table flap-info** command again to display the flapping statistics about BGP routes in order to locate problems.


Example
-------

# Clear the flapping statistics about the routes of BGP unnumbered peers.
```
<HUAWEI> reset bgp unnumbered peer interface 100GE 1/0/1 flap-info

```
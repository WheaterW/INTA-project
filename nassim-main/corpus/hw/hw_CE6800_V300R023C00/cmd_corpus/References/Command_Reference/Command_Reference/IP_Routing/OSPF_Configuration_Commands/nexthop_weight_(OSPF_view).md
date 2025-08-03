nexthop weight (OSPF view)
==========================

nexthop weight (OSPF view)

Function
--------



The **nexthop weight** command sets a priority for equal-cost routes. After OSPF calculates the equal-cost routes, the next hop is chosen from these equal-cost routes based on the priority value. The smaller the value, the higher the priority.

The **undo nexthop** command cancels the priority of equal-cost routes.



By default, the value of weight-value is 255, and equal-cost routes load balance traffic.


Format
------

**nexthop** *ip-address* **weight** *value*

**undo nexthop** *ip-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of the next hop. | The value is in dotted decimal notation. |
| *value* | Specifies a priority for the next hop. The smaller the value, the higher the priority. | The value is an integer that ranges from 1 to 254. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the number of equal-cost routes on the network is greater than the value specified using the **maximum load-balancing** command and you need to specify valid routes for load balancing, run the **nexthop weight** command to set a higher priority for the valid routes to be specified.


Example
-------

# Set the priority of equal-cost routes in OSPF.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] nexthop 10.0.0.3 weight 1

```
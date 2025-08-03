nexthop weight (OSPFv3 view)
============================

nexthop weight (OSPFv3 view)

Function
--------



The **nexthop weight** command sets the priority for equal-cost routes.

The **undo nexthop** command cancels the priority of equal-cost routes.



By default, the value of weight-value is 255, and equal-cost routes load balance traffic.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nexthop** *neighbor-id* { *interface-name* | *interface-type* *interface-number* } **weight** *value*

**undo nexthop** *neighbor-id* { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *neighbor-id* | Specifies the router ID of a neighbor. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | - |
| **weight** *value* | Specifies a priority for the next hop. The smaller the value, the higher the priority. | The value is an integer that ranges from 1 to 254. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the number of equal-cost routes on the network is greater than the value specified using the **maximum load-balancing** command and you need to specify valid routes for load balancing, run the **nexthop weight** command to set a higher priority for the valid routes to be specified.


Example
-------

# Set the priority for OSPFv3 equal-cost routes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] nexthop 10.0.0.3 100GE1/0/1 weight 1

```
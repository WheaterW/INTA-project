nexthop weight (IS-IS view)
===========================

nexthop weight (IS-IS view)

Function
--------



The **nexthop weight** command sets the preference for equal-cost routes.

The **undo nexthop** command deletes the configured priority.



By default, no weight is set for equal-cost routes, and IS-IS forwards packets in load balancing mode.


Format
------

**nexthop** *ip-address* **weight** *value*

**undo nexthop** *ip-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of the next hop. | The value is in dotted decimal notation. |
| **weight** *value* | Specifies a priority. | The value is an integer ranging from 1 to 254. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When there are multiple redundant links on an IS-IS network, multiple equal-cost routes may exist. That is, there are multiple equal-cost paths to a destination network segment.You can run the **nexthop ip-address weight** command to set a weight for the next hop so that the next hop can be specified without changing the interface cost. The smaller the weight value, the higher the priority.

**Prerequisites**

IS-IS processes have been enabled, and the IS-IS routing table contains multiple equal-cost routes.

**Configuration Impact**

After the nexthop command is run, an IS-IS device does not forward traffic in load balancing mode to a specific destination network segment, but forwards traffic to the next hop with the highest priority.


Example
-------

# In an IS-IS process, set the weight of the next hop of the equal-cost route with the IP address 10.0.0.3 to 1.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] nexthop 10.0.0.3 weight 1

```
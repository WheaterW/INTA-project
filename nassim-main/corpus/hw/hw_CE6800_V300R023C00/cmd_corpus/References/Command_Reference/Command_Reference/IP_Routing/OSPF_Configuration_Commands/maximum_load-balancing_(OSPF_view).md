maximum load-balancing (OSPF view)
==================================

maximum load-balancing (OSPF view)

Function
--------

By default, load balancing is supported. For details about the maximum number of equal-cost routes, see the parameter value range.


Format
------

**maximum load-balancing** *number*

**undo maximum load-balancing**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of equal-cost routes. | The value is an integer that ranges from 1 to 128. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple routes with the same cost to the same destination are available, they can carry out load balancing. The **maximum load-balancing** command sets the maximum number of equal-cost routes for carrying out load balancing. This optimizes route selection rules and meet traffic forwarding requirements on a complex network.

**Configuration Impact**



Packets will be load-balanced by multiple equal-cost routes to one destination.

Load balancing is performed either per-destination or per-packet. By default, packets are load-balanced per-destination.The **undo maximum load-balancing** command restores the default equal-cost routes that are discovered by OSPF for load balancing.



**Follow-up Procedure**

If the number of equal-cost routes on the network is greater than the value specified using the **maximum load-balancing** command and you need to specify valid routes for load balancing, run the **nexthop ip-address weight value** command to set weights for the routes to increase the priority of the valid routes to be specified.

**Precautions**

To disable load balancing, set the value of number to 1.


Example
-------

# Set the maximum number of the equal-cost routes.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] maximum load-balancing 2

```

# Restore the default maximum number of equal-cost routes for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] undo maximum load-balancing

```
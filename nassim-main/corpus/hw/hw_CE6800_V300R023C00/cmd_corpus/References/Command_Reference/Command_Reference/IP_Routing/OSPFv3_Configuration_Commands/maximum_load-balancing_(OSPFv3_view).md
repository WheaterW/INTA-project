maximum load-balancing (OSPFv3 view)
====================================

maximum load-balancing (OSPFv3 view)

Function
--------

By default, load balancing is supported. For details about the maximum number of equal-cost routes, see the parameter value range.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple routes with the same cost to the same destination are available, they can carry out load balancing. The **maximum load-balancing** command sets the maximum number of equal-cost routes for carrying out load balancing. This optimizes route selection rules and meet traffic forwarding requirements on a complex network.

**Configuration Impact**

Packets will be load-balanced by multiple equal-cost routes to one destination.NOTE:Load balancing is performed either per-destination or per-packet. By default, packets are load-balanced per-destination.The **undo maximum load-balancing** command restores the default maximum number of 32 equal-cost routes that are discovered by OSPFv3 for load balancing.

**Precautions**

To disable load balancing, set the value of number to 1.


Example
-------

# Set the maximum number of equal-cost routes supported by OSPFv3 to 3.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] maximum load-balancing 3

```

# Restore the default maximum number of equal-cost routes for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] undo maximum load-balancing

```
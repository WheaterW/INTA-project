maximum load-balancing (IS-IS view)
===================================

maximum load-balancing (IS-IS view)

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
| *number* | Specifies the number of equal-cost routes in load balancing mode. | The value is an integer. The value ranges from 1 to 128. The default value is 128. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the destinations and costs of the multiple routes discovered by one routing protocol are the same, load balancing can be implemented among them, improving link usage on a network and reducing the network congestion caused by some overloaded links. However, routes are randomly selected for forwarding traffic, which complicates service traffic management. To address this problem, run the **maximum load-balancing** command to set the maximum number of equal-cost routes for load balancing based on network requirements.

**Precautions**

When the number of equal-cost routes on the network is greater than the value specified in the **maximum load-balancing** command, valid routes are selected for load balancing according to the following rules:

1. Route weight: Routes with small weight values (high priority) are selected for load balancing.
2. Next-hop system ID: If routes have the same weight, those with small system IDs are selected for load balancing.
3. Outbound interface index: If routes have the same weight and system ID, those with small outbound interface indexes are selected for load balancing.
4. Next-hop IP address: If the weights, next-hop system IDs, and interface indexes of the routes are the same, their next-hop IP addresses are compared. The routes with high IP addresses are selected for load balancing.

Example
-------

# Set the maximum number of equal-cost routes for load balancing to 2.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] maximum load-balancing 2

```

# Restore the default value for the maximum number of equal-cost routes.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] undo maximum load-balancing

```
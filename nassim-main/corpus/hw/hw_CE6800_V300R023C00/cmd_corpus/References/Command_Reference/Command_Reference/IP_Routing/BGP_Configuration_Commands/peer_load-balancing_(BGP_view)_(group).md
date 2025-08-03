peer load-balancing (BGP view) (group)
======================================

peer load-balancing (BGP view) (group)

Function
--------

By default, BGP load balancing is not enabled.


Format
------

**peer** *group-name* **load-balancing** [ **as-path-ignore** | **as-path-relax** ]

**undo peer** *group-name* **load-balancing** [ **as-path-ignore** | **as-path-relax** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **as-path-ignore** | Prevents the device from comparing the AS\_Path attributes of routes when selecting routes for load balancing. | - |
| **as-path-relax** | Prevents the device from comparing the AS\_Path attributes of the same length when selecting routes for load balancing. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large-scale network, there may be multiple valid routes to the same destination, but BGP advertises only the optimal route to its peers. This may cause unbalanced traffic load. This section describes how to configure BGP load balancing to implement load balancing among multiple BGP routes.After the **peer load-balancing** command is run, the following conditions must be met to implement load balancing:

* The routes are learned from the specified peer group.
* The route is the optimal route or equal-cost route with the optimal route.
* If the AS\_Path attribute is the same as that of the optimal route or the *as-path-ignore*or *as-path-relax*parameter is configured for the peer when load balancing is enabled on the peer:*as-path-ignore*: ignores the AS\_Path attribute and does not compare the AS\_Path attributes of the routes to be used for load balancing. That is, load balancing can be implemented even if the AS\_Path attributes of the routes are different.*as-path-relax*: The device ignores the AS\_Path attributes of the same length and does not compare the AS\_Path attributes of the same length when load balancing is performed among the routes. That is, load balancing cannot be performed among the routes with different AS\_Path lengths. For example, the AS\_Path attribute of route A is 10, and the AS\_Path attribute of route B is 10 20. Because the AS\_Path lengths of the two routes are different, load balancing cannot be implemented.

**Precautions**

The maximum load-balancing and **peer load-balancing** commands are mutually exclusive.By default, a BGP device does not change the next hop addresses of routes to a local address before sending the routes to its IBGP peer. However, after peer-based load balancing is enabled, a BGP device changes the next hop addresses of routes to a local address before sending the routes to its IBGP peer.If the **load-balancing as-path-ignore** or **load-balancing as-path-relax** command is run but the **peer load-balancing** command does not contain the *as-path-ignore*or *as-path-relax*parameter, the **load-balancing as-path-ignore** or **load-balancing as-path-relax** configuration takes effect. If *as-path-ignore*or *as-path-relax*is specified in the **peer load-balancing** command, the configuration specified in the **peer load-balancing** command takes effect.Running the load-balancing as-path-ignore or load-balancing as-path-relax command may cause BGP routing loops.


Example
-------

# Enable load balancing among routes learned from peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test load-balancing as-path-relax

```
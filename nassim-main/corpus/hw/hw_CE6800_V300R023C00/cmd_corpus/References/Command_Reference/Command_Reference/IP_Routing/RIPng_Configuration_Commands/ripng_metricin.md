ripng metricin
==============

ripng metricin

Function
--------



The **ripng metricin** command sets the metric that is added to the RIPng routes received by an interface.

The **undo ripng metricin** command restores the default setting.



By default, the metric that is added to received routes is 0.


Format
------

**ripng metricin** *value*

**undo ripng metricin**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the metric that is added to received routes. | The value is an integer in the range 0 to 15. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If there are multiple routes that perform load balancing and are destined for the same destination in the routing table, you can run the ripng metricin command to change the route metric locally. After the command is run, the routing entries in the routing table change accordingly.

**Configuration Impact**

When an interface receives a route, RIPng adds the interface metric to the route, and then adds the route to the routing table. Therefore, increasing the interface metric also increases the metric of the RIPng route received by the interface.


Example
-------

# Set the metric that is added to received routes to 12.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng metricin 12

```
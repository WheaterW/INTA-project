timers ripng
============

timers ripng

Function
--------



The **timers ripng** command sets the values of RIPng timers.

The **undo timers ripng** command restores the default setting.



By default, RIPng timers use default values after RIP processes are enabled.


Format
------

**timers ripng** *update* *age* *suppress* *garbage-collect*

**undo timers ripng**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *update* | Specifies the interval at which Update packets are sent. It is the basic timing parameter of the routing protocol. | The value is an integer ranging from 1 to 86400, in seconds. The default value is 30 seconds. |
| *age* | Specifies the period after which a RIPng route becomes invalid. The value must be at least three times the value of update. If no Update packet of a route is received within age, the route becomes invalid (unreachable). | The value is an integer ranging from 1 to 86400, in seconds. The default value is 180 seconds. |
| *suppress* | Specifies the period during which the optimal route is suppressed from being advertised. | The value is an integer ranging from 0 to 86400, in seconds. The default value is 0 seconds. |
| *garbage-collect* | Specifies the period from the time when the suppression timer times out and the time when the route is deleted from the routing table. | The value is an integer ranging from 1 to 86400, in seconds. The default value is 120 seconds. |



Views
-----

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the values of RIPng timers, run this command, which improves the routing protocol performance.The relationship between the timers is as follows: update<age, suppress<garbage-collect. For example, if the value of the update timer is greater than the value of the age timer, a device cannot inform its neighbors of the changes of RIPng routes on time within the update time.

**Precautions**

If the values of the four timers are set improperly, routes will become unstable, and route convergence will slow down. Generally, the four timers adopt the default values.


Example
-------

# Set values for RIPng timers.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100
[*HUAWEI-ripng-100] timers ripng 5 15 0 30

```
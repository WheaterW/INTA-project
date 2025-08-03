timers rip
==========

timers rip

Function
--------



The **timers rip** command adjusts timers.

The **undo timers rip** command restores the default values.



By default, timers adopt default values.


Format
------

**timers rip** *update* *age* *suppress* *garbage-collect*

**undo timers rip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *update* | Specifies the interval at which Update packets are sent. | The value is an integer ranging from 1 to 86400, in seconds. The default value is 30 seconds. |
| *age* | Specifies the aging time of a route. | The value is an integer ranging from 1 to 86400, in seconds. The default value is 180 seconds. |
| *suppress* | Specifies the period in which the optimal route is suppressed from being advertised. | The value is an integer ranging from 0 to 86400, in seconds. The default value is 0 seconds. |
| *garbage-collect* | Specifies the time for deleting a route from the routing table (the garbage collection time defined in the standard). | The value is an integer ranging from 1 to 86400, in seconds. The default value is 120. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By adjusting the RIP timers, you can improve routing protocol performance to meet network requirements.The relationship between the times is as follows: update<age, suppress<garbage-collect. For example, if the value of the update timer is larger than that of the age timer, a device cannot inform its neighbors of RIP route changes in time during the update time.

**Precautions**

If the values of the four timers are set improperly, routes will become unstable, and route convergence will slow down. Generally, the four timers adopt the default values.


Example
-------

# Set the value for each RIP timer.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-1] timers rip 60 180 0 120

```
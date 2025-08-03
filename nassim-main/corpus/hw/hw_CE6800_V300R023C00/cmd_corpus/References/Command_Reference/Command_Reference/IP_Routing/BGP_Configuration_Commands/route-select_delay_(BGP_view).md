route-select delay (BGP view)
=============================

route-select delay (BGP view)

Function
--------



The **route-select delay** command configures a route selection delay.

The **undo route-select delay** command deletes the configured route selection delay.



The default delay-value value is 0, indicating that route selection is not delayed.


Format
------

**route-select delay** *delay-value*

**undo route-select delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-value* | Specifies a route selection delay. | The value is an integer that ranges from 0 to 3600, in seconds. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a scenario in which primary and backup routes exist, packets may get lost after traffic switches back to the primary path from the backup path.You can run the **route-select delay** command to configure a route selection delay. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the device on the primary link completes refreshing forwarding entries.

**Precautions**

If you run the **route-select delay** command more than once, the latest configuration overrides the previous one. If a route selection delay is reconfigured and the delay timer has started, the new delay takes effect immediately.Delayed route selection is valid only for the routes received from peers. If a new route is locally imported, delayed route selection is not performed for it.If a route changes, but it does not meet the route selection delay conditions, and the route has the same prefix as other routes that are in delayed route selection, the latter routes exit delayed route selection and participate in route selection immediately.


Example
-------

# Set the route selection delay to 300s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] route-select delay 300

```
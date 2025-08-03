route-select delay (BGP-IPv6 unicast address family view)
=========================================================

route-select delay (BGP-IPv6 unicast address family view)

Function
--------



The **route-select delay** command configures a route selection delay.

The **undo route-select delay** command deletes the configured route selection delay.



The default delay-value value is 0, indicating that route selection is not delayed.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

BGP-IPv6 unicast address family view


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
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] route-select delay 300

```
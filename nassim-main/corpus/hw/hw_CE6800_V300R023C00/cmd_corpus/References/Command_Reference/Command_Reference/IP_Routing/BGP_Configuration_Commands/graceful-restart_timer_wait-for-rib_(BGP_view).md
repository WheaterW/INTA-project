graceful-restart timer wait-for-rib (BGP view)
==============================================

graceful-restart timer wait-for-rib (BGP view)

Function
--------



The **graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from each peer.

The **undo graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from each peer for a maximum of 600s.


Format
------

**graceful-restart timer wait-for-rib** *time*

**undo graceful-restart timer wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag from each peer. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum duration for a BGP restarter to wait for the End-of-RIB flag from each peer, run the **graceful-restart timer wait-for-rib** command. After the BGP session between the BGP restarter and any peer is reestablished, if the BGP restarter does not receive the End-of-RIB flag from this peer within the specified duration, the BGP session on the device exits from the GR process, and the device selects the optimal route among reachable routes.

**Configuration Impact**

If the **graceful-restart timer wait-for-rib** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

If there are a large number of routes, setting time to a large value is recommended.


Example
-------

# Set the maximum duration to 100s for a BGP restarter to wait for the End-of-RIB flag from each peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] graceful-restart timer wait-for-rib 100

```
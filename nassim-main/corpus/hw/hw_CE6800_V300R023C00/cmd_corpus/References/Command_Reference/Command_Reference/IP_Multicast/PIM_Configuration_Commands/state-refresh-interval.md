state-refresh-interval
======================

state-refresh-interval

Function
--------



The **state-refresh-interval** command configures the interval at which a Router sends State-Refresh messages.

The **undo state-refresh-interval** command restores the default setting.



By default, the interval at which a Router sends Status-Refresh messages is 60s.


Format
------

**state-refresh-interval** *interval*

**undo state-refresh-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which a router sends State-Refresh messages. | The value is an integer ranging from 1 to 255, in seconds. The default value is recommended. |



Views
-----

PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-DM network, to avoid that a pruned interface restores forwarding because the prune timer expires, the first-hop Router closest to the source periodically sends State-Refresh messages. The State-Refresh messages are flooded on the entire network to refresh the prune timers on all Routers. To configure the interval at which a Router sends State-Refresh messages, run the **state-refresh-interval** command.

**Precautions**

To prevent pruned interfaces from forwarding packets after the Prune state times out, the interval at which State-Refresh messages are sent must be shorter than the period for keeping the Prune state. Run the **holdtime join-prune** command to configure the period during which a Router keeps the Prune state.


Example
-------

# In the public network instance, set the interval at which a Router sends State-Refresh messages to 70s.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] state-refresh-interval 70

```
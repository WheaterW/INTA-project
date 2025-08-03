peer graceful-restart timer wait-for-rib (BGP view)(group)
==========================================================

peer graceful-restart timer wait-for-rib (BGP view)(group)

Function
--------



The **peer graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from each peer in a specified group.

The **undo peer graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from each peer in a specified group for a maximum of 600s.


Format
------

**peer** *group-name* **graceful-restart** **timer** **wait-for-rib** *time-value*

**undo peer** *group-name* **graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *time-value* | Specifies the maximum duration for waiting for the End-Of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the local device re-establishes a BGP session with a specified peer group, the local device should receive the End-Of-RIB flag from the specified peer group within the period specified by this command. If the local device does not receive the End-Of-RIB flag within the period specified by this command, the local device exits the GR process and selects the optimal route from the existing routes.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the maximum duration during which a BGP restarter waits for the End-of-RIB flag from each peer in a specified group to 100s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group aaa
[*HUAWEI-bgp] peer aaa graceful-restart timer wait-for-rib 100

```
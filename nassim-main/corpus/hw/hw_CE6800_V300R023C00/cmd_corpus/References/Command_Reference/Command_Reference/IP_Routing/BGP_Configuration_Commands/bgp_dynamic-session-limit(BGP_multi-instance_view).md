bgp dynamic-session-limit(BGP multi-instance view)
==================================================

bgp dynamic-session-limit(BGP multi-instance view)

Function
--------



The **bgp dynamic-session-limit** command configures a maximum number for dynamic BGP peer sessions.

The **undo bgp dynamic-session-limit** command restores the default configuration.



By default, the maximum number of dynamic BGP peer sessions is 100.


Format
------

**bgp dynamic-session-limit** *limit-value*

**undo bgp dynamic-session-limit** *limit-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-value* | Specifies a maximum number for dynamic BGP peer sessions. | The value is an integer that ranges from 1 to 16000. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The dynamic BGP peer function enables BGP to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. This spares you from adding or deleting BGP peer configurations in response to each change in dynamic peers. To configure a maximum number for dynamic BGP peer sessions, run the bgp dynamic-session-limit command.



**Precautions**



If you run the command to reduce the maximum number of dynamic BGP peer sessions, the established dynamic peers are not disconnected. For example, the current max-num is 50, and 50 dynamic peers have been established. Then, max-num is changed to 20. In this case, the 50 dynamic peers are not disconnected.If the bgp dynamic-session-limit command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Set the maximum number to 20 for dynamic BGP peer sessions.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] bgp dynamic-session-limit 20

```
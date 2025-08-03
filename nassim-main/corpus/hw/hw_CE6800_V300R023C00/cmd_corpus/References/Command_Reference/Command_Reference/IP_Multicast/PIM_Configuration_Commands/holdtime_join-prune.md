holdtime join-prune
===================

holdtime join-prune

Function
--------



The **holdtime join-prune** command globally sets the holdtime for Join/Prune messages sent by PIM interfaces.

The **undo holdtime join-prune** command restores the default value.



By default, the holdtime value in Join/Prune messages sent by all PIM interfaces is 210 seconds.


Format
------

**holdtime join-prune** *interval*

**undo holdtime join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the holdtime for Join/Prune messages sent by the local router. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving a Join/Prune message from a downstream interface, an upstream router determines the time period for keeping the join or prune state of a downstream interface based on the holdtime field carried in the Join/Prune message. To set a value for the holdtime field, run the holdtime join-prune command. Generally, the holdtime is 3.5 times the interval (specified using the **timer join-prune** command) at which Join/Prune messages are sent.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the holdtime join-prune command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 280 seconds as the holdtime value in Join/Prune messages sent by all PIM interfaces.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] holdtime join-prune 280

```
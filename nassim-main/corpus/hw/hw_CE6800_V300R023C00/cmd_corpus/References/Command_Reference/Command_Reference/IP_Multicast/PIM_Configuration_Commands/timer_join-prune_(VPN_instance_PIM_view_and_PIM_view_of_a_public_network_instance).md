timer join-prune (VPN instance PIM view/PIM view of a public network instance)
==============================================================================

timer join-prune (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **timer join-prune** command globally sets an interval at which PIM interfaces send Join/Prune messages upstream.

The **undo timer join-prune** command restores the default value.



By default, all PIM interfaces send Join/Prune messages upstream at an interval of 60 seconds.


Format
------

**timer join-prune** *interval*

**undo timer join-prune**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which PIM interfaces send Join/Prune messages upstream. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a router receives a Join/Prune message, the router updates the downstream interface status to maintain the (S, G) or (\*, G) entry. To set the interval at which PIM interfaces send Join/Prune messages upstream, run the timer join-prune command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the timer join-prune command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The interval at which PIM interfaces send Join/Prune messages to an upstream neighbor must be shorter than the holdtime specified for Join/Prune messages; otherwise, the upstream neighbor times out.


Example
-------

# In the public network instance, specify 80 seconds as the interval at which PIM interfaces send Join/Prune messages upstream.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] timer join-prune 80

```
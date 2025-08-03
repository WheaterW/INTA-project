source-lifetime (VPN instance PIM view/PIM view of a public network instance)
=============================================================================

source-lifetime (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **source-lifetime** command specifies a timeout period for (S, G) entries.

The **undo source-lifetime** command restores the default value.



By default, the timeout period of (S, G) entries is 210 seconds.


Format
------

**source-lifetime** *interval*

**undo source-lifetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period for (S, G) entries. | The value is an integer ranging from 60 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Router creates a timer for each (S, G) entry. To set a timeout period for those timers, run the **source-lifetime** command. The Router starts the timer after receiving multicast packets from a multicast source for the first time. Each time the Router receives a multicast packet from the source, the Router resets the timer. If no multicast packets are received before timer times out, the (S, G) entry is considered invalid.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **source-lifetime** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The actual aging time of (S, G) entries may be longer than the set timeout period.


Example
-------

# In the public network instance, specify 200 seconds as the timeout period for (S, G) entries.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] source-lifetime 200

```
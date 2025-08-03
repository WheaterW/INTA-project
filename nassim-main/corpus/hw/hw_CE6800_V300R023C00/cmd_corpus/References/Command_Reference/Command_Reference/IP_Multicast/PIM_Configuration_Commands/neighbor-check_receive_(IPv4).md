neighbor-check receive (IPv4)
=============================

neighbor-check receive (IPv4)

Function
--------



The **neighbor-check receive** command enables a device to check whether Join/Prune and Assert messages are received from a PIM neighbor.

The **undo neighbor-check receive** command restores the default configuration.



By default, the PIM neighbor check function is not enabled.


Format
------

**neighbor-check receive**

**undo neighbor-check receive**


Parameters
----------

None

Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To improve message transmission security, run the **neighbor-check** command to enable the PIM neighbor check function. The receive and send parameters can be both specified to allow a device to check PIM neighbor information in received and sent Join/Prune and Assert messages.


Example
-------

# In the public network instance, enable the PIM neighbor check function for received Join/Prune and Assert messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] neighbor-check receive

```
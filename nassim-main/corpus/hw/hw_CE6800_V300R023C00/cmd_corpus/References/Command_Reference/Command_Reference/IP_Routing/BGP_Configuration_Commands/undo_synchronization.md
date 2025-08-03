undo synchronization
====================

undo synchronization

Function
--------



The **undo synchronization** command disables synchronization between BGP and an IGP.



By default, synchronization between BGP and an IGP is disabled.


Format
------

**undo synchronization**


Parameters
----------

None

Views
-----

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Device does not support IGP and BGP synchronization. Therefore, the **undo synchronization** command is configured by default and the configuration cannot be modified.


Example
-------

# Disable synchronization between BGP and an IGP.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] undo synchronization

```
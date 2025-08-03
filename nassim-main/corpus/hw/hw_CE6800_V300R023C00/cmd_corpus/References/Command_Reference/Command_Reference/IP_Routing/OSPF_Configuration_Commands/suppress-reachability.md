suppress-reachability
=====================

suppress-reachability

Function
--------



The **suppress-reachability** command suppresses the advertisement of all interface addresses in an OSPF process.

The **undo suppress-reachability** command restores the default setting.



By default, OSPF interfaces can advertise its addresses in the OSPF process.


Format
------

**suppress-reachability**

**undo suppress-reachability**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To suppress the advertisement of all interface addresses in an OSPF process, run the **suppress-reachability** command.


Example
-------

# Suppress the advertisement of all interface addresses in OSPF process 100.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] suppress-reachability

```
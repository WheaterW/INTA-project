suppress-flapping peer disable (OSPF view)
==========================================

suppress-flapping peer disable (OSPF view)

Function
--------



The **suppress-flapping peer disable** command disables OSPF neighbor relationship flapping suppression globally.

The **undo suppress-flapping peer disable** command enables OSPF neighbor relationship flapping suppression globally.



By default, OSPF neighbor relationship flapping suppression is enabled globally.


Format
------

**suppress-flapping peer disable**

**undo suppress-flapping peer disable**


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

If an interface carrying OSPF services alternates between Up and Down, OSPF neighbor relationship flapping occurs on the interface. During the flapping, OSPF frequently sends Hello packets to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, adversely affecting neighbor relationship stability, OSPF services, and other OSPF-dependent services, such as BGP. OSPF neighbor relationship flapping suppression can address this problem by delaying OSPF neighbor relationship reestablishment or preventing service traffic from passing through flapping links.By default, OSPF neighbor relationship flapping suppression is enabled globally. To disable this function globally, run the **suppress-flapping peer disable** command.


Example
-------

# Disable neighbor relationship flapping suppression globally.
```
<HUAWEI> system-view
[~HUAWEI] ospf
[*HUAWEI-ospf-1] suppress-flapping peer disable

```
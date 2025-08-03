suppress-flapping peer disable (OSPFv3 view)
============================================

suppress-flapping peer disable (OSPFv3 view)

Function
--------



The **suppress-flapping peer disable** command disables OSPFv3 neighbor relationship flapping suppression globally.

The **undo suppress-flapping peer disable** command enables OSPFv3 neighbor relationship flapping suppression globally.



By default, OSPFv3 neighbor relationship flapping suppression is enabled globally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**suppress-flapping peer disable**

**undo suppress-flapping peer disable**


Parameters
----------

None

Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If an interface carrying OSPFv3 services alternates between Up and Down, OSPFv3 neighbor relationship flapping occurs on the interface. During the flapping, OSPFv3 frequently sends Hello packets to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, adversely affecting neighbor relationship stability, OSPFv3 services, and other OSPFv3-dependent services, such as BGP. OSPFv3 neighbor relationship flapping suppression can address this problem by delaying OSPFv3 neighbor relationship reestablishment or preventing service traffic from passing through flapping links.By default, OSPFv3 neighbor relationship flapping suppression is enabled globally. To disable this function globally, run the **suppress-flapping peer disable** command.


Example
-------

# Disable OSPFv3 neighbor relationship flapping suppression globally.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] suppress-flapping peer disable

```
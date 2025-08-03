ospf maxage-lsa auto-protect disable
====================================

ospf maxage-lsa auto-protect disable

Function
--------



The **ospf maxage-lsa auto-protect disable** command disables master/slave board switching triggered by abnormal OSPF LSA aging.

The **undo ospf maxage-lsa auto-protect disable** command enables master/slave board switching triggered by abnormal OSPF LSA aging.



By default, master/slave board switching triggered by abnormal OSPF LSA aging is enabled.


Format
------

**ospf maxage-lsa auto-protect disable**

**undo ospf maxage-lsa auto-protect disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the local device's aging timer expires, the local device incorrectly clears all Router LSAs from the peer device, which causes route flapping and service interruptions. To resolve this issue, master/slave board switching triggered by abnormal OSPF LSA aging is automatically enabled. Master/Slave board switching is triggered to restore network connections and service traffic when the following condition is met:(Number of incorrectly cleared Router LSAs/Total number of Router LSAs) x 100%>=80% (Router LSAs are those sent by the peer device to the local device)To disable master/slave board switching triggered by abnormal OSPF LSA aging, run the **ospf maxage-lsa auto-protect disable** command.


Example
-------

# Disable master/slave board switching triggered by abnormal OSPF LSA aging.
```
<HUAWEI> system-view
[~HUAWEI] ospf maxage-lsa auto-protect disable

```
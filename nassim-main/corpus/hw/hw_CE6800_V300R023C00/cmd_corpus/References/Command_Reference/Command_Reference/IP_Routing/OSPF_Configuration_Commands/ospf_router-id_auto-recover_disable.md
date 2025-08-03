ospf router-id auto-recover disable
===================================

ospf router-id auto-recover disable

Function
--------



The **ospf router-id auto-recover disable** command disables automatic router ID recovery after a router detects a router ID conflict.

The **undo ospf router-id auto-recover disable** command enables automatic router ID recovery after a router detects a router ID conflict.



By default, automatic router ID recovery takes effect after a router detects a router ID conflict.


Format
------

**ospf router-id auto-recover disable**

**undo ospf router-id auto-recover disable**


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

**Usage Scenario**

If a router ID conflict occurs between indirectly connected devices in an OSPF area, the system can reselect a router ID to complete automatic router ID recovery. This prevents route flapping, reduces the route calculation frequency, and prevents other protocol disconnections caused by high CPU usage.

**Precautions**

* After automatic router ID conflict recovery is enabled, if a router ID conflict occurs on a non-directly connected device in an OSPF area, a router ID is automatically generated. The router ID is changed even if it is manually configured.
* After the router ID is changed, if the router ID conflict persists in the OSPF area, the router ID can be reselected for a maximum of three times by default.

Example
-------

# Disable automatic router ID recovery after a router detects a router ID conflict.
```
<HUAWEI> system-view
[~HUAWEI] ospf router-id auto-recover disable

```
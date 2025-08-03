route loop-detect isis enable
=============================

route loop-detect isis enable

Function
--------



The **route loop-detect isis enable** command enables loop detection for routes imported into IS-IS.

The **undo route loop-detect isis enable** command disables loop detection for routes imported into IS-IS.



By default, loop detection is disabled for the routes imported into IS-IS.


Format
------

**route loop-detect isis enable**

**undo route loop-detect isis enable**


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

When an IS-IS process imports routes, routing loops may occur. To enable routing loop detection for routes imported into IS-IS, run the **route loop-detect isis enable** command. When a device detects that it has imported a route advertised by itself, the device advertises a large link cost for the route so that other devices can preferentially select another path after learning the route. This prevents routing loops.

**Precautions**

* Before enabling loop detection, check whether non-Huawei devices exist on the network and ensure that IS-IS services are not affected when non-Huawei devices receive LSPs and private TLVs advertised by IS-IS.

1. If the non-Huawei device cannot identify the TLV or sub-TLV carried in the packet, ensure that the non-Huawei device ignores the TLV or sub-TLV without affecting the processing of other TLVs.
2. If the non-Huawei device uses the same private TLV type and the TLV values of the two functions conflict, do not configure this function.

* After a routing loop is removed, the device cannot automatically exit the routing loop state or clear the alarm. Manual intervention is required. For example, after a route-policy or route tag is correctly configured, run the **clear route loop-detect isis alarm-state** command to exit the loop state and clear the alarm.
* A single process supports loop detection for a maximum of 2000 imported routes. When the number of imported routes exceeds 2000, loop detection is automatically disabled. The system checks the number of imported routes in the early morning every day. If the number of imported routes is less than 2000, the system automatically restores the loop detection function.
* Summary routes and default routes do not support loop detection.
* Routing loop detection is supported in the scenario where two IS-IS domains import routes from each other. If there are more than two IS-IS domains, loops cannot be detected.
* After a loop is detected during route import between IS-IS processes, if the original route is withdrawn, a loop occurs. IS-IS reports a loop alarm, but the loop cannot be removed. Manual intervention is required.
* If the system IDs of the devices configured with IS-IS route import conflict in two IS-IS domains, a false loop detection error may occur.
* When a large cost is advertised due to detection of a loop, the **apply cost** command no longer takes effect.
* The IS-IS process that imports routes also calculates routes with the same prefix. If these routes and the routes imported to IS-IS work in load balancing mode across processes, loops cannot be detected.

Example
-------

# Enable loop detection.
```
<HUAWEI> system-view
[~HUAWEI] route loop-detect isis enable

```
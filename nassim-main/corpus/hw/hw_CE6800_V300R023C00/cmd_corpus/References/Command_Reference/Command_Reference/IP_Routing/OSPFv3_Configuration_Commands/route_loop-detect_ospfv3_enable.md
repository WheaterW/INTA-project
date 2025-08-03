route loop-detect ospfv3 enable
===============================

route loop-detect ospfv3 enable

Function
--------



The **route loop-detect ospfv3 enable** command enables loop detection for OSPFv3 imported routes.

The **undo route loop-detect ospfv3 enable** command disables loop detection for OSPFv3 imported routes.



By default, loop detection is disabled for OSPFv3 imported routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**route loop-detect ospfv3 enable**

**undo route loop-detect ospfv3 enable**


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

Routing loops may occur when an OSPFv3 process imports routes. To prevent routing loops, run the **route loop-detect ospfv3 enable** command to enable loop detection for the imported routes. When a device detects that it has imported a route advertised by itself, it advertises a large cost for the route to other devices. After learning this route, other devices preferentially select another path, preventing routing loops.

**Precautions**

* Before enabling routing loop detection, check whether non-Huawei devices exist on the network and ensure that OSPFv3 services are not affected when non-Huawei devices receive LSAs advertised by a Huawei device and private TLVs carried in the LSAs.

1. According to the protocol, non-Huawei devices must be able to receive and flood E-AS-External LSAs with the Type field set to U-bit. The establishment of neighbor relationships cannot be affected even if the LSAs cannot be recognized.
2. If a non-Huawei device receives an E-AS-External LSA but cannot identify the TLV or sub-TLV carried in the LSA, the non-Huawei device needs to ignore the TLV without affecting the processing of other TLVs.
3. If a non-Huawei device uses the same private TLV type and the TLV values of the two functions conflict, do not configure this function.Note: OSPFv3 advertises loop detection information through the sub-TLV (TLV type value 32770) of the External-Prefix TLV in the E-AS-External LSA.

* After a loop is removed, the device cannot automatically exit the routing loop state and the alarm cannot be automatically cleared. Manual intervention is required. For example, after a routing policy or route tag is correctly configured, run the **clear route loop-detect ospfv3 alarm-state** command to exit the routing loop state and clear the alarm.
* A single process supports routing loop detection for a maximum of 100,000 routes. If more than 100,000 routes are imported, loops cannot be detected for the excess routes. The system checks the number of routes for loop detection at 03:00 every day. If the number of routes for loop detection is less than 100,000, the system performs loop detection on the previously excess imported routes. The maximum number of imported routes for loop detection is still 100,000.
* When a large cost is advertised upon a routing loop, the **apply cost** command does not take effect.
* Summary routes and NSSA routes do not support routing loop detection.
* The default route advertised using the **default-route-advertise** command supports only loop detection and does not support self-healing.
* Only loops caused by inter-process route import between two devices can be detected. If more than two devices import routes between processes, loops cannot be detected.
* Router ID conflicts are not supported, including intra-AS and inter-AS router ID conflicts. A router ID conflict may trigger incorrect detection.
* When the OSPF process that imports routes calculates routes with the same prefix and the calculated routes participate in load balancing with the imported routes, loops cannot be detected.

Example
-------

# Enable OSPFv3 loop detection.
```
<HUAWEI> system-view
[~HUAWEI] route loop-detect ospfv3 enable

```
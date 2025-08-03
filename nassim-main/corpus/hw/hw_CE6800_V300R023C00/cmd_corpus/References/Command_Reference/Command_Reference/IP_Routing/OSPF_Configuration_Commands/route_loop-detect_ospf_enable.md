route loop-detect ospf enable
=============================

route loop-detect ospf enable

Function
--------



The **route loop-detect ospf enable** command enables OSPF to detect loops of imported OSPF, IS-IS, and BGP routes.

The **undo route loop-detect ospf enable** command disables OSPF from detecting loops of imported OSPF, IS-IS, and BGP routes.

The **route loop-detect ospf import-ospf enable** command enables OSPF to detect loops of imported OSPF routes.

The **undo route loop-detect ospf import-ospf enable** command disables OSPF from detecting loops of imported OSPF routes.



By default, loop detection is disabled for routes imported into OSPF.


Format
------

**route loop-detect ospf enable**

**route loop-detect ospf import-ospf enable**

**undo route loop-detect ospf enable**

**undo route loop-detect ospf import-ospf enable**


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

When an OSPF process imports routes, routing loops are likely to occur. You can run the route loop-detect ospf [import-ospf] enable command to enable loop detection for imported OSPF routes. When a device detects that it has imported a route advertised by itself, the device advertises a large link cost for the route so that other devices can preferentially select another path after learning the route. This prevents routing loops.

**Precautions**

* Before enabling routing loop detection, check whether non-Huawei devices exist on the network and ensure that OSPF services are not affected when non-Huawei devices receive LSAs advertised by a Huawei device and private TLVs carried in the LSAs.

1. According to the protocol, if a non-Huawei device has the Opaque capability, it must be able to receive and flood AS Opaque LSAs. If a non-Huawei device does not have the Opaque capability, it must be able to discard AS Opaque LSAs without affecting neighbor relationship establishment.
2. If a non-Huawei device receives an AS Opaque LSA but cannot identify the TLV or sub-TLV carried in the AS Opaque LSA, the non-Huawei device needs to ignore this TLV without affecting the processing of other TLVs.
3. If a non-Huawei device uses the same private TLV type and the TLV values of the two functions conflict, do not configure this function.Note: OSPF advertises loop detection information through the sub-TLV (TLV type value: 32770) of the Extended Prefix TLV in the AS Opaque LSA.

* OSPF uses opaque LSAs to detect loops of imported routes. Therefore, the opaque LSA capability must be enabled using the **opaque-capability enable** command.
* After a loop is removed, the device cannot automatically exit the routing loop state, the alarm cannot be automatically cleared, and the normal cost cannot be restored. Manual intervention is required. For example, after a routing policy or route tag is correctly configured, run the **clear route loop-detect ospf alarm-state** command to exit the routing loop state and clear the alarm.
* A single process supports routing loop detection for a maximum of 100,000 routes. If more than 100,000 routes are imported, loops cannot be detected for the excess routes. The system checks the number of routes for loop detection at 03:00 every day. If the number of routes for loop detection is less than 100,000, the system performs loop detection on the previously excess imported routes. The maximum number of imported routes for loop detection is still 100,000.
* When a large cost is advertised upon a routing loop, the **apply cost** command does not take effect.
* Summary routes and NSSA routes do not support routing loop detection.
* The default route advertised using the **default-route-advertise** command supports loop detection and cost increasing. However, increasing the cost of the default route cannot ensure self-healing of loops.
* Only loops caused by inter-process route import between two devices can be detected. If more than two devices import routes between processes, loops cannot be detected.
* Router ID conflicts are not supported, including intra-AS and inter-AS router ID conflicts. A router ID conflict may trigger incorrect detection.
* When the OSPF process that imports routes calculates routes with the same prefix and the calculated routes participate in load balancing with the imported routes, loops cannot be detected.

Example
-------

# Enable loop detection for imported OSPF routes.
```
<HUAWEI> system-view
[~HUAWEI] route loop-detect ospf import-ospf enable

```

# Enable loop detection.
```
<HUAWEI> system-view
[~HUAWEI] route loop-detect ospf enable

```
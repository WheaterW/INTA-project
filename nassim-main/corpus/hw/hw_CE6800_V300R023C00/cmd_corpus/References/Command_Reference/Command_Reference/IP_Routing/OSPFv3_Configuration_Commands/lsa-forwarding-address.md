lsa-forwarding-address
======================

lsa-forwarding-address

Function
--------



The **lsa-forwarding-address** command enables the OSPFv3 forwarding address (FA) function.

The **undo lsa-forwarding-address** command disables the OSPFv3 FA function.



By default, the OSPFv3 FA function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**lsa-forwarding-address** { **standard** | **zero-translate** }

**undo lsa-forwarding-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **standard** | Indicates that the OSPFv3 FA function is compatible with OSPF NSSA RFC. | - |
| **zero-translate** | Allows the Type 7 LSAs with the Propagate (P) bit set and without the FA to be translated to Type 5 LSAs. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* When external routes are imported to an OSPFv3 area, to calculate the optimal path based on the FA, run the **lsa-forwarding-address** command. If the **lsa-forwarding-address standard** command is run, NSSA-LSAs are converted to AS external LSAs only when the P-bit is set to 1 and the FA exists. If the **lsa-forwarding-address zero-translate** command is run, NSSA-LSAs in which the P-bit is set to 1 and the FA does not exist can be converted to AS external LSAs.
* The rules for setting the forwarding address of NSSA LSAs are as follows:

1. The global IP address of the active interface in the NSSA is preferentially selected. The global IP address of the loopback interface is preferentially selected. The global IP address of the common interface on which no neighbor relationship is established is the second optimal. Them the global IP address of another interface is selected. If the priorities are the same, the smaller global IP address of the interface is preferentially selected.
2. When a new interface with a better IP address is available in the area, the LSA forwarding address is updated after a delay of 10s. When the IP address of the interface that functions as the FA is unavailable, the LSA forwarding address is updated immediately.

**Precautions**

* According to the FA selection rules of NSSA LSAs, the system compares whether the neighbor relationship is established on the interface during FA selection. If the neighbor status of the interface changes after the restart, the FA address may change after the restart.
* You are advised to configure a loopback address for the device in the NSSA so that the loopback address can be automatically selected as the FA. Loopback interfaces do not establish neighbor relationships. Therefore, loopback interface addresses are stable and are recommeded as FAs. If other devices have multiple paths with the same cost to the device in the NSSA, load balancing can be implemented.

Example
-------

# Enable the OSPFv3 FA function and allow it to be compatible with OSPF NSSA RFC.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] lsa-forwarding-address standard

```
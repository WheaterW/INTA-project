bfd all-interfaces enable (OSPFv3 view)
=======================================

bfd all-interfaces enable (OSPFv3 view)

Function
--------



The **bfd all-interfaces incr-cost** command enables an OSPFv3 process to adjust the cost based on BFD.

The **undo bfd all-interfaces incr-cost** command disables an OSPFv3 process from adjusting the cost based on BFD.

The **bfd all-interfaces enable** command enables BFD for OSPFv3.

The **undo bfd all-interfaces enable** command disables BFD for OSPFv3.



By default, an OSPFv3 process does not adjust the cost based on BFD.

By default, BFD is not enabled for OSPFv3.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bfd all-interfaces enable**

**bfd all-interfaces incr-cost** { *cost* | **max-reachable** }

**undo bfd all-interfaces enable**

**undo bfd all-interfaces incr-cost** [ *cost* | **max-reachable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **incr-cost** *cost* | Specifies a cost adjustment value. | The value is an integer that ranges from 1 to 65534 . |
| **max-reachable** | Adjusts the link cost of an OSPFv3 interface to the maximum link cost 65535. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Either a link fault or topology change on a network will cause routes to be re-calculated within an area. As such, speeding up the convergence of a routing protocol is critical to improving the network performance.As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. This includes associating BFD with a routing protocol to speed up convergence of the routing protocol once a link fault occurs.

**Prerequisites**



Before running the **bfd all-interfaces incr-cost** command, you need to run the **bfd all-interfaces enable** command to enable BFD in the OSPFv3 process.



**Precautions**



The cost value association with BFD configured on an interface takes precedence over that in a process.After BFD is enabled, OSPFv3 establishes BFD sessions only with neighbors in the Exstart state.The BFD feature configured on the interface has priority over the BFD feature configured for the process.The bfd all-interfaces and ospfv3 bfd block commands are mutually exclusive.




Example
-------

# Configure an OSPFv3 process to adjust the link cost to 5 based on BFD.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] bfd all-interfaces enable
[*HUAWEI-ospfv3-100] bfd all-interfaces incr-cost 5

```

# Enable BFD for an OSPFv3 process.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] bfd all-interfaces enable

```
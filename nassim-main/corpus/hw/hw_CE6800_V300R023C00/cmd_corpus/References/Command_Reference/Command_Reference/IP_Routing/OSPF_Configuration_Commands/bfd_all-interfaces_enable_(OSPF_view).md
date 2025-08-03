bfd all-interfaces enable (OSPF view)
=====================================

bfd all-interfaces enable (OSPF view)

Function
--------



The **bfd all-interfaces enable** command enables BFD in an OSPF process.

The **undo bfd all-interfaces enable** command disables BFD in an OSPF process.

The **bfd all-interfaces incr-cost** command enables an OSPF process to adjust the cost based on BFD.

The **undo bfd all-interfaces incr-cost** command disables an OSPF process from adjusting the cost based on BFD.



By default, BFD is disabled.

By default, an OSPF process does not adjust the cost based on BFD.




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
| **max-reachable** | Adjusts the link cost to the maximum link cost 65535. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BFD can fast detect a fault on a network, minimizing the impact of the fault on services.You can enable BFD either on an interface or in an OSPF process. The configurations of BFD on an interface take precedence over those in an OSPF process. When BFD detects a fault, which is rectified soon, the corresponding interface is disconnected due to the BFD Down event. As a result, the link is unstable, and traffic is lost.To ensure network reliability and solve the preceding problems, run the **bfd all-interfaces incr-cost** command for OSPF to adjust the link cost. When the OSPF process detects that the BFD session goes down, OSPF automatically increases the cost of the corresponding interface so that the problem link associated with the BFD session is not preferentially selected; in this case, traffic is transmitted over other links.When the device detects that the BFD session goes up, the cost of the interface is automatically restored to the original value. If link quality changes frequently, BFD status changes frequently too, causing link instability, which may in turn lead to traffic loss. To solve the preceding problem, you can run the bfd all-interfaces incr-cost wtr command on the OSPF interface for delayed interface cost restoration. BFD status changes within the delay do not cause path calculation changes, ensuring network reliability.



**Prerequisites**

Before running the **bfd all-interfaces incr-cost** command, you need to run the **bfd all-interfaces enable** command to enable BFD in the OSPF process.

**Precautions**

The cost value association with BFD configured on an interface takes precedence over that configured in a process.A BFD session can be established only after global BFD is configured on both ends and the **bfd all-interfaces enable** command is run. In addition, OSPF establishes BFD sessions only with neighbors in the Exstart state.The **bfd all-interfaces** command and the ospf bfd block command are mutually exclusive.


Example
-------

# Configure an OSPF process to adjust the link cost to 5 based on BFD.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] bfd all-interfaces enable
[*HUAWEI-ospf-100] bfd all-interfaces incr-cost 5

```
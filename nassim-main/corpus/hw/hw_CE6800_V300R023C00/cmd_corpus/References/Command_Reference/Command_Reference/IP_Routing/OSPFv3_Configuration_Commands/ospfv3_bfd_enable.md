ospfv3 bfd enable
=================

ospfv3 bfd enable

Function
--------



The **ospfv3 bfd enable** command enables BFD on an OSPFv3 interface.

The **undo ospfv3 bfd enable** command disables BFD from an interface.

The **ospfv3 bfd incr-cost** command enables an OSPFv3 interface to adjust the cost based on BFD.

The **undo ospfv3 bfd incr-cost** command disables an OSPFv3 interface from adjusting the cost based on BFD.

The **ospfv3 bfd incr-cost block** command blocks an OSPFv3 interface from adjusting the cost based on BFD.

The **undo ospfv3 bfd incr-cost block** command unblocks an OSPFv3 interface from adjusting the cost based on BFD.



By default, BFD is not enabled on an OSPFv3 interface.

By default, an OSPFv3 interface does not adjust the cost based on BFD.

By default, an OSPFv3 interface is not blocked from adjusting the cost based on BFD.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 bfd enable** [ **instance** *instance-id* ]

**ospfv3 bfd incr-cost** { *cost* | **max-reachable** } [ **instance** *instance-id* ]

**ospfv3 bfd incr-cost block**

**undo ospfv3 bfd enable** [ **instance** *instance-id* ]

**undo ospfv3 bfd incr-cost** [ *cost* | **max-reachable** ] [ **instance** *instance-id* ]

**undo ospfv3 bfd incr-cost block**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Indicates the ID of the instance to which the interface belongs. | The value is an integer that ranges from 0 to 255. |
| **incr-cost** *cost* | Specifies a cost adjustment value. | The value is an integer ranging from 1 to 65534. |
| **max-reachable** | Adjusts the link cost of an OSPF interface to the maximum link cost 65535. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A link fault or topology change on a network causes route recalculation in an area. Shortening the convergence time of routing protocols is important to improve network performance.Link faults cannot be completely avoided. Therefore, it is feasible to speed up fault detection and quickly notify routing protocols of faults. BFD is associated with routing protocols. Once a link fails, BFD can speed up the convergence of routing protocols.When BFD detects a link fault on the network, the interface is disconnected because BFD goes Down even if the fault is rectified quickly. As a result, the link is unstable and traffic is lost. To ensure network reliability and solve the preceding problems, run the **ospfv3 bfd incr-cost** command on an OSPFv3 interface to adjust the link cost. When the OSPFv3 interface detects that a BFD session goes Down, the OSPFv3 interface automatically increases the link cost.When the device detects that the BFD session goes Up, the cost of the interface is automatically restored to the previous cost. If frequent BFD status changes occur due to bad link quality, traffic loss may occur due to link instability. To address this problem, run the **ospfv3 bfd incr-cost wtr** command to set a withdrawal delay on an OSPFv3 interface. BFD status changes within the delay do not cause path calculation changes, ensuring network reliability.



**Prerequisites**

BFD has been enabled on the interface.

**Configuration Impact**

If global BFD is not enabled, BFD can be enabled on an interface. The BFD session, however, cannot be set up after BFD is enabled on the interface. If the parameters of a BFD session are set but the **ospfv3 bfd enable** command is not run, the BFD session cannot be set up.The BFD configuration on an interface takes precedence over that in a process. If BFD is enabled on an interface, a BFD session is established according to the BFD parameters set on the interface.

**Follow-up Procedure**

Run the **display ospfv3 bfd session** command to view the information about neighbors enabled with BFD.

**Precautions**



After BFD is enabled, a device sets up BFD sessions with only adjacencies.The **ospfv3 bfd enable** command and ospfv3 bfd block command are mutually exclusive in function, and the later configuration overwrites the previous one.After BFD is disabled from an interface using the **undo ospfv3 bfd enable** command, the parameters for setting up BFD sessions remain on this interface but no longer take effect.The interface-specific BFD-associated cost value has a higher priority than the process-specific BFD-associated cost value.The ospfv3 bfd incr-cost block and ospfv3 bfd incr-cost { cost | max-reachable } commands are mutually exclusive. The latter command overwrites the previously configured command.




Example
-------

# Enable BFD function on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 bfd enable

```
ospf bfd (interface view)
=========================

ospf bfd (interface view)

Function
--------



The **ospf bfd enable** command enables BFD on an OSPF interface.

The **undo ospf bfd enable** command disables BFD from an interface.

The **ospf bfd incr-cost** command enables an OSPF interface to adjust the cost based on BFD.

The **undo ospf bfd incr-cost** command disables an OSPF interface from adjusting the cost based on BFD.

The **ospf bfd incr-cost block** command blocks an OSPF interface from adjusting the cost based on BFD.

The **undo ospf bfd incr-cost block** command unblocks an OSPF interface from adjusting the cost based on BFD.



By default, BFD is not enabled in the OSPF interface view.

By default, an OSPF interface does not adjust the cost based on BFD.

By default, an OSPF interface is not blocked from adjusting the cost based on BFD.




Format
------

**ospf bfd enable**

**ospf bfd incr-cost** { *cost* | **max-reachable** }

**ospf bfd incr-cost block**

**undo ospf bfd incr-cost** [ *cost* | **max-reachable** ]

**undo ospf bfd incr-cost block**

**undo ospf bfd enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost* | Specifies a cost increment value for the interface. | The value is an integer that ranges from 1 to 65534 . |
| **max-reachable** | Adjusts the link cost of an OSPF interface to the maximum link cost 65535. | - |
| **enable** | Enables BFD. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Either a link fault or topology change on a network will cause routes to be re-calculated within an area. As such, speeding up the convergence of a routing protocol is critical to improving the network performance.As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. This includes associating BFD with a routing protocol to speed up convergence of the routing protocol once a link fault occurs.On a network where BFD detects a link fault, even if the fault is rectified quickly, the involved interface is disconnected due to the fact that the associated BFD session is down. As a result, the link is unstable and traffic is lost. To ensure network reliability and solve the preceding problems, run the **ospf bfd incr-cost** command on an OSPF interface to adjust the link cost. When the OSPF interface detects that the BFD session goes Down, the OSPF interface automatically increases the link cost so that the link in the BFD Down state is not preferentially selected, traffic can be transmitted over other links.When an interface detects that a BFD session goes Up, the cost of the interface is automatically restored to the original value. To prevent frequent BFD status changes caused by link quality, traffic loss may occur due to link instability. To solve the preceding problem, run the ospf bfd incr-cost wtr command on an OSPF interface to set a delay after which the interface cost is restored. A BFD status change within the delay does not cause a path calculation change, ensuring network reliability.



**Prerequisites**

Before running the **ospf bfd enable** command, you need to enable BFD globally.Before running the **ospf bfd incr-cost** and **ospf bfd incr-cost block** commands, you need to run the **ospf bfd enable** command to enable BFD on the interface.

**Configuration Impact**



If global BFD is not enabled, you can enable BFD on an interface, but BFD sessions cannot be set up in this case. Similarly, if only parameters of a BFD session are set but the **ospf bfd enable** command is not used, the BFD session cannot be set up.BFD configured on an interface takes precedence over BFD configured for a process. If BFD is enabled on an interface, the BFD parameters on the interface are used to establish BFD sessions.



**Precautions**

* After BFD is enabled, OSPF establishes BFD sessions only with neighbors in the Full state.
* After BFD is disabled on an interface using the **undo ospf bfd enable** command, BFD session parameters still exist on the interface.
* The cost value associated with BFD configured on an interface takes precedence over that associated with BFD configured in a process.
* The **ospf bfd enable** and **ospf bfd block** commands are mutually exclusive. The latest configuration overrides the previous one.
* The **ospf bfd incr-cost block** and **ospf bfd incr-cost** { *cost*| **max-reachable** } commands are mutually exclusive. The latest configuration overrides the previous one.


Example
-------

# Enable BFD function on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf bfd enable

```
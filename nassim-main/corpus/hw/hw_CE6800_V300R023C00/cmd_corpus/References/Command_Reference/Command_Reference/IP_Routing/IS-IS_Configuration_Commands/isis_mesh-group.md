isis mesh-group
===============

isis mesh-group

Function
--------



The **isis mesh-group** command adds an interface to a specified mesh-group.

The **undo isis mesh-group** command deletes the interface from the mesh-group.



By default, an interface does not belong to any mesh-group and floods LSPs normally.


Format
------

**isis mesh-group** { *mesh-group-number* | **mesh-blocked** }

**undo isis mesh-group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mesh-group-number* | Specifies a mesh-group number. | The value is an integer ranging from 1 to 4294967295. |
| **mesh-blocked** | Blocks the interface so that no new LSPs are flooded on this interface. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an interface that does not belong to an IS-IS mesh-group receives an LSP, the interface sends the LSP to all the other interfaces. On an NBMA network with multiple connections and P2P links, the same LSP will flood the network and consume bandwidth.To address this problem, run the **isis mesh-group** command to add an interface to a mesh-group. Then, the interface sends the received LSP only to interfaces that do not belong to its mesh-group.It is also mentioned in the agreement that in order to prevent the mesh-group feature from causing the database to be out of sync, the interface configured with the mesh-group should periodically flood CSNP. Therefore, when an interface of the device receives an LSP, other interfaces configured with mesh-group periodically send CSNP packets. After the peer device receives the CSNP packet, the peer device compares its own database and will do so when it finds that the LSP packet is missing. Send PSNP to request updated LSP packets. In this case, new LSP packets will also be sent on the mesh-group interface normally.

**Prerequisites**

IS-IS has been enabled on an interface using the **isis enable** command.

**Configuration Impact**

If all interfaces on a device are blocked, no packet can be sent, causing a database synchronization problem.

**Precautions**

When adding interfaces to mesh-groups or blocking interfaces, do not run the **isis mesh-group** command on all interfaces. This can prevent link faults from affecting the normal spreading of LSPs.


Example
-------

# Add 100GE1/0/1 to mesh-group 3.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis mesh-group 3

```
port (Smart Link group view)
============================

port (Smart Link group view)

Function
--------



The **port** command adds an interface to a Smart Link group and specifies the interface as a master or slave interface.

The **undo port** command deletes a master or slave interface from a Smart Link group.



By default, no interface is added to a Smart Link group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**port** { *interface-name* | *interface-type* *interface-number* } { **master** | **slave** }

**undo port** [ **all** | [ *interface-name* | *interface-type* *interface-number* ] { **master** | **slave** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-number* | Specifies an interface to be added to a Smart Link group.   * interface-type specifies the type of the interface. * interface-number specifies the number of the interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **master** | Specifies the interface as a master interface. | - |
| **slave** | Specifies the interface as a slave interface. | - |
| **all** | Deletes all interfaces in a Smart Link group. | - |



Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Smart Link is a reliability mechanism that provides reliable and efficient link backup and a fast traffic switchover. Smart Link is used on dual-homing networks. If the primary and secondary links in a Smart Link group are normal, the secondary link is blocked to provide backup. If the primary link fails, traffic is switched to the secondary link. To implement the preceding functions, run the port command to configure a master interface and a slave interface in the Smart Link group. In most cases, only one interface is Active, and the other interface is blocked and Inactive.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command, and the spanning tree protocol has been disabled using the **stp disable** command on the interfaces to be added to the Smart Link group.

**Follow-up Procedure**

Run the **smart-link enable** command to enable the Smart Link group. Run the **flush send** command to enable the Smart Link group to send Flush packets on the device, and run the smart-link flush receive command to enable an interface on a device to receive Flush packets.

**Precautions**

* To reconfigure the master or slave interface in a Smart Link group, delete the configured master or slave interface first.
* Normally, the slave interface in a Smart Link group is blocked after the Smart Link group is enabled.
* Deleting an interface from a Smart Link group may cause a temporary loop.
* An interface can be added to only one Smart Link group.
* An interface cannot be added to a Smart Link group in the following situations:
* STP has been enabled on the interface.
* The interface has been added to an Eth-Trunk.
* The interface has been added to a Monitor Link group.
* The interface has been added to another Smart Link group.

Example
-------

# Add to Smart Link group 1 and specify the interface as the master interface.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] port 100GE 1/0/1 master

```
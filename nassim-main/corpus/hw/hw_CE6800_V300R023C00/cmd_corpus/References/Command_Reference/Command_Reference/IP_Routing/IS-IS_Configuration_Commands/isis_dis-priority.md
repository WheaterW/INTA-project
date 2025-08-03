isis dis-priority
=================

isis dis-priority

Function
--------



The **isis dis-priority** command sets a priority for an interface to run for the DIS on a specified level.

The **undo isis dis-priority** command restores the default priority.



By default, the DIS priority of an IS-IS interface is 64.


Format
------

**isis dis-priority** *priority* [ **level-1** | **level-2** ]

**undo isis dis-priority** [ *priority* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a priority for DIS election. | The value is an integer ranging from 0 to 127. |
| **level-1** | Specifies a priority for Level-1 DIS election. | - |
| **level-2** | Specifies a priority for Level-2 DIS election. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a broadcast network, IS-IS needs to elect a DIS from all devices. If there are Level-1 and Level-2 devices on this network, Level-1 and Level-2 DISs are elected separately and can be the same device or different devices.The DIS is elected as follows: The device whose IS-IS interface has the highest DIS priority is elected as the DIS; If the interfaces on multiple devices have the same DIS priority, the device whose interface has the largest MAC address is elected as the DIS.The **isis dis-priority** command can be used to set a DIS Priority for an IS-IS interface.

**Prerequisites**

An IS-IS process has been created, and the IS-IS process has been started on a specified interface.

**Configuration Impact**

If neither Level-1 nor Level-2 is specified in the command, the same priority is set for Level-1 and Level-2 DISs.After the **isis dis-priority** command is run, the DIS priority is advertised in Hello packets.

**Precautions**

This configuration is valid only for broadcast networks.If the network type of an Ethernet interface is changed to P2P through the **isis circuit-type** command, the **isis dis-priority** command does not take effect on the Ethernet interface.This command takes effect on both IPv4 and IPv6.The isis dis-priority and isis circuit-type p2p commands are mutually exclusive.


Example
-------

# Set the DIS priority of 100GE1/0/1 to 127.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis dis-priority 127 level-2

```
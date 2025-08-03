ospfv3 dr-priority
==================

ospfv3 dr-priority

Function
--------



The **ospfv3 dr-priority** command sets the priority of an interface that runs for the DR or BDR.

The **undo ospfv3 dr-priority** command restores the default value.



By default, the priority is 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 dr-priority** *priovalue* [ **instance** *instanceId* ]

**undo ospfv3 dr-priority** [ *priovalue* ] [ **instance** *instanceId* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priovalue* | Specifies the priority of the interface that runs for the DR or BDR. | The value is an integer ranging from 0 to 255. |
| **instance** *instanceId* | Specifies the interface instance ID. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The priority of an interface determines whether the interface is qualified to be a DR or BDR. The interface with the highest priority is elected as the DR or BDR. If the priority of an interface on a device is 0, the device cannot be elected as a DR or BDR. On a broadcast or an NBMA network, you can set the priority of an interface to control the DR or BDR selection.ProcedureIn OSPFv3, the DR priority cannot be configured for null interfaces.

**Prerequisites**

OSPFv3 has been enabled on the interface. To set the priority of an interface in a specified instance for DR/BDR election, ensure that the instance parameter is also configured when OSPFv3 is enabled on the interface.

**Implementation Procedure**

In OSPFv3, the DR priority cannot be configured for null interfaces.

**Follow-up Procedure**

Run the **display ospfv3 interface** command to view the DR and BDR on the network.


Example
-------

# Set the priority of instance 1 on the interface that runs for the DR or BDR to 8.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 dr-priority 8 instance 1

```
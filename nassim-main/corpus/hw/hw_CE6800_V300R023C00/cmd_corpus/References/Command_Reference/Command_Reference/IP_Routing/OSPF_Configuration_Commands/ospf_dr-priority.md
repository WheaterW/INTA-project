ospf dr-priority
================

ospf dr-priority

Function
--------



The **ospf dr-priority** command sets the priority of an interface that runs for the DR or BDR.

The **undo ospf dr-priority** command restores the default value.



By default, the priority is 1.


Format
------

**ospf dr-priority** *priovalue*

**undo ospf dr-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priovalue* | Specifies the priority of the interface that runs for the DR or BDR. The greater the value, the higher the priority. | The value is an integer ranging from 0 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The priority of an interface determines whether the interface is qualified to be a DR or BDR. The interface with the highest priority is elected as the DR. If the priority of an interface is 0, it cannot be elected as a DR or BDR. On a broadcast or an NBMA network, you can set the priority of an interface to control the DR or BDR selection.

**Configuration Impact**

When the DR and BDR are elected on a network segment, they send DD packets to all neighboring nodes and set up adjacencies with all neighboring nodes.

**Precautions**

OSPF does not support the configuration of DR priorities on null interfaces.According to the protocol, the OSPF DR/BDR does not have preemption. Therefore, reconfiguring the DR priority of a device does not change the DR or BDR on the network. You can use either of the following methods to re-elect a DR or BDR. However, the methods will interrupt the OSPF neighbor relationship between devices. Therefore, these methods are not recommended.

* Restart OSPF processes on all devices.
* Run the **shutdown** and **undo shutdown** commands in sequence on the interfaces where OSPF neighbor relationships are established.

Example
-------

# Set the priority of the interface that runs for the DR or BDR to 8.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf dr-priority 8

```
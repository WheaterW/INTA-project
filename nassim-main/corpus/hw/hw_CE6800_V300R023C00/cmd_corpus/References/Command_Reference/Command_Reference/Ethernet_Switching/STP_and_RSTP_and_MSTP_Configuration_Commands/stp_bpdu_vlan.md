stp bpdu vlan
=============

stp bpdu vlan

Function
--------



The **stp bpdu vlan** command enables an interface to add a specified VLAN ID to bridge protocol data units (BPDUs) before sending them.

The **undo stp bpdu vlan** command disables the function.



By default, an interface does not add a VLAN ID to BPDUs that it sends.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**stp bpdu vlan** *vlan-id*

**undo stp bpdu vlan**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the VLAN ID that the interface adds to BPDUs. | The value is an integer ranging from 1 to 4094. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* If multiple user networks are connected to the same interface of a PE, configure the interfaces of CEs to add specific VLAN IDs to BPDUs before sending them to the PE.
* Run the **stp bpdu vlan** command on an interface of a CE to add a specified VLAN ID to BPDUs before sending them.
* In most cases, the **stp bpdu vlan** command is configured on the network-side interface of a CE.

**Prerequisites**



If the interface is a Layer 3 interface, it must have been switched to a Layer 2 interface using the **portswitch** command.Before configuring a CE interface to add a VLAN ID to BPDUs to be sent to a PE, ensure that the interface has been added to the specified VLAN.




Example
-------

# Configure the VLAN ID in BPDUs sent by the interface to 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[~HUAWEI-vlan100] quit
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 100
[*HUAWEI-100GE1/0/1] stp bpdu vlan 100

```
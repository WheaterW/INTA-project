port (VLAN view)
================

port (VLAN view)

Function
--------



The **port** command sets a default VLAN for interfaces and adds interfaces to the VLAN.

The **undo port** command deletes the interfaces from the default VLAN and restores the default VLAN ID.



By default, the VLAN ID of all interfaces is 1.


Format
------

**port** *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10>

**port** *interface-name*

**undo port** *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10>

**undo port** *interface-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | - |
| *interface-number1* | Specifies the start number of an interface. | - |
| **to** *interface-number2* | Specifies the end number of an interface. | - |
| *interface-name* | Specifies the name of an interface. | - |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Frames sent from user hosts are untagged and those sent from a remote device may also be untagged. However, a switching device only processes and forwards tagged frames. Therefore, tags need to be added to the untagged frames on the switching device. To implement this function, run the **port default vlan** command to configure a default VLAN on an interface of the switching device. After this function is enabled, the interface adds the default VLAN ID to received untagged frames.After a default VLAN is configured on an interface:The interface inserts the default VLAN ID to a received untagged frame if the link type of the interface is access or hybrid.When the interface receives a tagged frame:If the interface type is access and the VLAN ID in the tag is the same as the default VLAN ID, the access interface forwards the frame.If the VLAN ID in the tag is different from the default VLAN ID, the access interface discards the frame.If the interface type is hybrid and the VLAN ID in the tag is in the permitted VLAN ID list, the hybrid interface forwards the frame.If the VLAN ID is not in the permitted VLAN ID list, the hybrid interface discards the frame.When the interface sends a tagged frame:If the interface type is access, the access interface removes the VLAN tag and then forwards the frame.If the interface type is hybrid, the hybrid interface removes or keeps the VLAN tag in a frame as required and then forwards the frame.



**Prerequisites**



The link type of the interface has been configured as access or hybrid or dot1q-tunnel using the **port link-type** command.



**Precautions**



The port command has the same function as the **port default vlan** command in the interface view.Before you specify an interface range, note that:1.The interface types must be the same.2.The interfaces in the range must exist.3.If the port command is run more than once, all configurations take effect.4.The interface to be added to a VLAN must be a Layer 2 interface. If the interface is a Layer 3 interface, run the **portswitch** command to switch the interface to Layer 2. The **port default vlan** command cannot be configured on physical interfaces that are added to an Eth-Trunk.




Example
-------

# Add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 3.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] port link-type access
[~HUAWEI-100GE1/0/1] quit
[~HUAWEI] interface 100GE 1/0/2
[~HUAWEI-100GE1/0/2] portswitch
[~HUAWEI-100GE1/0/2] port link-type access
[~HUAWEI-100GE1/0/2] quit
[~HUAWEI] vlan 3
[*HUAWEI-vlan3] port 100GE 1/0/1 to 1/0/2

```
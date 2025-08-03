undo mac-address sticky
=======================

undo mac-address sticky

Function
--------



The **undo mac-address sticky** command deletes the MAC address entries learned after the sticky MAC function is enabled on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**undo mac-address sticky** { [ *portType* *portNum* | *portName* ] | [ **vlan** *vlanId* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *portType* | Specifies the type of an interface. | - |
| *portNum* | Specifies an interface number. | - |
| *portName* | Specifies an interface name. | The value is a string of 1 to 47 characters. |
| **vlan** *vlanId* | Specifies the ID of a VLAN to which the outbound interface belongs. | The value is an integer ranging from 1 to 4094. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the **port-security mac-address sticky** command to enable the sticky MAC function on an interface, the secure dynamic MAC addresses learned by the interface become sticky MAC addresses (static MAC addresses). If the learned sticky MAC address entries are not expected ones, run the **undo mac-address sticky** command to delete them and enable the interface to relearn sticky MAC addresses.


Example
-------

# Delete the sticky MAC address entries learned by 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] undo mac-address sticky 100GE 1/0/1

```
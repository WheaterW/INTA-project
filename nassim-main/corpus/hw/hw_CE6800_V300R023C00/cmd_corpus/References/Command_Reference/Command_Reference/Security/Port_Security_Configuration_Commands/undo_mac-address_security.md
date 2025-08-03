undo mac-address security
=========================

undo mac-address security

Function
--------



The **undo mac-address security** command deletes the MAC address entries learned after the security function is enabled on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**undo mac-address security** { [ *interface-type* *interface-number* | *interface-name* ] | [ **vlan** *vlanId* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlanId* | Specifies the ID of a VLAN to which the outbound interface belongs. | The value is an integer ranging from 1 to 4094. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the **port-security enable** command to enable the security function on an interface, the MAC address entries learned by the interface become secure dynamic MAC address entries. If the learned secure dynamic MAC address entries are not expected ones, run the **undo mac-address security** command to delete them.


Example
-------

# Delete the secure dynamic MAC address entries learned by 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] undo mac-address security 100GE 1/0/1

```
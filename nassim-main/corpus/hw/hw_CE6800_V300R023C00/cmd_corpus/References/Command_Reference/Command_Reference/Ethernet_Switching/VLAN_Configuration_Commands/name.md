name
====

name

Function
--------



The **name** command configures a name for a VLAN.

The **undo name** command deletes the VLAN name.



By default, a VLAN does not have a name.


Format
------

**name** *vlan-name*

**undo name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *vlan-name* | Specifies a VLAN name. | The name is a string of 1 to 31 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If multiple VLANs are configured on a device to transmit different services, you can run the **name** command in a VLAN view to configure a VLAN name to facilitate service management. In addition, you can check the deployed services of a VLAN by the VLAN name.After a VLAN is named, you can run the **vlan vlan-name** command in the system view to enter the VLAN view and check or modify the VLAN configuration.




Example
-------

# Configure voice as the name of VLAN 2 used to transmit voice services.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] name voice

```
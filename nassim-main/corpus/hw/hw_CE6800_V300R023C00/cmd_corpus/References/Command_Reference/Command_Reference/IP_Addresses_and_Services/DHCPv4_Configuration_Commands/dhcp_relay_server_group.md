dhcp relay server group
=======================

dhcp relay server group

Function
--------



The **dhcp relay server group** command creates a DHCP server group and displays the DHCP server group view.

The **undo dhcp relay server group** command deletes a specified DHCP server group.



By default, no DHCP server group is created.


Format
------

**dhcp relay server group** *group-name*

**undo dhcp relay server group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a DHCP server group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, and can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot use "-" and "--" as names. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A DHCP relay agent serves multiple DHCP servers for assigning IP addresses to DHCP clients. To facilitate DHCP server management, run the dhcp server group command to create a DHCP server group. Then add DHCP servers to the DHCP server group.

**Follow-up Procedure**

* **server** command to add DHCP servers to the DHCP server group.
* **dhcp relay server-group** command in the VLANIF interface view to specify the DHCP server group for the DHCP relay agent.

Example
-------

# Create a DHCP server group named dhcp-srv1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance dhcp-srv1
[~HUAWEI-vpn-instance-vpn-1] ipv4-family
[~HUAWEI-vpn-instance-vpn-1-af-ipv4] q
[~HUAWEI] dhcp relay server group dhcp-srv1

```
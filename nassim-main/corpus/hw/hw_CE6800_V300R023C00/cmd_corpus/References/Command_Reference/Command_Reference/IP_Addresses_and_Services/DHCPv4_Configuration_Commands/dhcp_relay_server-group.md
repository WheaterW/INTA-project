dhcp relay server-group
=======================

dhcp relay server-group

Function
--------



The **dhcp relay server-group** command configures a DHCP server group for a DHCP relay agent.

The **undo dhcp relay server-group** command deletes the DHCP server group configured for a DHCP relay agent.



By default, no DHCP server group is configured on an interface.


Format
------

**dhcp relay server-group** *group-name*

**undo dhcp relay server-group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a DHCP server group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, and can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot use "-" and "--" as names. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a DHCP relay agent is used to forward DHCP Request messages from DHCP clients to DHCP servers, run the **dhcp relay server-group** command on the DHCP relay agent to configure a DHCP server group. Then configure IP addresses for the DHCP servers in the DHCP server group.

* You can bind multiple VLANIF interfaces to a DHCP server group. However, you can specify only one DHCP server group for each VLANIF interface.
* IP addresses of the DHCP servers in a DHCP server group must not reside on the same network segment as the interface IP address of the DHCP relay agent.

**Prerequisites**

Before running the **dhcp relay server-group** command, perform the following operations:

* A DHCP server group has been created using the **dhcp relay server group** command.
* The DHCP relay function has been enabled using the **dhcp select relay** command.

**Precautions**

If the **dhcp relay server-group** command is run in the same view more than once, the latest configuration overrides the previous one. If you specify a non-existent DHCP server group, the configuration fails, and the earlier configuration takes effect.


Example
-------

# Configure a DHCP server group named group1 on interface 100GE1/0/1 for a DHCP relay agent.
```
<HUAWEI> system-view
[HUAWEI] dhcp relay server group group1
[*HUAWEI-dhcp-server-group-group1] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp relay server-group group1

```
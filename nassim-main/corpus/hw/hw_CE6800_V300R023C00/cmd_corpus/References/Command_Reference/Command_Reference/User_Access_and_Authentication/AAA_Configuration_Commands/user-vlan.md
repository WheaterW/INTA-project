user-vlan
=========

user-vlan

Function
--------



The **user-vlan** command configures a user VLAN in a service scheme.

The **undo user-vlan** command deletes the user VLAN configured in a service scheme.



By default, no user VLAN is configured in a service scheme.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**user-vlan** *vlan-id*

**undo user-vlan**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the ID of a VLAN. | The value is an integer ranging from 1 to 4094. |



Views
-----

Service scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



After creating a service scheme using the service-scheme (AAA view) command, you can run the user-vlan command to configure a user VLAN in the service scheme. The user assigned with the service scheme will be added to the user VLAN and obtain network resources in the VLAN.



**Precautions**



If the user access mode is not multi-share, you must configure the link type of the interface connected to users to hybrid and configure user packets to pass through the interface in untagged mode. After the configuration, this command can take effect.




Example
-------

# Configure user VLAN 100 in the service scheme huawei.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] service-scheme huawei
[*HUAWEI-aaa-service-huawei] user-vlan 100

```
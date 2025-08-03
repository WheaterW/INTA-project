access-operation
================

access-operation

Function
--------



The **access-operation** command configures access operations.

The **undo access-operation** command restores the default configuration.



By default, no access operations are configured.


Format
------

**access-operation** { { **create** | **read** | **update** | **delete** | **exec** } \* | \* }

**undo access-operation**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **create** | Allows data nodes to be created. | - |
| **read** | Allows data nodes, notification alarms, and events to be read. | - |
| **update** | Allows data nodes to be updated. | - |
| **delete** | Allows data nodes to be deleted. | - |
| **exec** | Allows protocol operations to be executed. | - |
| \* | Allows all access operation types. | - |



Views
-----

NACM rule view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure access operations in NACM rules on a device, run the access-operation { { create | read | update | delete | exec } \* | \* } command.


Example
-------

# Configure the operation for a device in the NACM rule named rule1.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] rule-type rpc-name edit-config
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] access-operation exec

```

# Configure the create operation for an ACL in the data node path /huawei-acl:acl in the NACM rule named rule3.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule3 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule3] rule-type path /huawei-acl:acl
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule3] access-operation create

```
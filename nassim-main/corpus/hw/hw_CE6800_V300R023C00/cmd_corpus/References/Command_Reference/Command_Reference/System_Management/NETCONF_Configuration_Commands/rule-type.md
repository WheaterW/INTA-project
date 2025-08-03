rule-type
=========

rule-type

Function
--------



The **rule-type** command specifies a type for an NACM rule.

The **undo rule-type** command deletes the type set for an NACM rule.



By default, no type is specified for an NACM rule.


Format
------

**rule-type** { **rpc-name** *rpc-name* | **notification-name** *notification-name* | **path** *path* }

**undo rule-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rpc-name** *rpc-name* | Specifies a basic protocol operation in an NACM rule. | The value is a string of 1 to 63 characters, which can be get, get-config, edit-config, copy-config, delete-config, lock, unlock, commit, close-session, or kill-session. |
| **notification-name** *notification-name* | Specifies an alarm or event name in a notification NACM rule. | The value is a string of 1 to 63 characters. |
| **path** *path* | Specifies a data node path in a data node NACM rule. | The value is a string of 1 to 1023 characters starting with a slash (/). |



Views
-----

NACM rule view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

NACM rules fall into the following types: protocol operation, notification, and data node, which can be selected as needed. If you want to control user access to a NETCONF operation, specify rpc-name. If you want to control user access to alarms or events reported through the notification mechanism, specify notification-name. If you want to control user access to a data node, specify path.


Example
-------

# Specify rpc-name as the type of the NACM rule named rule1 to allow users to perform the edit-config operation.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] rule-type rpc-name edit-config

```

# Specify notification-name as the type of the NACM rule named rule1 to allow users to perform the notification operation.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] rule-type notification-name netconf-session-start

```

# Specify path as the type of the NACM rule named rule1 to allow users to read a data node.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] rule-type path /huawei-acl:acl

```
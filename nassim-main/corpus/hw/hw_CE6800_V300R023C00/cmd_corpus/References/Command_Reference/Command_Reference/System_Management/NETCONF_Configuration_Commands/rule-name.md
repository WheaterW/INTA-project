rule-name
=========

rule-name

Function
--------



The **rule-name** command sets a name for an NACM rule and displays the rule view.

The **undo rule-name** command deletes the name set for an NACM rule.



By default, no name is set for an NACM rule.


Format
------

**rule-name** *rule-name* **action** { **permit** | **deny** }

**undo rule-name** *rule-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-name* | Specifies the name of an NACM rule. | The value is a string of 1 to 15 case-sensitive characters. |
| **action** | The NACM action to perform. | - |
| **permit** | The NACM rule is permitted. | - |
| **deny** | The NACM rule is denied. | - |



Views
-----

NACM rule list view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

NACM users can use an NACM rule list only when the list contains rules. To set a name for an NACM rule, run the rule-name command. This command also displays the NACM rule view, in which you can configure an NACM rule.

**Follow-up Procedure**

Perform the following operations to configure an NACM rule:

* Run the **module-name** command to specify the name of the feature module that a user can access.
* Run the **rule-type** command to specify a type for an NACM rule.
* Run the access-operation{ { create | read | update | delete | exec } \* | \* } command to configure access operations.

**Precautions**

An NACM rule list can contain more than one NACM rule.When an NACM rule is deleted using the **undo rule-name** command, all the commands run in the rule view are also deleted.


Example
-------

# Configure an NACM rule named rule1 and allow users to execute the permission defined in the rule.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit

```
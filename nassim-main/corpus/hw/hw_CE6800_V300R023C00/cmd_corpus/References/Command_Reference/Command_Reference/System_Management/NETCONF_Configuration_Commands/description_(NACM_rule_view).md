description (NACM rule view)
============================

description (NACM rule view)

Function
--------



The **description** command configures a description for an NACM rule.

The **undo description** command deletes the description of an NACM rule.



By default, no description is configured for an NACM rule.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description of an NACM rule. | The value is a string ranging from 1 to 63. |



Views
-----

NACM rule view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When there are a large number of NACM rules, to allow users to easily learn each rule's function, run the **description** command to configure a description for each rule.


Example
-------

# Configure a description for an NACM rule.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] description nacm-description

```
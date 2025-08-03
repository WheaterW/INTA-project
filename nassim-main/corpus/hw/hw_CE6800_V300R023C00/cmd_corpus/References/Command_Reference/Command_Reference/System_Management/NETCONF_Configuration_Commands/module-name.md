module-name
===========

module-name

Function
--------



The **module-name** command specifies the name of a feature module in an NACM rule.

The **undo module-name** command deletes the name of a feature module in an NACM rule.



By default, the feature module name is an asterisk (\*), indicating all features.


Format
------

**module-name** *module-name*

**undo module-name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *module-name* | Specifies the name of a feature module in an NACM rule. It is also the name of a YANG file. | The value is a string of 1 to 63 characters.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

NACM rule view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To specify the name of a feature module to which a user has access rights in an NACM rule, run the module-name command. This command allows proper feature module management by different users.


Example
-------

# Specify ietf-netconf-acm as the feature module to which a user is given access.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] rule-name rule1 action permit
[*HUAWEI-netconf-nacm-rule-list-list1-rule-name-rule1] module-name ietf-netconf-acm

```
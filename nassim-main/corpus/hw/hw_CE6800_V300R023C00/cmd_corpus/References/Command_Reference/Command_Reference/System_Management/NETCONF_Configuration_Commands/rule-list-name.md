rule-list-name
==============

rule-list-name

Function
--------



The **rule-list-name** command creates an NACM rule list and displays the rule list view.

The **undo rule-list-name** command deletes an NACM rule list.



By default, no NACM rule list is created.


Format
------

**rule-list-name** *list-name*

**undo rule-list-name** *list-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *list-name* | Specifies the name of an NACM rule list. | The value is a string of 1 to 15 case-sensitive characters. |



Views
-----

NACM view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Multiple rules can be defined in an NACM rule list. Users can use these defined rules to obtain permissions. To create an NACM rule list or display the rule list view, run the rule-list-name command.


Example
-------

# Create an NACM rule list named list 1.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] rule-list-name list1

```
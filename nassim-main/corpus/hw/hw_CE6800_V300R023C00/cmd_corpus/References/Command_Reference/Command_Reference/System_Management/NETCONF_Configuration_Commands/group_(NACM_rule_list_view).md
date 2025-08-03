group (NACM rule list view)
===========================

group (NACM rule list view)

Function
--------



The **group** command associates an existent NACM user group with an NACM rule list.

The **undo group** command deletes an existent NACM user group from an NACM rule list.



By default, no NACM user group is associated with an NACM authentication rule list.


Format
------

**group** *group-name*

**undo group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a user group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

NACM rule list view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To allow an NACM user to use the rules in an NACM rule list, create an NACM user group in the NACM view, add the NACM user to the user group, and then run the group command to associate the created NACM user group with the rule list.

**Precautions**

To successfully delete an NACM user group, the user group must have been created.By default, NACM user groups can be created only by users in the administrator groups of the physical system (PS). If users in other user groups want to create NACM user groups, they must first get authorization from the users in the administrator groups through NACM rules.


Example
-------

# Associate the NACM user group named g1 with an NACM rule list.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] group g1
[~HUAWEI-netconf-nacm-group-g1] quit
[~HUAWEI-netconf-nacm] rule-list-name list1
[*HUAWEI-netconf-nacm-rule-list-list1] group g1

```
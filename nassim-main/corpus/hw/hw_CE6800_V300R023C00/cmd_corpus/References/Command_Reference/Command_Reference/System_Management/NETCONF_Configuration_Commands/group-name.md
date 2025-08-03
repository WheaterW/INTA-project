group-name
==========

group-name

Function
--------



The **group-name** command creates an NACM user group and displays the NACM user group view.

The **undo group-name** command deletes an NACM user group.



By default, no NACM user group is created.


Format
------

**group-name** *group-name*

**undo group-name** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of an NACM user group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

NACM view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To allow an NACM user to use the rules in an NACM rule list, run the group-name command to create an NACM user group in the NACM view, add the NACM user to the user group, and then associate the created NACM user group with the rule list.

**Follow-up Procedure**

Run the **group group-name** command in the NACM rule list view to associate the created user group with the NACM rule list.

**Precautions**

To successfully delete an NACM user group, the user group must have been created and is not associated with any NACM authentication rule list.NACM user groups that are not created on the local device in use are not supported.


Example
-------

# Create an NACM user group named g1.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] group-name g1

```
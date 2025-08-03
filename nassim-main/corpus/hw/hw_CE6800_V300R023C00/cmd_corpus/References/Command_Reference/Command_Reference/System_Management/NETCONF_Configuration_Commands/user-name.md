user-name
=========

user-name

Function
--------



The **user-name** command specifies an NACM user for an NACM user group.

The **undo user-name** command deletes an NACM user from an NACM user group.



By default, no NACM user is specified for an NACM user group.


Format
------

**user-name** *user-name*

**undo user-name** *user-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies the name of an NACM user. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

NACM group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To allow an NACM user to use the rules in an NACM rule list, create an NACM user group in the NACM view, run the user-name command to add the NACM user to the user group, and then associate the created NACM user group with the rule list.NACM users must be SSH users that have been created on devices.


Example
-------

# Specify an NACM user named u1 for an NACM user group.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] group-name g1
[*HUAWEI-netconf-nacm-group-g1] user-name u1

```
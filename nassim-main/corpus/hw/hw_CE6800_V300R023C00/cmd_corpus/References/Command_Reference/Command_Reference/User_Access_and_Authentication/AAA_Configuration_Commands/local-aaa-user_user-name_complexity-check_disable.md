local-aaa-user user-name complexity-check disable
=================================================

local-aaa-user user-name complexity-check disable

Function
--------

The **local-aaa-user user-name complexity-check disable** command disables the device from checking whether the user name length of a local administrator is greater than or equal to 6.

The **undo local-aaa-user user-name complexity-check disable** command enables the device to check whether the user name length of a local administrator is greater than or equal to 6.

By default, the complexity check is enabled for local user names.



Format
------

**local-aaa-user user-name complexity-check disable**

**undo local-aaa-user user-name complexity-check disable**



Parameters
----------

None


Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To prevent accounts from being stolen due to simple passwords, run this command to set the length of a local administrator user name to be greater than or equal to 6 characters.

**Precautions**

After the user name complexity check function is disabled, the user name of a local administrator can be set to a string of less than 6 characters. A simple user name, however, has security risks.



Example
-------

# Enable the complexity check for local user names.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] undo local-aaa-user user-name complexity-check disable

```
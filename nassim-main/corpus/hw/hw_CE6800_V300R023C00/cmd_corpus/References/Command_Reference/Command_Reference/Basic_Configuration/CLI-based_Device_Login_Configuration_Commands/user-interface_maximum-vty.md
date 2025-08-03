user-interface maximum-vty
==========================

user-interface maximum-vty

Function
--------



The **user-interface maximum-vty** command sets the maximum number of login users.

The **undo user-interface maximum-vty** command restores the default maximum number of login users.



By default, the maximum number of Telnet and SSH users are 5.


Format
------

**user-interface maximum-vty** *number*

**undo user-interface maximum-vty**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of Telnet and SSH users. | It is an integer data type. Value ranges from 0 to 21. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the VTY node IDs of all login users are less than the configured number of users, the system accepts the configuration. Otherwise, the system displays a message indicating that the configuration is invalid.After the configuration is committed, if all VTY channels are occupied, the device does not allow new users to log in through Telnet or SSH. However, users who have logged in are not affected. Telnet has security risks, and SSH v2 is recommended.


Example
-------

# Set the maximum number of VTY user interfaces to 7.
```
<HUAWEI> system-view
[~HUAWEI] user-interface maximum-vty 7

```
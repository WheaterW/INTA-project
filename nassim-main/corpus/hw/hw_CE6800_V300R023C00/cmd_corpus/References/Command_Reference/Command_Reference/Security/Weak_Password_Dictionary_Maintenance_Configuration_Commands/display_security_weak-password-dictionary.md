display security weak-password-dictionary
=========================================

display security weak-password-dictionary

Function
--------



The **display security weak-password-dictionary** command displays the weak password configured on a device.




Format
------

**display security weak-password-dictionary**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

A device supports the pre-configuration of a weak password dictionary. A user-configured password cannot be the same as any password in the weak password dictionary (completely match). To check the configured weak password, run the display security weak-password-dictionary command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the weak password configured on a device.
```
<HUAWEI> display security weak-password-dictionary
--------------------------------------------------------------------------------
Weak Password
--------------------------------------------------------------------------------
test1
test2
test3
--------------------------------------------------------------------------------
Total: 3

```

**Table 1** Description of the **display security weak-password-dictionary** command output
| Item | Description |
| --- | --- |
| Weak Password | Weak password. |
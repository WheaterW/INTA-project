lock (user view)
================

lock (user view)

Function
--------



The **lock** command locks the current user interface to prevent unauthorized access to the device.




Format
------

**lock**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**



To prevent other users from accessing the device, you can run the **lock** command to lock the user interface. The user interface can be the console interface and VTY interface.



**Implementation Procedure**



After running the **lock** command, you need to enter a password twice as prompted to activate the screen save mode. When entering the same password twice, you successfully lock the current user interface. You must enter a password that meets password complexity requirements.



**Configuration Impact**

After the system is locked, if you attempt to log in to the system, press Enter and then input the correct password as prompted. In this manner, you can unlock the user interface and log in to the system.

**Precautions**

* You cannot log in to the system if forgetting the password. In this case, you must retrieve the password from the administrator or re-configure a password.
* After the system is locked, the user can enter the password to unlock the system. If the user enters incorrect passwords for multiple consecutive times, the system disconnects the current user.
* After the weak password dictionary maintenance function is enabled, the passwords (which can be queried using the **display security weak-password-dictionary** command) defined in the weak password dictionary are unavailable.

Example
-------

# Log in and lock the current user interface.
```
<HUAWEI> lock
Enter Password:
Confirm Password:
Info: The terminal is locked.

```
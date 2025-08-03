display aaa-quiet administrator except-list
===========================================

display aaa-quiet administrator except-list

Function
--------



The **display aaa-quiet administrator except-list** command displays IP addresses that a user can use to access the network when the user account is locked.




Format
------

**display aaa-quiet administrator except-list**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After a user is configured to access the network using a specified IP address when the user account is locked using the **aaa-quiet administrator except-list** command, you can run the display **aaa-quiet administrator except-list** command to check information about the specified IP addresses.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IP addresses that a user can use to access the network when the user account is locked.
```
<HUAWEI> display aaa-quiet administrator except-list
 -------------------------------------------------------------------------------
 Admin silent whitelist (Total: 2)
 -------------------------------------------------------------------------------
 10.2.2.1
 10.2.2.2
 -------------------------------------------------------------------------------

```

**Table 1** Description of the **display aaa-quiet administrator except-list** command output
| Item | Description |
| --- | --- |
| Admin silent whitelist | IP addresses configured in a whitelist. |
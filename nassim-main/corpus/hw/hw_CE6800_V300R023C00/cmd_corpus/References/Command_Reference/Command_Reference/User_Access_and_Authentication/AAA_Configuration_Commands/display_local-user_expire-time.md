display local-user expire-time
==============================

display local-user expire-time

Function
--------



The **display local-user expire-time** command displays the time when local accounts expire.




Format
------

**display local-user expire-time**


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

The command output helps you diagnose and rectify the faults related to the local user password.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the time when local accounts expire.
```
<HUAWEI> display local-user expire-time
 -------------------------------------------------------------------------------    
 Username                Password-expire       Account-expire            Expired
 -------------------------------------------------------------------------------
 zsh                     2014-12-01 21:25:44    -                        NO
 mm001                   2014-12-01 21:29:58    -                        NO
 -------------------------------------------------------------------------------
 Total: 2, printed: 2

```

**Table 1** Description of the **display local-user expire-time** command output
| Item | Description |
| --- | --- |
| Username | Local account name.  To configure this parameter, run the local-user command. |
| Password-expire | Number of days after which the password expires.  To configure this parameter, run the password expire command. |
| Account-expire | Account expiration time.  To configure this parameter, run the local-user expire-date command. |
| Expired | Whether the local account has expired:   * YES. * NO.   The displayed value and actual value may have a difference within one minute; there is a possibility that the password has expired, but the displayed value is NO.  When the local user account or password has expired, the local user becomes invalid. |
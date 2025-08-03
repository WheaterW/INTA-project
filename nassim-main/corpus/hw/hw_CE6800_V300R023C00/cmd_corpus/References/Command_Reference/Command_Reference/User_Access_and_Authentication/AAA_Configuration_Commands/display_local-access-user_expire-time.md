display local-access-user expire-time
=====================================

display local-access-user expire-time

Function
--------



The **display local-access-user expire-time** command displays the time when local access accounts expire.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display local-access-user expire-time**


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

The command output helps you diagnose and rectify the faults related to local access user passwords.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the time when local access accounts expire.
```
<HUAWEI> display local-access-user expire-time
 -------------------------------------------------------------------------------                                                    
 Username                Password-expire           Account-expire        Expired                                                    
 -------------------------------------------------------------------------------                                                    
 11                      -                         -                     No                                                         
 111                     -                         -                     No                                                         
 abc                     -                         -                     No                                                         
 1111                    -                         -                     No                                                         
 dot1x                   -                         -                     No                                                         
 testsss                 -                         -                     No                                                         
 hello@163.net           -                         2021-10-01 00:00:00   No                                                         
 -------------------------------------------------------------------------------                                                    
 Total: 7, printed: 7

```

**Table 1** Description of the **display local-access-user expire-time** command output
| Item | Description |
| --- | --- |
| Username | Local access account name.  To configure this parameter, run the local-access-user (AAA view) command. |
| Password-expire | Number of days after which the password expires.  To configure this parameter, run the password expire command. |
| Account-expire | Account expiration time.  To configure this parameter, run the expire-time command. |
| Expired | Whether the local access account has expired:   * YES. * NO.   The displayed value and actual value may have a difference within one minute; there is a possibility that the password has expired, but the displayed value is NO.  When the local access user account or password has expired, the local user becomes invalid. |
display local-user
==================

display local-user

Function
--------



The **display local-user** command displays information about local users.




Format
------

**display local-user** [ **domain** *domain-name* | **username** *user-name* | **state** { **active** | **block** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **domain** *domain-name* | Displays information about local users in a specified domain. | The domain name must exist. |
| **username** *user-name* | Displays information about a specified local user name. | The value is a string of 1 to 253 case-sensitive characters. It cannot contain spaces. |
| **state** | Indicates the status of the local user. | - |
| **active** | Indicates the active state. | - |
| **block** | Indicates the blocking state. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The command output helps you check the configuration of local users and isolate faults related to the local users.

**Precautions**

If no parameter is specified, brief information about all local users is displayed. If a parameter is specified, detailed information about the specified local user is displayed.Low-level users cannot view information about high-level users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the local user user1 who fails to log in to the device.
```
<HUAWEI> display local-user username user1
  The contents of local user(s):                                                                                                    
  Password             : ****************                                                                                           
  State                : active                                                                                                     
  Service-type-mask    : T                                                                                                          
  Privilege level      : 0                                                                                                          
  Ftp-directory        : -       
  Ftp-access-permission: -                                                                                                       
  HTTP-directory       : -                                                                                                          
  Access-limit         : -                                                                                                          
  Accessed-num         : 0                                                                                                          
  Idle-timeout         : -  
  Password-force-change: Yes                                                                                                        
  Retry-interval       : 4 Min(s)                                                                                                   
  Retry-time-left      : 1                                                                                                          
  Original-password    : Yes                                                                                                        
  Password-set-time    : 2019-01-27 13:26:55+08:00                                                                                  
  Password-expired     : No                                                                                                         
  Password-expire-time : -                                                                                                          
  Account-expire-time  : -

```

# Display information about local user user1 whose password (first configured) fails to be changed.
```
<HUAWEI> display local-user username user1
  The contents of local user(s):                                                                                                    
  Password             : ****************                                                                                           
  State                : active                                                                                                     
  Service-type-mask    : T                                                                                                          
  Privilege level      : 0                                                                                                          
  Ftp-directory        : -    
  Ftp-access-permission: -                                                                                                         
  HTTP-directory       : -                                                                                                          
  Access-limit         : -                                                                                                          
  Accessed-num         : 1                                                                                                          
  Idle-timeout         : -  
  Password-force-change: Yes                                                                                                   
  Change password retry-interval  : 4 Min(s)                                                                                        
  Change password retry-count-left: 3                                                                                               
  Original-password    : Yes                                                                                                        
  Password-set-time    : 2019-01-27 13:26:55+08:00                                                                                  
  Password-expired     : No                                                                                                         
  Password-expire-time : -                                                                                                          
  Account-expire-time  : -

```

# Display information about local users in blocking state.
```
<HUAWEI> display local-user state block
  ----------------------------------------------------------------------------                                                      
  User-name                      State  AuthMask  AdminLevel  BlockTime                                                             
  ----------------------------------------------------------------------------                                                      
  test2                          B      T         0           2018-04-10 01:55:11-00:00                                             
  ---------------------------------------------------------------------------- 
  Total 1 user(s)

```

# Display information about local user test2 in blocking state.
```
<HUAWEI> display local-user state block username test2
  The contents of local user(s):                                                                                                    
  Password             : ****************                                                                                           
  State                : block                                                                                                      
  Service-type-mask    : T                                                                                                          
  Privilege level      : 0                                                                                                          
  Ftp-directory        : -     
  Ftp-access-permission: -                                                                                                        
  HTTP-directory       : -                                                                                                          
  Access-limit         : -                                                                                                          
  Accessed-num         : 0                                                                                                          
  Idle-timeout         : -    
  Password-force-change: Yes                                                                                             
  Block-time-left      : 8 Min(s)                                                                                                   
  Original-password    : Yes                                                                                                        
  Password-set-time    : 2019-01-27 13:26:55+08:00                                                                                  
  Password-expired     : No                                                                                                         
  Password-expire-time : -                                                                                                          
  Account-expire-time  : -

```

# Display brief information about all local users.
```
<HUAWEI> display local-user
  ----------------------------------------------------------------------------
  User-name                      State  AuthMask  AdminLevel
  ----------------------------------------------------------------------------
  user-a                         A      A         0
  user-c                         A      A         0
  ----------------------------------------------------------------------------
  Total 2 user(s)

```

# Display detailed information about the local user user-a.
```
<HUAWEI> display local-user username user-a
  The contents of local user(s):
  Password             : ****************
  State                : active
  Service-type-mask    : A
  Privilege level      : -
  Ftp-directory        : -
  Ftp-access-permission: -   
  HTTP-directory       : -       
  Access-limit         : Yes
  Access-limit-max     : 4294967295
  Accessed-num         : 0
  Idle-timeout         : -
  Password-force-change: Yes
  Original-password    : No
  Password-set-time    : 2019-12-01 18:42:57+01:00 DST
  Password-expired     : No 
  Password-expire-time : - 
  Account-expire-time  : -   
  Last login ip        : 192.168.240.235
  Last login time      : 2019-03-21 09:38:24+08:00
  Login fail count     : 0

```

**Table 1** Description of the **display local-user** command output
| Item | Description |
| --- | --- |
| Password | Password of the local user. |
| State | State of the local user:  A: Active.  B: Block. |
| Service-type-mask | Service type of the local user. Same as the AuthMask type. |
| Privilege level | Local user level. |
| Ftp-directory | FTP directory of the local user. |
| HTTP-directory | HTTP directory of the local user.  To configure this parameter, run the local-user command. |
| Access-limit | Whether the maximum number of sessions of the local user is configured. |
| Accessed-num | Number of established sessions. |
| Idle-timeout | Idle timeout interval. |
| Retry-interval | Login retry interval before a local user is locked. |
| Retry-time-left | Remaining number of login retries before a local user is locked. |
| Original-password | Whether the password of a local user is the first configured password. |
| Password-set-time | Time when the local user's password is created. The value is in format local time + DST offset. |
| Password-expired | Whether a local user password has expired. |
| Password-expire-time | Time when the local user's password expires. The value is in format local time + DST offset. |
| Account-expire-time | Expiry time of a local user account. The value is in format local time + DST offset. |
| Change password retry-interval | Retry interval for retrying an incorrect password of a local user before the user is locked. |
| Change password retry-count-left | Remaining number of retrying password change retries before a local user is locked. |
| User-name | Name of the local user. |
| AuthMask | Access type of the local user. |
| AdminLevel | Local user level. |
| Access-limit-max | Maximum number of sessions of the local user. |
| Last login ip | IP address for user login.  This item can be displayed only for administrators. |
| Last login time | User login time.  This item can be displayed only for administrators. |
| Login fail count | Number of user login failures.  This item can be displayed only for administrators. |
| Ftp-access-permission | FTP access permission. |
| BlockTime/Block-time-left | Remaining time of locked local users. (Local users are locked because the entered password is incorrect consecutively.). |
| Password-force-change | When a local administrator logs in to the system for the first time, the system forces the administrator to change the password. |
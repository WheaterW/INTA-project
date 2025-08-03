display local-access-user
=========================

display local-access-user

Function
--------



The **display local-access-user** command displays information about local access users.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display local-access-user** [ **username** *user-name* | **domain** *domain-name* | **state** { **active** | **block** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **username** *user-name* | Displays information about a specified local access user name. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| **domain** *domain-name* | Displays information about local access users in a specified domain. | The value is a string of 1 to 64 case-insensitive characters. It cannot contain spaces.  The value must be an existing domain name. |
| **state** | Displays the attributes of local access users in the specified state. | - |
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

The command output helps you check the configuration of local access users and isolate faults related to the local access users.

**Precautions**

If no parameter is specified, brief information about all local access users is displayed. If a parameter is specified, detailed information about the specified local access user is displayed.Low-level users cannot view information about high-level users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the local access user user-a.
```
<HUAWEI> display local-access-user username user-a
  The contents of local access user(s):                                                                                             
  Password             : ****************                                                                                           
  State                : active                                                                                                     
  Service-type-mask    : -                                                                                                          
  Access-limit         : Yes                                                                                                        
  Access-limit-max     : 4294967295                                                                                                 
  Accessed-num         : 0                                                                                                          
  Original-password    : No                                                                                                         
  Password-set-time    : 2021-11-18 14:31:50                                                                                        
  Password-expired     : No                                                                                                         
  Password-expire-time : -                                                                                                          
  Account-expire-time  : -                                                                                                          
  Local Access User ID : 1                                                                                                          
  Service-scheme       : -                                                                                                          
  UCL group(s)         : -

```

# Display brief information about local access users.
```
<HUAWEI> display local-access-user
  Total 7 user(s)                                                                                                                   
  ----------------------------------------------------------------                                                                  
  User-name                      State  AuthMask                                                                                    
  ----------------------------------------------------------------                                                                  
  11                             A      -                                                                                           
  111                            A      X                                                                                           
  abc                            A      X                                                                                           
  1111                           A      -                                                                                           
  dot1x                          A      X                                                                                           
  testsss                        A      -                                                                                           
  hello@163.net                  A      -                                                                                           
  ----------------------------------------------------------------

```

**Table 1** Description of the **display local-access-user** command output
| Item | Description |
| --- | --- |
| Password | Password of the local access user. |
| State | State of the local access user:  A: Active.  B: Block. |
| Service-type-mask | Service type of the local access user. Same as the AuthMask type. |
| Access-limit | Whether the maximum number of sessions of the local access user is configured. |
| Access-limit-max | Maximum number of sessions of the local access user. |
| Accessed-num | Number of established sessions. |
| Original-password | Whether the password of a local access user is the first configured password. |
| Password-set-time | Time when the local access user's password is created. The value is the local time with the DST time zone. |
| Password-expired | Whether a local access user password has expired. |
| Password-expire-time | Time when the local access user's password expires. The value is the local time with the DST time zone. |
| Account-expire-time | Expiry time of a local access user account. The value is the local time with the DST time zone. |
| Local Access User ID | Access user ID. |
| Service-scheme | User of the service scheme of the access user. |
| UCL group | UCL group name of access users. |
| User-name | Name of the local access user. |
| AuthMask | Access type of the local access user. |
| Time-range | Access time range of the local access account. |
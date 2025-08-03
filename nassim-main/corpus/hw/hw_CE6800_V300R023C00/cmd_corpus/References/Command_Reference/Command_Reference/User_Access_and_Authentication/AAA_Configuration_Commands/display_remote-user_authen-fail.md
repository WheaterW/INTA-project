display remote-user authen-fail
===============================

display remote-user authen-fail

Function
--------



The **display remote-user authen-fail** command displays the accounts that fail in remote AAA authentication.




Format
------

**display remote-user authen-fail** [ **blocked** | **username** *username* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **blocked** | Displays all the remote AAA authentication accounts that have been locked. | - |
| **username** *username* | Displays details about the accounts that fail in remote AAA authentication.  If the username parameter is not specified, basic information about all accounts that fail in remote AAA authentication is displayed. | The value is a string of 1 to 253 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the account locking function is enabled for the users who fail in AAA remote authentication, the device records all failed accounts, including:

* The accounts that failed in authentication and are locked, for example, when the user entered the wrong account name or password too many times.
* The accounts that failed in authentication, but are not locked, for example, when the number of times the account name or password was entered incorrectly did not exceed the limit.

**Prerequisites**

The function of locking an account after the remote AAA authentication fails is enabled.

**Precautions**

The device cannot back up a recorded account that fails the AAA authentication. If an active/standby switchover policy has been configured on the device, all user entries are cleared when the device completes an active/standby switchover.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all accounts that have failed in remote AAA authentication.
```
<HUAWEI> display remote-user authen-fail
  Interval: Retry Interval(Mins)                                                                                                    
  TimeLeft: Retry Time Left                                                                                                         
  BlockDuration: Block Duration(Mins)                                                                                               
  -------------------------------------------------------------------------------------------                                       
  Username                   Interval  TimeLeft  BlockDuration                                                                      
  -------------------------------------------------------------------------------------------                                       
  www@test                   0         0         65414                                                                              
  -------------------------------------------------------------------------------------------                                       
  Total 1, 1 printed

```

# Display all locked accounts.
```
<HUAWEI> display remote-user authen-fail blocked
  Interval: Retry Interval(Mins)                                                                                                    
  TimeLeft: Retry Time Left                                                                                                         
  BlockDuration: Block Duration(Mins)                                                                                               
  -------------------------------------------------------------------------------------------                                       
  Username                   Interval  TimeLeft  BlockDuration  BlockTime                                                           
  -------------------------------------------------------------------------------------------                                       
  www@test                   0         0         65414          2018-04-23 17:22:09+08:00                                           
  -------------------------------------------------------------------------------------------                                       
  Total 1, 1 printed

```

# Display details about the account test that failed in remote AAA authentication.
```
<HUAWEI> display remote-user authen-fail username test
  The contents of the user:
  Retry-interval    : 0 Min(s)
  Retry-time-left   : 0
  Block-time-left   : 4 Min(s)
  User-state        : Block

```

**Table 1** Description of the **display remote-user authen-fail** command output
| Item | Description |
| --- | --- |
| Interval: RetryInterval(Mins) | Authentication retry interval, in minutes.  To configure this parameter, run the remote-aaa-user authen-fail command. |
| TimeLeft: Retry Time Left | Remaining number of consecutive authentication failures.  To configure this parameter, run the remote-aaa-user authen-fail command. |
| BlockDuration: Block Duration(Mins) | User account locking duration, in minutes.  To configure this parameter, run the remote-aaa-user authen-fail command. |
| Username | User name. |
| BlockTime | User account locking time. |
| Retry-interval | Remaining number of consecutive authentication failures.  To configure this parameter, run the remote-aaa-user authen-fail command. |
| Retry-time-left | Remaining number of consecutive authentication failures.  To configure this parameter, run the remote-aaa-user authen-fail command. |
| Block-time-left | Remaining locking time of an account. |
| User-state | User status:  Block.  Active. |
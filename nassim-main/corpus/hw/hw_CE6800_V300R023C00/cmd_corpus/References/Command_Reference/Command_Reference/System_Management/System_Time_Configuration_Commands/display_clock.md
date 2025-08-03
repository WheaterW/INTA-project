display clock
=============

display clock

Function
--------



The **display clock** command displays the current date and time.




Format
------

**display clock**

**display clock utc**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **utc** | Indicates the Universal Time Coordinated (UTC) time. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the current date and time on a device, run the **display clock** command. The command output helps you check whether the system time is correct and whether the time needs to be adjusted.If you have set the daylight saving time using the clock daylight-saving-time command, run the **display clock** command to view information about the summer time. If you do not set the daylight saving time before using the **display clock** command, summer time information is not displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the current date and time on a device.
```
<HUAWEI> display clock
2020-02-02 17:02:34+08:00                                                       
Tuesday                                                                         
Time Zone(BJ) : UTC+08:00                                                       
Daylight saving time    :                                                       
         Name           :  BJ                                                   
         Repeat mode    :  one-year                                             
         Start year     :  2020                                                 
         End year       :  2020                                                 
         Start time     :  02-01 11:22:00                                       
         End time       :  08-11 22:11:00                                       
         Saving time    :  01:04:00

```

**Table 1** Description of the **display clock** command output
| Item | Description |
| --- | --- |
| Time Zone(BJ) | BJ time zone is used. |
| Daylight saving time | DST.  You can run the display clock command to view information about the DST only after the DST is configured using the clock daylight-saving-time command. |
| Name | Name of the DST time zone. |
| Repeat mode | DST configuration mode.   * one-year: The DST configuration is valid within a year. * repeating: The DST is used periodically. |
| Start year | Start year. |
| Start time | Start time. |
| End year | End year. |
| End time | End time. |
| Saving time | Time offset after the DST is used. |
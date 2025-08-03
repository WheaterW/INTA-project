ntp offset-limit
================

ntp offset-limit

Function
--------



The **ntp offset-limit** command sets the offset threshold for clock synchronization. If the time offset between the clock source and the client is greater than the offset threshold, the client does not synchronize the time of the clock source.

The **undo ntp offset-limit** command deletes the clock synchronization offset threshold.



By default, no offset threshold is set for clock synchronization on a client.


Format
------

**ntp offset-limit** *maxOffset*

**undo ntp offset-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *maxOffset* | Indicates the offset threshold for time synchronization. | The value is an integer ranging from 5 to 7620, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **ntp offset-limit** command provides extra security for users. If the time offset between the device and the clock source is greater than the value of offset-time, the device does not synchronize the time with the clock source.



**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp server disable/ntp ipv6 server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp server disable/undo ntp ipv6 server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp server disable/ntp ipv6 server disable command from the configuration file when you delete this command.




Example
-------

# Set the offset threshold for clock synchronization to 1000 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ntp offset-limit 1000

```
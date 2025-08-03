ntp discard
===========

ntp discard

Function
--------



The **ntp discard** command configures the minimum inter-packet interval and average minimum inter-packet interval.

The **undo ntp discard** command deletes the minimum inter-packet interval and average minimum inter-packet interval.



The default minimum inter-packet interval is 1, and the default average minimum packet interval is 5.


Format
------

**ntp discard** { **min-interval** *min-interval-val* | **avg-interval** *avg-interval-val* } \*

**undo ntp discard**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-interval** *min-interval-val* | Specifies the minimum inter-packet spacing. | The value ranges from 1 to 8, in seconds. The actual minimum interval for sending packets is the nth power of 2, in seconds. |
| **avg-interval** *avg-interval-val* | Specifies the average inter-packet spacing. | The value ranges from 1 to 8, in seconds. The actual average interval for sending packets is the nth power of 2, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To set the global minimum inter-packet interval and average minimum inter-packet interval, run the **ntp discard** command, which is used to generate the RATE kiss code.



**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp server disable/ntp ipv6 server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp server disable/undo ntp ipv6 server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp server disable/ntp ipv6 server disable command from the configuration file when you delete this command.




Example
-------

# Set the minimum-interval to 4 and average-interval to 4.
```
<HUAWEI> system-view
[~HUAWEI] ntp discard min-interval 4 avg-interval 4

```
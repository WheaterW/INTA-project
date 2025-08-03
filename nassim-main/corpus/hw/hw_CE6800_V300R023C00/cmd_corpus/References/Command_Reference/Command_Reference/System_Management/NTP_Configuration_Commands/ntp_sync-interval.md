ntp sync-interval
=================

ntp sync-interval

Function
--------



The **ntp sync-interval** command sets the time interval at which the client clock is updated.

The **undo ntp sync-interval** command deletes the interval period.



By default, the time interval for updating the client clock is not set.


Format
------

**ntp sync-interval** *interval*

**undo ntp sync-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the time interval for updating a clock. | The value is an integer ranging from 180 to 600 seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the interval at which the client clock is updated, run this command.

**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp server disable and ntp ipv6 server disable commands to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp server disable or **undo ntp ipv6 server disable** command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp server disable and ntp ipv6 server disable commands from the configuration file when you delete this command.




Example
-------

# Set the update interval to 180 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ntp sync-interval 180

```
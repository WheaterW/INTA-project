ntp refclock-master
===================

ntp refclock-master

Function
--------



The **ntp refclock-master** command configures a local clock to be the NTP master clock that provides the synchronizing time for other devices.

The **undo ntp refclock-master** command deletes the configuration of the NTP master clock.



By default, no NTP master clock is specified.


Format
------

**ntp refclock-master** [ *ip-address* ] [ *stratum* ]

**undo ntp refclock-master** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of the local clock 127.127.t.u. | Value 't' is an integer ranging from 0 to 37. Here 't' indicates the local reference clock, and its value is 1. 'u' indicates number of NTP processes. Value 'u' is an integer ranging from 0 to 3. If no IP address is specified, by default, the local clock 127.127.1.0 is considered as the NTP master clock. |
| *stratum* | Specifies the stratum of an NTP master clock. | The value is an integer that ranges from 1 to 15. The default value is 8. A smaller value indicates a higher stratum, which allows for more accurate time. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure the local clock as the NTP master clock to provide a clock source for other devices, run the **ntp refclock-master** command.



**Precautions**

If a clock server is configured for a local device, the following situations occur:

* If the local clock stratum value is higher than that of the clock source provided by the clock server, the device takes the clock source provided by the clock server.
* If the local clock stratum value is lower than or the same as that of the clock source provided by the clock server, the device takes the value of the local clock.If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command in the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file.


Example
-------

# Set the local clock to be the NTP master clock with the stratum of 3.
```
<HUAWEI> system-view
[~HUAWEI] ntp refclock-master 3

```
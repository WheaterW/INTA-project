ntp max-distance
================

ntp max-distance

Function
--------



The **ntp max-distance** command configures the maximum NTP synchronization distance threshold.

The **undo ntp max-distance** command restores the default value.



By default, the maximum NTP synchronization distance threshold is 1.


Format
------

**ntp max-distance** *max-distance-value*

**undo ntp max-distance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-distance-value* | Indicates the maximum NTP synchronization distance threshold. | The value is an integer ranging from 1 to 16 seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **ntp max-distance** command is used on the client side for NTP to calculate the synchronization distance to each NTP server. After the calculation is complete, NTP compares the synchronization distance with the maximum synchronization distance threshold. If the synchronization distance exceeds the threshold, the client will not consider the associated server for clock synchronization.



**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp server disable/ntp ipv6 server disable command to the configuration file to disable the NTP server function. To enable the NTP service, run the undo ntp server disable/undo ntp ipv6 server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp server disable/ntp ipv6 server disable command from the configuration file when you delete this command.




Example
-------

# Set the maximum distance threshold to 16.
```
<HUAWEI> system-view
[~HUAWEI] ntp max-distance 16

```
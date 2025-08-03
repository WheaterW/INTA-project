dhcp snooping user-alarm percentage
===================================

dhcp snooping user-alarm percentage

Function
--------



The **dhcp snooping user-alarm percentage** command configures the alarm thresholds for the percentage of DHCP snooping binding entries.

The **undo dhcp snooping user-alarm percentage** command restores the default alarm thresholds for the percentage of DHCP snooping binding entries.



By default, the lower alarm threshold for the percentage of DHCP snooping binding entries is 50, and the upper alarm threshold for the percentage of DHCP snooping binding entries is 100.


Format
------

**dhcp snooping user-alarm percentage** *percent-lower-value* *percent-upper-value*

**undo dhcp snooping user-alarm percentage**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *percent-lower-value* | Specifies the lower alarm threshold for the percentage of DHCP snooping binding entries. | The value is an integer, ranging from 1 to 100. |
| *percent-upper-value* | Specifies the upper alarm threshold for the percentage of DHCP snooping binding entries. | The value is an integer that ranges from 1 to 100, but must be larger than or equal to the lower alarm threshold. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the **dhcp snooping user-bind max-number** command to set the maximum number of DHCP snooping binding entries on an interface, you can run the **dhcp snooping user-alarm percentage** command to set the alarm thresholds for the percentage of DHCP snooping binding entries. When the percentage of learned DHCP snooping binding entries against the maximum number of DHCP snooping entries allowed by the device reaches or exceeds the upper alarm threshold, the device generates an alarm. When the percentage of learned DHCP snooping binding entries against the maximum number of DHCP snooping entries allowed by the device reaches or falls below the lower alarm threshold later, the device generates a clear alarm. The upper alarm threshold is the sum of DHCPv4 and DHCPv6 alarm thresholds.


Example
-------

# Set the lower alarm threshold for the percentage of DHCP snooping binding entries to 30 and the upper alarm threshold to 80.
```
<HUAWEI> system-view
[~HUAWEI] dhcp snooping user-alarm percentage 30 80

```
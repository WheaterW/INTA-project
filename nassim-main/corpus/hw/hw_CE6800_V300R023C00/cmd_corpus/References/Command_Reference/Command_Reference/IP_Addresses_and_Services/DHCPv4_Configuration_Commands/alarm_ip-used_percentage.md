alarm ip-used percentage
========================

alarm ip-used percentage

Function
--------

The **alarm ip-used percentage** command configures the percentage of the alarms indicating that the addresses in an address pool are used up, and the percentage of the clear alarms.

The **undo alarm ip-used percentage** command restores the default percentages of the alarms and clear alarms.

By default, the percentage of the alarms indicating that the addresses in an IP address pool are used up is 100%, and the percentage of the clear alarms is 50%.



Format
------

**alarm ip-used percentage** *alarm-resume-percentage* *alarm-percentage*

**undo alarm ip-used percentage**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *alarm-resume-percentage* | Specifies the percentage of the clear alarms. | The value is an integer that ranges from 1 to 100. The default value is 50. |
| *alarm-percentage* | Specifies the percentage of the alarms indicating that the addresses in an address pool are used up. | The value is an integer in the range from 1 to 100, in percentage. The default value is 100. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

When the addresses in an interface address pool are used up, alarms are sent to notify the administrator.

**Prerequisites**

A global IP address pool has been created using the ip pool command.

**Precautions**

The percentage of the clear alarms cannot exceed that of the alarms.



Example
-------

# Configure the percentage of the alarms indicating that the addresses in an address pool are used up, and the percentage of the clear alarms in the IP address pool view.
```
<HUAWEI> system-view
[~HUAWEI] ip pool p1
[*HUAWEI-ip-pool-p1] alarm ip-used percentage 80 90

```
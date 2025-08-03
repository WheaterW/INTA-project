display ntp slot-status
=======================

display ntp slot-status

Function
--------

The **display ntp slot-status** command displays the status of the clock system of a device.



Format
------

**display ntp slot-status**



Parameters
----------

None


Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

Based on the status of the time service feature, you can view the synchronization status of the local clock system on the device.



Example
-------

# Display the synchronization status of the local clock.
```
<HUAWEI> display ntp slot-status
Slot ID               : *
Sync Source           : 127.127.1.0
NTP Server Configured : No
Clock Status          : synchronized
Offset                : 0.7 ms
Clock Precision       : 217
Poll                  : 8
Reference Time        : 08:23:58.496 UTC Apr 9 2020(E2395A1E.7F179BFD)
Current Time          : 08:23:58.173 UTC Apr 9 2020(E2395A1E.2C5C0336)

```


**Table 1** Description of the
**display ntp slot-status** command output

| Item | Description |
| --- | --- |
| Sync Source | Board source of synchronization. |
| NTP Server Configured | Whether NTP server is configured or not:   * Yes. * No. |
| Clock Status | Status of the clock.   * synchronized. * unsynchronized. |
| Clock Precision | Clock precision. |
| Offset | Clock offset, in ms. |
| Poll | Interval at which the device sends packets to the clock synchronization source. |
| Reference Time | Last synchronized time of the clock. |
| Current Time | Current time in the clock. |
| Slot ID | Slot ID. |
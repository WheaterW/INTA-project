display ntp trace
=================

display ntp trace

Function
--------

The **display ntp trace** command displays the path to a reference clock source.



Format
------

**display ntp trace**



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

To check brief information about each NTP server from the local device to the reference clock source along the NTP server chain for time synchronization, run the **display ntp trace** command.

The IPv6 clock source does not support the
**display ntp trace** command.

Example
-------

# Display summary information on each passing NTP server when a device traces a path to a reference clock source.
```
<HUAWEI> display ntp trace
server 127.0.0.1, stratum 5, offset 0.024099 s, synch distance 0.06337
server 172.16.1.2, stratum 4, offset 0.028786 s, synch distance 0.04575
server 10.1.1.2, stratum 3, offset 0.035199 s, synch distance 0.03075
server 10.1.7.1, stratum 2, offset 0.039855 s, synch distance 0.01096
refid 127.127.1.0

```


**Table 1** Description of the
**display ntp trace** command output

| Item | Description |
| --- | --- |
| server | IP address of an NTP server. |
| stratum | Clock stratum on the NTP server. |
| offset | Offset to the superior reference clock. |
| synch distance | Synchronization distance to the superior reference clock.  This parameter evaluates and describes the reference clock, and NTP selects the reference clock with the shortest synchronization distance. |
| refid | Reference clock source. |
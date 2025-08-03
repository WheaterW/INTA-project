display ntp status
==================

display ntp status

Function
--------

The **display ntp status** command displays the NTP status.



Format
------

**display ntp status**



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

By viewing the NTP service status, you can learn about the clock synchronization status and clock hierarchy of the local node.

If multiple clock servers are configured, the clock server with the highest clock stratum is preferentially synchronized.

Example
-------

# Display the status of the NTP service.
```
<HUAWEI> display ntp status
 clock status: synchronized
 clock stratum: 2
 reference clock ID: LOCAL(0)
 nominal frequency: 60.0002 Hz
 actual frequency: 60.0002 Hz
 clock precision: 218
 clock offset: 0.0000 ms
 root delay: 0.00 ms
 root dispersion: 0.00 ms
 peer dispersion: 10.00 ms
 reference time: 15:51:36.259 UTC Apr 25 2020(C6179088.426490A3)
 synchronization state: clock synchronized

```


**Table 1** Description of the
**display ntp status** command output

| Item | Description |
| --- | --- |
| clock status | Clock status:   * synchronized: The local system clock is synchronized with an NTP server or a reference clock. * unsynchronized: The local system clock is not synchronized with any NTP server. |
| clock stratum | Stratum of the local system clock.  If the clock status is unsynchronized, the stratum value is 16. |
| clock precision | Precision of the local system clock. |
| clock offset | Offset between the local system clock and the NTP server. |
| reference clock ID | Reference clock:   * Reference clock: If the local system clock has been synchronized with a remote NTP server or a reference clock, this field displays the identifier of the remote NTP server or reference clock. * If the local system clock acts as a reference clock, this field displays "LOCAL". * If the clock status is unsynchronized, this field displays "none". |
| reference time | Last corrected system clock time. |
| nominal frequency | Nominal frequency of the local system clock. |
| actual frequency | Actual frequency of the local system clock. |
| root delay | Total delay between the local system clock and master reference clock. |
| root dispersion | Total dispersion between the local system clock and master reference clock. |
| peer dispersion | Dispersion between the local system clock and the remote NTP peer. |
| synchronization state | Clock synchronization status.   * clock not set: indicates that no clock has been set. * frequency set by configuration: indicates that the clock frequency is obtained from configuration information. * clock set: indicates that a local clock has been set. * clock set but frequency not determined: indicates that a clock has been set, but the frequency has not been determined yet. * clock synchronized: indicates that clock signals have been synchronized. * spike (clock will be set in 600 secs): indicates that the time difference will be deleted in 128 milliseconds, and the clock change will take effect in 600 seconds. The 600-second period is not fixed and may be changed in different situations. |
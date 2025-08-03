display ntp sessions
====================

display ntp sessions

Function
--------

The **display ntp sessions** command displays brief information about all local NTP sessions.



Format
------

**display ntp sessions**



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

To check brief session information, run this command.



Example
-------

# Display detailed information about local NTP sessions.
```
<HUAWEI> display ntp sessions
clock source: 10.1.1.1
 clock stratum: 8
 clock status: configured, master, sane, valid
 reference clock ID: LOCAL(0)
 reach: 255
 current poll: 1024
 now: 355
 offset: 0.5995 ms
 delay: 3.01 ms
 disper: 25.42 ms

```


**Table 1** Description of the
**display ntp sessions** command output

| Item | Description |
| --- | --- |
| clock stratum | When the clock status is unsynchronized, the NTP stratum of the local system is 16.Stratum of a peer clock. |
| clock status | Clock status.   * master: The clock source corresponding to a specified session is the primary clock source of the current system. * peer: The clock source corresponding to a specified session is synchronized in peer mode. * selected: The clock source corresponding to a specified session passes the clock selection algorithm but is not selected as a candidate clock source. * candidate: The clock source corresponding to a specified session is a candidate clock source. * configured: The clock source corresponding to a specified session is configured using a command. * vpn-instance: A VPN instance is configured for the clock source corresponding to a specified session. * dynamic: The clock source corresponding to a specified session is configured dynamically. * sane: The clock source corresponding to a specified session passes the saneness test. * insane: The clock source corresponding to a specified session does not pass the saneness test. * valid: The clock source corresponding to a specified session is valid. For example, the clock source passes the saneness test, is in a synchronized state, or has a valid stratum, or the root delay and root dispersion are within the normal ranges. * invalid: The clock source corresponding to a specified session is invalid. * unsynced: The clock source corresponding to a specified session is not synchronized or has an invalid stratum. * conflicted: The clock source corresponding to a specified session is conflicted. |
| clock source | IP address, NEID or domain name of a reference clock. |
| reference clock ID | IP address of the remote server or identifier of the reference clock with which the peer system clock has been synchronized. |
| current poll | Poll interval. |
| reach | Reachability of the configured server or peer. |
| now | Time since NTP packet is not received or last synchronized. |
| offset | Offset between the local system clock and peer for the last received packet. |
| delay | Delay between the local system clock and peer for the last received packet. |
| disper | Dispersion between the local system clock and peer for the last received packet. |
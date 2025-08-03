display ntp sessions verbose
============================

display ntp sessions verbose

Function
--------

The **display ntp sessions verbose** command displays information about local Network Time Protocol (NTP) sessions.



Format
------

**display ntp sessions verbose**



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

To check information about all sessions maintained by the local NTP service, run this command.



Example
-------

# Display detailed information about local NTP sessions.
```
<HUAWEI> display ntp sessions verbose
 clock source: 127.127.1.0 
 clock stratum: 0
 clock status: configured, master, sane, valid
 reference clock ID: LOCAL(0)
 local mode: client, local poll: 2, current poll: 2
 peer mode: server, peer poll: 2, now: 0
 offset: 0.0000 ms, delay: 0.00 ms, disper: 0.08 ms
 root delay: 0.00 ms, root disper: 10.00 ms
 reach: 255, sync dist: 0.010, sync state: 4
 precision: 217, version: 3, peer interface: InLoopBack0
 reftime: 09:49:15.493 UTC Mar 24 2020(E224561B.7E379B77)
 orgtime: 09:49:15.493 UTC Mar 24 2020(E224561B.7E379B77)
 rcvtime: 09:49:15.493 UTC Mar 24 2020(E224561B.7E383276)
 xmttime: 09:49:15.493 UTC Mar 24 2020(E224561B.7E36F3B2)
 filter delay :  0.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 
 filter offset:  0.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 
 filter disper:  0.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 
 reference clock status: normal

```


**Table 1** Description of the
**display ntp sessions verbose** command output

| Item | Description |
| --- | --- |
| clock stratum | Stratum of a peer clock. |
| clock status | Clock status.   * master: The clock source corresponding to a specified session is the primary clock source of the current system. * peer: The clock source corresponding to a specified session is synchronized in peer mode. * selected: The clock source corresponding to a specified session passes the clock selection algorithm but is not selected as a candidate clock source. * candidate: The clock source corresponding to a specified session is a candidate clock source. * configured: The clock source corresponding to a specified session is configured using a command. * vpn-instance: A VPN instance is configured for the clock source corresponding to a specified session. * dynamic: The clock source corresponding to a specified session is configured dynamically. * sane: The clock source corresponding to a specified session passes the saneness test. * insane: The clock source corresponding to a specified session does not pass the saneness test. * valid: The clock source corresponding to a specified session is valid. For example, the clock source passes the saneness test, is in a synchronized state, or has a valid stratum, or the root delay and root dispersion are within the normal ranges. * invalid: The clock source corresponding to a specified session is invalid. * unsynced: The clock source corresponding to a specified session is not synchronized or has an invalid stratum. * conflicted: The clock source corresponding to a specified session is conflicted. |
| clock source | IP address, NEID or domain name of a reference clock. |
| reference clock ID | IP address of the remote server or identifier of the reference clock with which the peer system clock has been synchronized. |
| reference clock status | Reference Clock Source Status. |
| local mode | Clock mode of a local system:   * client: The peer clock can synchronize with a local clock, but the local clock cannot synchronize with the peer clock. * server: The local clock can synchronize the peer clock but peer clock cannot synchronize local clock. * active: The local clock can get synchronized to its peer clock, and the peer clock can get synchronized to local clock based on a larger stratum value. The synchronization request is first sent by the local clock. * passive: The local clock can get synchronized to its peer clock, and the peer clock can get synchronized to local clock based on a larger stratum value. The synchronization request is first sent by the peer clock. * broadcast: The local clock is in broadcast server mode. * broadcast client: The local clock is in broadcast client mode. * unspecified: The field is unspecified. |
| local poll | Local poll. |
| current poll | Poll interval. |
| peer mode | Clock mode of a peer system:   * client: The peer clock cannot synchronize with a local clock, but the local clock can synchronize with the peer clock. * server: The peer clock can synchronize with a local clock, but the local clock cannot synchronize with the peer clock. * active: The peer clock can get synchronized to a local clock, and the local clock can get synchronized to the peer clock based on a larger stratum value. The synchronization request is first sent by the peer clock. * passive: The peer clock can get synchronized to a local clock, and the local clock can get synchronized to the peer clock based on a larger stratum value. The synchronization request is first sent by the local clock. * broadcast: The peer clock is in broadcast server mode. * client: The peer clock is in broadcast client mode. * unspecified: The field is unspecified. |
| peer poll | Peer poll. |
| peer interface | Name of a peer interface. |
| root delay | Total delay between the local system clock and master reference clock. The default value is 0. |
| root disper | Total dispersion between the local system clock and master reference clock. The default value is 0. |
| sync dist | Synchronized distance relative to reference clock source.  This parameter describes the clock source, and NTP selects the minimum synchronized distance to a clock source. |
| sync state | Synchronization status:   * 0: A clock is not set. * 1: A frequency is set. * 2: The time is set. * 3: A mode is frequency. * 4: A clock is synchronized. * 5: A spike is detected. |
| filter delay | Time when an NTP packet is received for the last time. |
| filter offset | Filter offset of the last eight packets received. |
| filter disper | Filter dispersion of the last eight packets received. |
| delay | Delay between the local system clock and peer for the last received packet. |
| now | Time since NTP packet is not received or last synchronized. |
| offset | Offset between the local system clock and peer for the last received packet. |
| disper | Dispersion between the local system clock and peer for the last received packet. |
| reach | Reachability of the configured server or peer. |
| precision | Peer clock precision. |
| version | NTP version. |
| reftime | Reference timestamp. |
| orgtime | Date and time of the last originated packet. |
| rcvtime | Date and time when the last packet was received. |
| xmttime | Date and time when the last packet was transmitted. |
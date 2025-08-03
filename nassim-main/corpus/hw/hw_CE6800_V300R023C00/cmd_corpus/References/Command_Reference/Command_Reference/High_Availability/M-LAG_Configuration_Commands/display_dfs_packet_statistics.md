display dfs packet statistics
=============================

display dfs packet statistics

Function
--------



The **display dfs packet statistics** command displays the number of received and sent packets about M-LAG status change.




Format
------

**display dfs packet statistics**


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

The **display dfs packet statistics** command displays the number of received and sent packets about M-LAG status change, which helps you locate faults and analyze problems.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of received and sent packets about M-LAG status change.
```
<HUAWEI> display dfs packet statistics
Last send success type    : --
Last send fail type       : --
Last send fail reason     : --
Last receive type         : --
Last send success time    : 0000-00-00 00:00:00
Last receive time         : 0000-00-00 00:00:00
Last send fail time       : 0000-00-00 00:00:00
---------------------------------------------------------------------
Type                Send success       Send fail         Receive
---------------------------------------------------------------------
HELLO                          0               0               0
DEVIINFO                       0               0               0
UNIPORTINFO                    0               0               0
IPV4_HEART                     0               0               0
IPV6_HEART                     0               0               0
MSTPINFO                       0               0               0
MSTPPORT                       0               0               0
PORT_REQ                       0               0               0
PORT_ASK                       0               0               0
ACK                            0               0               0
LACPSYSINFO                    0               0               0
LACPSYSINFOACK                 0               0               0
MSTPPROCINST                   0               0               0
SYNC_CONFIG                    0               0               0
MLAG_CONFIG                    0               0               0
MLAGIP                         0               0               0
MLAGIP_ACK                     0               0               0
ARP_SYNC                       0               0               0
ND_SYNC                        0               0               0
PORTGROUP_BTH                  0               0               0
PORTGROUP_REAL                 0               0               0
PORTGROUP_ACK                  0               0               0
SYNC                           0               0               0
SYNC_ACK                       0               0               0
---------------------------------------------------------------------

```

**Table 1** Description of the **display dfs packet statistics** command output
| Item | Description |
| --- | --- |
| Last send success type | Type of packets that are successfully sent last time. |
| Last send fail type | Type of packets that fail to be sent last time. |
| Last send fail reason | Cause for the failure to send packets last time. |
| Last receive type | Type of packets that are received last time. |
| Last send success time | Last time when packets are successfully sent. |
| Last send fail time | Last time when packets fail to be sent. |
| Last receive time | Last time when packets are received. |
| Type | Packet type. |
| Send success | Statistics on packets that are successfully sent. |
| Send fail | Statistics on packets that fail to be sent. |
| Receive | Statistics on packets that are received. |
display inof bfd session
========================

display inof bfd session

Function
--------



The **display inof bfd session** command displays information about BFD sessions in the iNOF system.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display inof bfd session**


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

You can run this command to view information about BFD sessions in the iNOF system.

**Precautions**

When two reflectors exist on an iNOF network, the BFD parameters configured for the two reflectors must be the same.If the BFD parameters configured on the two reflectors are different, the larger value takes effect.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BFD sessions in the iNOF system.
```
<HUAWEI> display inof bfd session
IPv4 Info:
Local Min Tx Interval (ms): 300    Actual Min Tx Interval (ms): 1000
Local Min Rx Interval (ms): 1000   Actual Min Rx Interval (ms): 1000
Local Detect Multi        : 3      Actual Detect Multi        : 3
---------------------------------------------------------------------
PeerIpAddress                                             State
---------------------------------------------------------------------
192.168.1.2                                               Up   
192.168.2.3                                               Down   
---------------------------------------------------------------------
IPv6 Info:
Local Min Tx Interval (ms): 300    Actual Min Tx Interval (ms): 1000
Local Min Rx Interval (ms): 1000   Actual Min Rx Interval (ms): 1000
Local Detect Multi        : 3      Actual Detect Multi        : 3
---------------------------------------------------------------------
PeerIpAddress                                             State
---------------------------------------------------------------------
2001:DB8:1::1                                             Up   
2001:DB8:1::2                                             Down   
---------------------------------------------------------------------

```

**Table 1** Description of the **display inof bfd session** command output
| Item | Description |
| --- | --- |
| IPv4 Info | IPv4 information. |
| Local Min Tx Interval (ms) | Configured minimum interval for sending BFD packets. |
| Local Min Rx Interval (ms) | Configured minimum interval at which BFD packets are received. |
| Local Detect Multi | Configured local detection multiplier of BFD packets. |
| Actual Min Tx Interval (ms) | Effective minimum interval for sending BFD packets. |
| Actual Min Rx Interval (ms) | Effective minimum interval for receiving BFD packets. |
| Actual Detect Multi | Active detection multiplier of the BFD session. |
| PeerIpAddress | Peer IP address tracked by BFD. |
| State | Current status of the BFD session:   * Up. * Down. * AdminDown. |
| IPv6 Info | IPv6 information. |
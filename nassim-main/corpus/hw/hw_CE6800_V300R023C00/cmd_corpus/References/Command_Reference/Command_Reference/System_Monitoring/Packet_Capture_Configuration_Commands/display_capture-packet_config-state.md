display capture-packet config-state
===================================

display capture-packet config-state

Function
--------



The **display capture-packet config-state** command displays the configuration of the packet capture function.




Format
------

**display capture-packet config-state**


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

After the device is configured to obtain the packets to be sent to the CPU or forwarded or discarded, you can run this command to view packet obtaining status, parameters, and name of the file for storing obtained packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the packet capture function.
```
<HUAWEI> display capture-packet config-state
Capture-Packet Index 1
Type        : local-host
Interface   : 100GE1/0/1
ACL         : 2001
File Name   : flash:/logfile/capture_host_all_100GE.cap
Time-out    : 3600 seconds
Remain-time : 60 seconds
Packet-num  : 1000
Remain-num  : 100
Packet-len  : 64

```

**Table 1** Description of the **display capture-packet config-state** command output
| Item | Description |
| --- | --- |
| Capture-Packet Index | Index of an instance for obtaining packets. |
| Type | Type of obtained packets. |
| Interface | Name of an interface. |
| ACL | IPv4 ACL number or name. |
| File Name | Name of a file saving an instance. |
| Time-out | Timeout time before the system stops obtaining packets. |
| Remain-time | Remaining packet obtaining time. |
| Packet-num | Number of obtained packets in a file. |
| Remain-num | Number of remaining packets to be obtained. |
| Packet-len | Length of each packet in a file. |
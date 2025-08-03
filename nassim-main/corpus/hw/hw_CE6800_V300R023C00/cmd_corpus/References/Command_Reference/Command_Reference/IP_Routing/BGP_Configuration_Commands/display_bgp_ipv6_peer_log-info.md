display bgp ipv6 peer log-info
==============================

display bgp ipv6 peer log-info

Function
--------



The **display bgp ipv6 peer log-info** command displays log information about BGP IPv6 peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 peer** *ipv6-address* **log-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer to be displayed. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp ipv6 peer log-info** command can be used for troubleshooting, with details as follows: If BGP peers are disconnected, check the log information of the specified peer. In the command output, Date/Time indicates the time when the peers were disconnected, and Error Code and Error Subcode indicate the cause of the disconnection.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display log information about the BGP peer 2001:DB8:1::2.
```
<HUAWEI> display bgp ipv6 peer 2001:DB8:1::2 log-info
Peer : 2001:DB8:1::2 
 Date/Time     : 2019/16/09 11:53:25
 State         : Down
 Error Code    : 5(Finite State Machine Error)
 Error Subcode : 2(Receive Unexpected Message in OpenConfirm State)
 Error Data    : 2(UPDATE message)
 Notification  : Receive Notification

 Date/Time     : 2019/16/09 11:53:21
 State         : Up
 Date/Time     : 2019/16/09 11:53:09
 State         : Down
 Error Code    : 6(CEASE)
 Error Subcode : 4(Administrative Reset)
 Notification  : Receive Notification
 Date/Time     : 2019/16/09 10:34:05
 State         : Up

```

**Table 1** Description of the **display bgp ipv6 peer log-info** command output
| Item | Description |
| --- | --- |
| Peer | Peer IP address. |
| Date/Time | Date/time. |
| State | Status of a HWTACACS server. |
| Error Code | Error code.  For the meanings and possible causes of error codes, see BGP Principles - BGP NOTIFICATION Packets. These packets are used to process various errors in the BGP process. |
| Error Subcode | Error subcode.  For details about error subcodes and possible causes, see BGP Fundamentals - BGP Notification Messages. These messages are used to process various errors in the BGP process. |
| Error Data | Error data. |
| Notification | Notification message sent or received by a peer. |
display bgp peer log-info
=========================

display bgp peer log-info

Function
--------



The **display bgp peer log-info** command displays log information about BGP peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp** [ **instance** *instance-name* ] **peer** { *ipv4-address* | *group-name* } **log-info**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **peer** *ipv4-address* **log-info**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **peer** *ipv4-address* **log-info**

**display bgp all peer log-info**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **peer-group** *group-name* **log-info**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **peer-group** *group-name* **log-info**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp** [ **instance** *instance-name* ] **peer** *ipv6-address* **log-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **log-info** | Displays log information of the specified peer. | - |
| **peer** *ipv4-address* | Specifies an IPv4 peer address to be displayed. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **vpnv4** | Displays information about peers in a VPNv4 instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **all** | Displays information about all peers. | - |
| **peer-group** | Specifies a peer group. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp peer log-info** command can be used for troubleshooting, with details as follows: If BGP peers are disconnected, specify log-info in the command to check the log information of the specified peer. In the command output, Date/Time indicates the time when the peers were disconnected, and Error Code and Error Subcode indicate the cause of the disconnection.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display log information on BGP peer 10.1.1.2.
```
<HUAWEI> display bgp peer 10.1.1.2 log-info
Peer : 10.1.1.2 
 Date/Time     : 2011/23/06 11:53:24
 State         : Down
 Error Code    : 5(Finite State Machine Error)
 Error Subcode : 2(Receive Unexpected Message in OpenConfirm State)
 Error Data    : 2(UPDATE message)
 Notification  : Receive Notification

 Date/Time     : 2011/13/06 11:53:21
 State         : Up
 Date/Time     : 2011/13/06 11:53:09
 State         : Down
 Error Code    : 6(CEASE)
 Error Subcode : 4(Administrative Reset)
 Notification  : Receive Notification
 Date/Time     : 2011/13/06 10:34:05
 State         : Up

```

**Table 1** Description of the **display bgp peer log-info** command output
| Item | Description |
| --- | --- |
| Peer | Peer IP address. |
| Date/Time | Date/time. |
| State | Thread status. |
| Error Code | Error code.  For the meanings and possible causes of error codes, see BGP Principles - BGP NOTIFICATION Packets. These packets are used to process various errors in the BGP process. |
| Error Subcode | Error subcode.  For details about error subcodes and possible causes, see BGP Fundamentals - BGP Notification Messages. These messages are used to process various errors in the BGP process. |
| Error Data | Error data. |
| Notification | Notification message sent or received by a peer. |
display bgp vpnv6 peer log-info
===============================

display bgp vpnv6 peer log-info

Function
--------



The **display bgp vpnv6 peer log-info** command displays the log information of the BGP VPNv6 address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **peer** *ipv6-address* **log-info**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **peer-group** *group-name* **log-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **peer-group** *group-name* | Specifies a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 peer log-info** command displays the log information of the BGP VPNv6 address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the log information of the BGP VPNv6 address family.
```
<HUAWEI> display bgp vpnv6 vpn-instance vpn1 peer 2001:DB8:1::2 log-info
            
Peer : 2001:DB8:1::2 
 Date/Time     : 2019-09-17 06:43:26+00:00
 State         : Down
 Error Code    : 5(Finite State Machine Error)
 Error Subcode : 2(Receive Unexpected Message in OpenConfirm State)
 Error Data    : 2(UPDATE message)
 Notification  : Receive Notification

 Date/Time     : 2019-09-17 06:43:16+00:00
 State         : Up

 Date/Time     : 2019-09-17 06:42:33+00:00
 State         : Down
 Error Code    : 6(CEASE)
 Error Subcode : 6(Other Configuration Change)
 Notification  : Receive Notification

 Date/Time     : 2019-09-17 06:42:29+00:00
 State         : Up

 Date/Time     : 2019-09-17 06:42:19+00:00
 State         : Down
 Error Code    : 6(CEASE)
 Error Subcode : 6(Other Configuration Change)
 Notification  : Send Notification

 Date/Time     : 2019-09-17 05:00:02+00:00
 State         : Up
                
 Date/Time     : 2019-09-17 04:59:52+00:00
 State         : Down
 Error Code    : 6(CEASE)
 Error Subcode : 6(Other Configuration Change)
 Notification  : Receive Notification

 Date/Time     : 2019-09-17 04:58:31+00:00
 State         : Up

```

**Table 1** Description of the **display bgp vpnv6 peer log-info** command output
| Item | Description |
| --- | --- |
| Peer | Peer. |
| Date/Time | Date/time. |
| State | State. |
| Error Code | Error code. |
| Error Subcode | Error sub-code. |
| Error Data | Error data. |
| Notification | Notification message sent or received by a peer. |
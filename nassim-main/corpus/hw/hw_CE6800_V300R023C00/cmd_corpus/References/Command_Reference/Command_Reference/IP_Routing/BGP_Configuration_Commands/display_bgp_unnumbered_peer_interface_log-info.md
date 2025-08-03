display bgp unnumbered peer interface log-info
==============================================

display bgp unnumbered peer interface log-info

Function
--------



The **display bgp unnumbered peer interface log-info** command displays log information about unnumbered BGP peers.




Format
------

**display bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **log-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies the type of an interface. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



The **display bgp unnumbered peer interface log-info** command displays log information about unnumbered BGP peers.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display log information about the peer on 100GE1/0/1.
```
<HUAWEI> display bgp unnumbered peer interface 100GE1/0/1 log-info
Unnumbered peer
Peer : FE80::3A01:FF:FE21:301(100GE1/0/1)
 Date/Time     : 2021-07-01 07:17:20+00:00
 State         : Down
 Error Code    : 5(Finite State Machine Error)
 Error Subcode : 2(Receive Unexpected Message in OpenConfirm State)
 Error Data    : 2(UPDATE message)
 Notification  : Receive Notification

 Date/Time     : 2021-07-01 07:16:20+00:00
 State         : Up

 Date/Time     : 2021-07-01 07:16:10+00:00
 State         : Down
 Error Code    : 4(Hold Timer Expired)
 Error Subcode : 0(UnSpecific)
 Notification  : Receive Notification

 Date/Time     : 2021-07-01 07:04:45+00:00
 State         : Up

```

**Table 1** Description of the **display bgp unnumbered peer interface log-info** command output
| Item | Description |
| --- | --- |
| Peer | Peer IP address. |
| Date/Time | Date/Time. |
| State | Status. |
| Error Code | Error code.  For the meanings and possible causes of error codes, see BGP Principles - BGP NOTIFICATION Packets. These packets are used to process various errors in the BGP process. |
| Error Subcode | Error subcode.  For details about error subcodes and possible causes, see BGP Principles - BGP NOTIFICATION Packets. These packets are used to process various errors in the BGP process. |
| Error Data | Error data. |
| Notification | The peer sends or receives a Notification packet. |
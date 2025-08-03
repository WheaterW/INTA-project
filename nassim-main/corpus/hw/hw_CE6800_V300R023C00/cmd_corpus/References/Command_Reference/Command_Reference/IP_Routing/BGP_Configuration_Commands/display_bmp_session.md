display bmp session
===================

display bmp session

Function
--------



The **display bmp session** command displays configurations about a BGP Monitoring Protocol (BMP) session.




Format
------

**display bmp session** [ **vpn-instance** *vpn-instacne-name* ]

**display bmp session** [ **vpn-instance** *vpn-instacne-name* ] { *ipv4-address* | *ipv6-address* } **verbose**

**display bmp session** [ **vpn-instance** *vpn-instacne-name* ] { *ipv4-address* | *ipv6-address* } **alias** *alias-name* **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instacne-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv4-address* | Specifies the IPv4 address used for the RPKI session. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a BMP session. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **verbose** | Displays detailed session information. | - |
| **alias** *alias-name* | Specifies a session alias. When the device needs to establish multiple TCP connections with the same monitoring server through different port numbers, specify session aliases for differentiation. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check configurations about a BMP session, run the **display bmp session** command. The command output helps you locate a fault (if any) and determine whether the BMP session is properly configured.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the BMP session with the session address 10.3.3.3 and alias aa.
```
<HUAWEI> display bmp session 10.3.3.3 alias aa verbose
BMP session 10.3.3.3, port 30000
    Current state: Up, Age: 12h18m32s
    VPN-instance name: _public_
    Local address: 10.98.178.12, Local port: 50423
    Statistics timeout: 3600(s)
    ConnectRetry Timer Remainder: 0(s)
    Statistics-report Timer Remainder: 2490(s)
    Send Route Monitoring messages: 9
    Send Statistics Report messages: 53
    Send Peer Down Notification messages: 3
    Send Peer Up Notification messages: 4
    Send Initiation messages: 1
    Send Termination messages: 0
    Send Trace Route messages: 121
  BGP ipv4-family unicast :
  0.0.0.0   (local-rib(all/path-marking))
  10.1.1.1 (in pre-policy)     
  10.2.2.2 (in pre-policy)
  BGP ipv4-family vpnv4 :
  10.2.2.2 (in pre-policy)

```

# Display the configuration of the BMP session with the session address 10.1.1.1.
```
<HUAWEI> display bmp session
Total number of BMP session : 2
 Session in up state : 0
  Session          Alias      State      Age            VPN                                
  10.1.1.1                     Down       57s            _public_                           
  10.1.1.1          a          Down       44s            _public_

```

# Display detailed information about the BMP session with the session address 10.1.1.1.
```
<HUAWEI> display bmp session 10.1.1.1 verbose
BMP session 10.10.10.10, port 0
    Current state: Down (Reason: Manual Stop), Age: 04h39m54s
    VPN-instance name: _public_
    Local address: 0.0.0.0, Local port: 0
    Statistics timeout: 3600(s)
    ConnectRetry Timer Remainder: 15(s)
    Statistics-report Timer Remainder: 2538(s)
    Send Route Monitoring messages: 9
    Send Statistics Report messages: 53
    Send Peer Down Notification messages: 3
    Send Peer Up Notification messages: 4
    Send Initiation messages: 1
    Send Termination messages: 0
    Send Trace Route messages: 121
  BGP ipv4-family unicast :
  0.0.0.0   (local-rib(all/path-marking))
  10.1.1.1 (in pre-policy)     
  10.2.2.2 (in pre-policy)
  BGP ipv4-family vpnv4 :
  10.2.2.2 (in pre-policy)

```

**Table 1** Description of the **display bmp session** command output
| Item | Description |
| --- | --- |
| BMP session | IP address of the server with which a BMP session is established. |
| port | Server port number. |
| Current state | Status of the BMP session:   * Down. * Up. |
| VPN-instance name | VPN instance to which the BMP session belongs. |
| Local address | Local IP address. |
| Local port | Local port number. |
| Statistics timeout | Interval at which the router sends BGP running statistics to the monitoring server. |
| ConnectRetry Timer Remainder | Period after which a connection is re-established. |
| Statistics-report Timer Remainder | Period after which the router sends BGP running statistics to a monitoring server. |
| Send Route Monitoring messages | Number of Route Monitoring messages sent by a BMP session. |
| Send Statistics Report messages | Number of statistics messages sent by a BMP session. |
| Send Peer Down Notification messages | Number of Peer Down messages sent by a BMP session. |
| Send Peer Up Notification messages | Number of Peer Up messages sent over a BMP session. |
| Send Initiation messages | Number of Initiation messages sent over a BMP session. |
| Send Termination messages | Number of Termination messages sent by a BMP session. |
| Send Trace Route messages | Number of Trace Route messages sent by a BMP session. |
| BGP ipv4-family unicast | Type of route whose statistics are sent by the device to the monitoring server in the IPv4 unicast address family.   * in pre-policy: all received RIB-in routes. * in post-policy: RIB-in routes accepted by an import policy. * out pre-policy: all RIB-out routes, regardless of whether they match an export policy. * out post-policy: RIB-out routes that match an export policy. * local-rib: Local-RIB routes. * local-rib(a): Local-RIB Add-Path routes. |
| BGP ipv4-family vpnv4 | Type of route whose statistics are sent by the device to the monitoring server in the BGP-VPNv4 address family.   * in pre-policy: all received RIB-in routes. * in post-policy: RIB-in routes accepted by an import policy. * out pre-policy: all RIB-out routes, regardless of whether they match an export policy. * out post-policy: RIB-out routes that match an export policy. * local-rib: Local-RIB routes. * local-rib(a): Local-RIB Add-Path routes. |
| Total number of BMP session | Total number of BMP session. |
| Session in up state | BMP sessions that are Up. |
| Session | IP address of the server with which a BMP session is established. |
| Alias | Alias of a BMP session. If no alias is specified, the field is empty. |
| State | Status of the BMP session:   * Down. * Up. |
| Age | Duration of the BMP session in the Up or Down state. |
| VPN | VPN instance to which the BMP session belongs. |
display tcp statistics
======================

display tcp statistics

Function
--------



The **display tcp statistics** command displays TCP packet statistics.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display tcp statistics**

**display tcp statistics verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display tcp ipv6 statistics**

**display tcp ipv6 statistics verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Indicates detailed information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check statistics about TCP packets, including the number of sent and received TCP packets, run the display tcp statistics command.You can judge the network connection status according to the following items in the command output:

* Established connections: You can view information about Established connections to check whether the number of connections exceeds the upper limit. If the number of connections exceeds the upper limit, you can determine whether to deploy services such as BGP services or adjust the load.
* You can view Duplicate ACK packets to check whether the system is attacked by ACK packets. If the device receives a large number of unknown ACK packets, the device may be attacked.
* Out-of-order packets: This field helps you determine the network quality. If the network is in poor condition, a lot of out-of-order packets are generated.If you want to diagnose problems and monitor information of specific applications, configure verbose in the display tcp statistics command so that application-specific TCP traffic statistics are displayed. The applications can be BGP, FTP, TELNET, SSH, PCEP and others.

**Precautions**

The number of packets received by a routing device includes the number of forwarded packets, packets sent to the upper layer, and discarded packets.The statistics on applications are collected based on well-known port numbers. The BGP port number is 179, the FTP port number is 20 or 21, the Telnet port number is 23, the SSH port number is 22, and the PCEP port number is 4189. The statistics on applications with other port numbers are recorded in the Others field.Before collecting the IPv4 TCP packet statistics during a specific period, you are recommended to run the **reset tcp statistics** command to clear the previous IPv4 TCP packet statistics.Before collecting the IPv6 TCP packet statistics during a specific period, you are recommended to run the **reset tcp ipv6 statistics** command to clear the previous IPv6 TCP packet statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display TCP packet statistics.
```
<HUAWEI> display tcp statistics
Received packets:
    Total packets                    : 11316
    SYN packets                      : 2386
    FIN packets                      : 0
    Packets bytes in sequence        : 303
    Window probe packets             : 0
    Window update packets            : 0
    Checksum error                   : 0
    Offset error                     : 0
    Short error                      : 0
    Duplicate packets bytes          : 10951
    Partially duplicate packets bytes: 0
    Out-of-order packets bytes       : 0
    Packets with data after window   : 0
    Packets after close              : 0
    ACK packets bytes                : 217
    Duplicate ACK packets            : 0
Sent packets:
    Total packets             : 317
    Urgent packets            : 0
    Control packets RST       : 0
    Window probe packets      : 0
    Window update packets     : 0
    Data packets              : 0
    Data packets retransmitted: 0
    ACK only packets          : 4


Retransmitted timeout                                 : 0
Connection dropped in retransmitted timeout           : 0
Keepalive timeout                                     : 10926
Keepalive probe                                       : 10926
Keepalive timeout, so connections disconnected        : 0
Initiated connections                                 : 0
Accepted connections                                  : 2
Established connections                               : 4
Closed connections                                    : 1
Packets dropped with MD5 authentication               : 0
Packets permitted with MD5 authentication             : 0
Send Packets permitted with Keychain authentication   : 0
Receive Packets permitted with Keychain authentication: 0
Receive Packets Dropped with Keychain authentication  : 0

```

# Display IPv4 TCP packet statistics by application.
```
<HUAWEI> display tcp statistics verbose
Received packets:
--------------------------------------------------------------------------------
Application   Checksum Errors   Format Errors   No Port   Auth Errors
                                                          (MD5/Keychain)
--------------------------------------------------------------------------------
BGP           0                 0               0         0/0
FTP           0                 0               0         0/0
LDP           0                 0               0         0/0
MSDP          0                 0               0         0/0
TELNET        0                 0               0         0/0
SSH           0                 0               0         0/0
PCEP          0                 0               0         0/0
Others        0                 0               0         0/0
--------------------------------------------------------------------------------
 
Sent packets:
--------------------------------------------------------------------------------
Application   Dropped packets 
--------------------------------------------------------------------------------
BGP           0  
FTP           0 
LDP           0       
MSDP          0 
TELNET        0
SSH           0 
PCEP          0 
Others        0
--------------------------------------------------------------------------------

```

# View the statistics about the transmitted and received IPv6 TCP packets.
```
<HUAWEI> display tcp ipv6 statistics
Received packets:
    Total packets                    : 0
    SYN packets                      : 0
    FIN packets                      : 0
    Packets bytes in sequence        : 0
    Window probe packets             : 0
    Window update packets            : 0
    Checksum error                   : 0
    Offset error                     : 0
    Short error                      : 0
    Duplicate packets bytes          : 0
    Partially duplicate packets bytes: 0
    Out-of-order packets bytes       : 0
    Packets with data after window   : 0
    Packets after close              : 0
    ACK packets bytes                : 0
    Duplicate ACK packets            : 0
Sent packets:
    Total packets             : 0
    Urgent packets            : 0
    Control packets RST       : 0
    Window probe packets      : 0
    Window update packets     : 0
    Data packets              : 0
    Data packets retransmitted: 0
    ACK only packets          : 0

Retransmitted timeout                                 : 0
Connection dropped in retransmitted timeout           : 0
Keepalive timeout                                     : 0
Keepalive probe                                       : 0
Keepalive timeout, so connections disconnected        : 0
Initiated connections                                 : 0
Accepted connections                                  : 0
Established connections                               : 0
Closed connections                                    : 0
Packets dropped with MD5 authentication               : 0
Packets permitted with MD5 authentication             : 0
Send Packets permitted with Keychain authentication   : 0
Receive Packets permitted with Keychain authentication: 0
Receive Packets Dropped with Keychain authentication  : 0

```

# Display IPv6 TCP packet statistics by application.
```
<HUAWEI> display tcp ipv6 statistics verbose
Received packets:
--------------------------------------------------------------------------------
Application   Checksum Errors   Format Errors   No Port   Auth Errors
                                                          (MD5/Keychain)     
--------------------------------------------------------------------------------
BGP           0                 0               0         0/0
FTP           0                 0               0         0/0
LDP           0                 0               0         0/0
TELNET        0                 0               0         0/0
SSH           0                 0               0         0/0
PCEP          0                 0               0         0/0
Others        0                 0               0         0/0
--------------------------------------------------------------------------------
 
Sent packets:
--------------------------------------------------------------------------------
Application   Dropped packets 
--------------------------------------------------------------------------------
BGP           0
FTP           0
LDP           0
TELNET        0
SSH           0
PCEP          0
Others        0
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display tcp statistics** command output
| Item | Description |
| --- | --- |
| Received packets | Number of received packets. |
| Total | Total number of received or sent packets. |
| Total packets | Total number of received or sent packets. |
| SYN packets | Number of received SYN packets. |
| FIN packets | Number of received FIN packets. |
| Packets with data after window | Number of packets outside the receiving window. |
| Packets dropped with MD5 authentication | Number of dropped packets after MD5 authentication. |
| Packets permitted with MD5 authentication | Number of passed packets after MD5 authentication. |
| Packets bytes in sequence | Number of packets that arrive in sequence (total bytes). |
| Packets after close | Number of packets that arrive after the connection is closed. |
| Window probe packets | Number of window probe packets. |
| Window update packets | Number of window update packets. |
| Checksum error | Number of packets with checksum errors. |
| Checksum Errors | Number of discarded packets with checksum errors. |
| Offset error | Number of packets in incorrect length. |
| Short error | Number of packets whose length is too short. |
| Duplicate ACK packets | Number of re-acknowledged packets. |
| Duplicate packets bytes | Number of completely repeated packets (total bytes). |
| Partially duplicate packets bytes | Number of partly repeated packets (total bytes). |
| Out-of-order packets bytes | Number of packets in incorrect sequence (total bytes). |
| ACK packets | Number of acknowledged packets (total bytes). |
| ACK only packets | Number of ACK packets. |
| ACK packets bytes | Number of acknowledged packets (total bytes). |
| Sent packets | Sent packet statistics. |
| Urgent packets | Number of urgent data packets. |
| Control packets | Number of control packets (number of RST packets). |
| Control packets RST | Number of control packets (number of RST packets). |
| Data packets | Number of data packets. |
| Data packets retransmitted | Number of retransmitted packets (total bytes). |
| Retransmitted timeout | Number of timeouts of the retransmission timer. |
| Connection dropped in retransmitted timeout | Number of dropped connections because their retransmission number exceeds the limit. |
| Keepalive timeout | Timeout period of the Keepalive timer. |
| Keepalive probe | Number of sent Keepalive packets. |
| Keepalive timeout, so connections disconnected | Number of discarded connections because the Keepalive probe fails. |
| Initiated connections | Number of times connections are initiated. |
| Accepted connections | Number of received connections. |
| Established connections | Number of established connections. |
| Closed connections | Number of closed connections. |
| Send Packets permitted with Keychain authentication | Number of sent packets carrying the Keychain information. |
| Receive Packets permitted with Keychain authentication | Number of received packets carrying the Keychain information. |
| Receive Packets Dropped with Keychain authentication | Number of dropped packets carrying the Keychain information. |
| Dropped packets | Number of sent packets that are discarded. |
| Application | TCP application protocol type. |
| Format Errors | Number of packets with incorrect formats. |
| No Port | Number of packets for which no socket can be found. |
| Auth Errors | Number of packets with authentication errors. |
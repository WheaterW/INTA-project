display tcp ipv6 status
=======================

display tcp ipv6 status

Function
--------



The **display tcp ipv6 status** command displays all IPv6 TCP connections.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display tcp ipv6 status** [ **local-ip** *local-ip* | **local-port** *local-port* | **remote-ip** *remote-ip* | **remote-port** *remote-port* ] \* [ **cid** *cid* ] [ **socket-id** *socket-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local-ip** *local-ip* | Displays the IPv6 TCP connection with a specified local IP address. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **local-port** *local-port* | Displays the IPv6 TCP connection with a specified local port number. | The value ranges from 0 to 65535. |
| **remote-ip** *remote-ip* | Displays the IPv6 TCP connection with a specified remote IP address. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **remote-port** *remote-port* | Displays the IPv6 TCP connection with a specified remote port number. | The value ranges from 0 to 65535. |
| **cid** *cid* | Displays the IPv6 TCP connection with a specified APP CID. | The value is a hexadecimal integer that ranges from 0 to ffffffff. |
| **socket-id** *socket-id* | Displays the IPv6 TCP connection with a specified socket ID. | The value is an integer that ranges from 0 to 2147418111. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

TCP defined in standard protocols ensures high-reliability transmission between hosts. TCP provides reliable, connection-oriented, and full-duplex services for user processes. To monitor the TCP connection status, run the display tcp status command to check the following information:

* IPv6 TCP socket ID
* APP CID
* Local IPv6 address and port number
* Remote IPv6 address and port number
* VPNID
* IPv6 TCP connection statusA filtering rule, such as a socket ID, local IP address, local port number, remote IP address, or remote port number, can be specified so that only the information matching the rule is displayed. This reduces the amount of output information, improving output information usability and fault locating accuracy and efficiency.

**Precautions**

If no TCP connection is available, the command output is empty.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of IPv6 TCP connections.
```
<HUAWEI> display tcp ipv6 status
-------------------------------------------------------------------------------------------------------
Cid/SocketID         Local Address                Foreign Address              VPNID      State        
-------------------------------------------------------------------------------------------------------
0x8093041E/3         ::->830                      ::->0                        4294967295 LISTEN       
0x8093041E/5         ::->22                       ::->0                        4294967295 LISTEN       
-------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display tcp ipv6 status** command output
| Item | Description |
| --- | --- |
| Cid/SocketID | Socket ID. |
| Local Address | Local IPv6 address. |
| Foreign Address | Peer IPv6 address. |
| VPNID | VPN instance ID. |
| State | Status of an IPv6 TCP connection:   * Established: indicates that the connection has been established. * LISTEN: indicates that the connection is being listened to. |
display tcp status
==================

display tcp status

Function
--------



The **display tcp status** command displays information about IPv4 TCP connections.




Format
------

**display tcp status** [ **local-ip** *local-ipv4-address* | **local-port** *local-port-number* | **remote-ip** *remote-ipv4-address* | **remote-port** *remote-port-number* ] \* [ **cid** *cid* ] [ **socket-id** *socket-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local-ip** *local-ipv4-address* | Displays the IPv4 TCP connection with a specified local IP address. | The address is a 4-digit number, in the format of X.X.X.X. |
| **local-port** *local-port-number* | Displays the IPv4 TCP connection with a specified local port number. | The value ranges from 0 to 65535. |
| **remote-ip** *remote-ipv4-address* | Displays the IPv4 TCP connection with a specified remote IP address. | The address is a 4-digit number, in the format of X.X.X.X. |
| **remote-port** *remote-port-number* | Displays the IPv4 TCP connection with a specified remote port number. | The value ranges from 0 to 65535. |
| **cid** *cid* | Displays the IPv4 TCP connection with a specified APP CID. | The value is a hexadecimal integer that ranges from 0 to ffffffff. |
| **socket-id** *socket-id* | Displays the IPv4 TCP connection with a specified socket ID. | The value is an integer that ranges from 0 to 2147418111. |



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

* IPv4 TCP socket ID
* APP CID
* Local IPv4 address and port number
* Remote IPv4 address and port number
* VPN Name
* IPv4 TCP connection statusA filtering rule, such as a socket ID, local IP address, local port number, remote IP address, or remote port number, can be specified so that only the information matching the rule is displayed. This reduces the amount of output information, improving output information usability and fault locating accuracy and efficiency.

**Precautions**



If no TCP connection is available, the command output is empty.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of IPv4 TCP connections.
```
<HUAWEI> display tcp status
* - MD5 Authentication is enabled.
# - Keychain Authentication is enabled.
--------------------------------------------------------------------------------
Cid         SocketID    Local Addr:Port    Foreign Addr:Port    State    VPNID  
--------------------------------------------------------------------------------
0x80C8272A  8           0.0.0.0:23         0.0.0.0:0            LISTEN   --     
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display tcp status**  command output
| Item | Description |
| --- | --- |
| Cid | Component ID. |
| SocketID | Socket ID. |
| Local Addr:Port | Local IP address and port number of a TCP connection.  If the value of Local Add is 0.0.0.0, all addresses are monitored. If the value of port number is 0, all port number are monitored. |
| Foreign Addr:Port | Remote IP address and port number of a TCP connection.  If the value of Foreign Add is 0.0.0.0, all addresses are monitored. If the value of port number is 0, all port number are monitored. |
| State | TCP connection status:   * Closed: A TCP connection has not been started or has been torn down. * Listening: A TCP connection is being listened to. * Syn\_Rcvd: A packet with the SYN flag is received. * Established: A TCP connection has been established. * Close\_Wait: In the Established state, a user sends a FIN packet to the server, requesting connection termination. After receiving the FIN packet, the server sends an ACK packet to the user and enters the Close\_Wait state. * Fin\_Wait1: A user enters this state after sending a FIN packet to the server to request the server to tear down the connection. * Fin\_Wait2: A user enters this state after receiving an ACK packet from the server. * Time\_Wait: TCP enters this state after a TCP connection is torn down. When TCP remains in this state for twice the length of the longest packet's lifetime, information about the TCP connection will be cleared. * Closing: Both ends are closing the TCP connection. |
| VPNID | Local VPN ID. |
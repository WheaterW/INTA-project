display ip socket
=================

display ip socket

Function
--------



The **display ip socket** command displays information about created IPv4 sockets. If no parameter is specified, the command displays information about all types of sockets.

The **display ipv6 socket** command displays information about created IPv6 sockets.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display ip socket** [ **socket-type** *socket-type* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display ipv6 socket** [ **socket-type** *socket-type* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **socket-type** *socket-type* | Displays information about sockets of a specified type. | The value is an integer ranging from 1 to 4:   1. Socket for TCP streams 2. Socket for UDP packets 3. Socket for RawIP 4. Socket for RawLink |
| **cid** *cid* | Displays socket information of the APP with a specified CID. | The value is in hexadecimal notation and ranges from 0x0-0xffffffff. The default value is 0x0. |
| **socket-id** *socket-id* | Displays information about the socket with a specified ID. | The value is an integer ranging from 0 to 2147418111. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check socket information, run the display ip socket command. A filtering rule, such as a PID, socket ID, or socket type, can be specified so that only the information matching the rule is displayed. This reduces the amount of output information, improving output information usability and fault locating accuracy and efficiency.The command can be used to display information about a specific type or all types of sockets.

**Precautions**

No information will be displayed if there is no information about sockets.If no parameter is specified, information about all types of sockets is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IP sockets.
```
<HUAWEI> display ip socket

Total: 2


Cid = 0x80262711, socketid = 0, Proto = 17,
LA=0.0.0.0:123, FA=0.0.0.0:0,
sndbuf = 0, rcvbuf = 0, sb_cc = 0, rb_cc = 0,
socket option = SO_REUSEADDR ,
socket state = SS_NBIO SS_ASYNC
 
Cid = 0x8035272E, socketid = 0, Proto = 17,
LA=0.0.0.0:1024, FA=0.0.0.0:0,
sndbuf = 0, rcvbuf = 0, sb_cc = 0, rb_cc = 0,
socket option = SO_REUSEADDR ,
socket state = SS_NBIO SS_ASYNC

```

# Display information about IPv6 sockets.
```
<HUAWEI> display ipv6 socket
Total: 2



Cid = 0x8035272E, socketid = 1, Proto = 17,
LA=:::1024, FA=:::0,
sndbuf = 0, rcvbuf = 0, sb_cc = 0, rb_cc = 0,
socket option = SO_REUSEADDR ,
socket state = SS_NBIO SS_ASYNC

Cid = 0x80C8272D, socketid = 3, Proto = 6,
LA = ::->23, FA = ::->0,
sndbuf = 0, rcvbuf = 0, sb_cc = 0, rb_cc = 0,
socket option = SO_REUSEADDR SO_ACCEPTCONN SO_REUSEADDR ,
socket state = SS_NBIO SS_ASYNC SS_NBIO SS_ASYNC

```

**Table 1** Description of the **display ip socket** command output
| Item | Description |
| --- | --- |
| socket option | Socket options that have been set:   * SO\_DEBUG: debugging option. * SO\_ACCEPTON: an option set on the server, responsible for monitoring. * SO\_REUSEADDR: address overlapping, which allows multiple identical addresses to be bound to the local port. * SO\_KEEPALIVE: keepalive option of TCP connections. After the option is set, the keepalive timer is started after a TCP connection is established. * SO\_DONTROUTE: The socket must choose the direct route to the destination when setting up a connection. * SO\_BROADCAST: The device can send broadcast packets through the interface. * SO\_REUSEPORT: port overlapping, which allows multiple identical ports to be bound to the local port. This optional is mostly set on servers. * SO\_UDPCHECKSUM: The socket calculates the checksum of UDP packets. * SO\_SENDVPNID: an option for VPN. * SO\_USELOOPBACK: The socket can use the loopback interface to send and receive data. * SO\_LINGER: A TCP connection is closed depending on the set time. If the time is not set to 0, the TCP connection is closed after the timer expires. If the time is set to 0, the TCP connection is closed immediately. * SO\_OOBINLINE: out-of-band data. After a socket receives data, it processes the out-of-band data first. * SO\_SENDDATAIF: A socket uses the specified interface to send and receive data. * SO\_SENDDATAIF\_DONTSETTTL: A socket uses the specified interface to send and receive data but does not set the time to live (TTL) value. * SO\_SETSRCADDR: A socket sets the source address for sending packets. * SO\_SENDBY\_IF\_NEXTHOP: A socket sets the outbound interface and next hop of packets. |
| socket state | Socket status:   * SS\_NOFDREF: A socketid has been deleted. * SS\_ISCONNECTED: A TCP connection has been established. * SS\_ISCONNECTING: A TCP connection is being established. * SS\_ISDISCONNECTING: A TCP connection is being closed. * SS\_CANTSENDMORE: A socket cannot send data. * SS\_CANTRCVMORE: A socket cannot receive data. * SS\_RCVMARK: A socket sets the receive option in received packets. * SS\_NBIO: The socket type is non-blocked. * SS\_ISCONFIRMING: The connection is to be processed by the upper layer. * SS\_BLOCKING: Sent and received packets are blocked. * SS\_RECALL: The message notification method is set by an asynchronous socket. * SS\_PRIV: The option is transferred from the Unix and is inapplicable in the current socket. * SS\_ASYNC: state identifier of an asynchronous socket. |
| Cid | Indicates the CID of the APP component. |
| socketid | Indicates the socket ID. |
| Proto | Indicates the protocol number. |
| sndbuf | Indicates the upper limit of the cache of packet sending. |
| rcvbuf | Indicates the upper limit of the cache of packet receiving. |
| sb\_cc | Number of sent packets, valid only when TCP caches data. |
| rb\_cc | Number of received packets. |
| LA | Local address. |
| FA | Foreign address, which means a remote address. |
| Total | Indicates the total number of socket instances. |
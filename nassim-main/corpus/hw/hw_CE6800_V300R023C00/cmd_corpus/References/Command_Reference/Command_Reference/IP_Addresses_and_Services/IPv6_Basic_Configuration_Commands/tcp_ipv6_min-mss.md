tcp ipv6 min-mss
================

tcp ipv6 min-mss

Function
--------



The **tcp ipv6 min-mss** command sets the minimum value of maximum segment size (MSS) for a TCP6 connection.

The **undo tcp ipv6 min-mss** command restores the default minimum MSS value for a TCP6 connection.



By default, the minimum MSS value for TCP6 connections is 216 bytes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tcp ipv6 min-mss** *min-mss-val*

**undo tcp ipv6 min-mss** [ *min-mss-val* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *min-mss-val* | Specifies the minimum MSS value for a TCP6 connection. | The value is an integer ranging from 32 to 9600, in bytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To establish a TCP6 connection, the MSS value is negotiated, which indicates the maximum length of packets that the local device can receive. The TCP6 client on a network may send a request packet for establishing a TCP6 connection carrying a small MSS value. For example, the MSS value is 1. After the TCP6 server receives the request packet carrying the MSS value, the TCP6 connection is established. The TCP6 client may then send large numbers of requests to the server by an application, causing the TCP6 server to generate large numbers of reply packets. This may burden the TCP6 server or network, causing denial of service (DoS) attacks. To resolve this problem, run the **tcp ipv6 min-mss** command to set the minimum MSS value for a TCP6 connection. This configuration prevents a server from receiving packets carrying a small MSS value.


Example
-------

# Set the minimum MSS value for a TCP6 connection to 512 bytes.
```
<HUAWEI> system-view
[~HUAWEI] tcp ipv6 min-mss 512

```
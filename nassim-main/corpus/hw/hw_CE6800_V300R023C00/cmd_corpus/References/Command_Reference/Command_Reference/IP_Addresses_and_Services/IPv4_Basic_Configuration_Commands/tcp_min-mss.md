tcp min-mss
===========

tcp min-mss

Function
--------



The **tcp min-mss** command sets the minimum value of maximum segment size (MSS) for a TCP connection.

The **undo tcp min-mss** command restores the default minimum MSS value for a TCP connection.



By default, the minimum MSS value for TCP connections is 216 bytes.


Format
------

**tcp min-mss** *minmss-val*

**undo tcp min-mss** [ *minmss-val* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *minmss-val* | Specifies the minimum MSS value for a TCP connection. | The value is an integer ranging from 32 to 9600, in bytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To establish a TCP connection, the MSS value is negotiated, which indicates the maximum length of packets that the local device can receive. The TCP client on a network may send a request packet for establishing a TCP connection carrying a small MSS value. For example, the MSS value is 1. After the TCP server receives the request packet carrying the MSS value, the TCP connection is established. The TCP client may then send large numbers of requests to the server by an application, causing the TCP server to generate large numbers of reply packets. This may burden the TCP server or network, causing denial of service (DoS) attacks. To resolve this problem, run the **tcp min-mss** command to set the minimum MSS value for a TCP connection. This configuration prevents a server from receiving packets carrying a small MSS value.




Example
-------

# Set the minimum MSS value for a TCP connection to 512 bytes.
```
<HUAWEI> system-view
[~HUAWEI] tcp min-mss 512

```
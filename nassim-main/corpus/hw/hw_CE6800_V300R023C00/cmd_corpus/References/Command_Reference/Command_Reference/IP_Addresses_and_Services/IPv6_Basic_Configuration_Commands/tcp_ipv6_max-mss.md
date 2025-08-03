tcp ipv6 max-mss
================

tcp ipv6 max-mss

Function
--------



The **tcp ipv6 max-mss** command sets the maximum MSS value for a TCP6 connection.

The **undo ipv6 tcp ipv6 max-mss** command deletes the maximum MSS value of a TCP6 connection.



By default, the maximum MSS value is not configured for TCP6 connections.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tcp ipv6 max-mss** *max-mss-val*

**undo tcp ipv6 max-mss** [ *max-mss-val* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-mss-val* | Specifies the maximum MSS value for a TCP6 connection. | The value is an integer ranging from 32 to 9600, in bytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To establish a TCP6 connection, the MSS value is negotiated, which indicates the maximum length of packets that the local device can receive. If the path MTU is unavailable on one end of a TCP6 connection, this end cannot adjust the TCP6 packet size based on the MTU. As a result, this end may send TCP6 packets that are longer than the MTUs on intermediate devices, which will discard these packets. To prevent this problem, run the **tcp ipv6 max-mss** command on either end of a TCP6 connection to set the maximum MSS value of TCP6 packets. Then the MSS value negotiated by both ends will not exceed this maximum MSS value, and accordingly TCP6 packets sent from both ends will not be longer than this maximum MSS value and can travel through the intermediate network.


Example
-------

# Set the maximum MSS value for a TCP6 connection to 1024 bytes.
```
<HUAWEI> system-view
[~HUAWEI] tcp ipv6 max-mss 1024

```
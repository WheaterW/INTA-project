tcp max-mss
===========

tcp max-mss

Function
--------



The **tcp max-mss** command sets the maximum MSS value for a TCP connection.

The **undo tcp max-mss** command deletes the maximum MSS value of a TCP connection.



By default, the maximum MSS value is not configured for TCP connections.


Format
------

**tcp max-mss** *maxmss-val*

**undo tcp max-mss** [ *maxmss-val* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *maxmss-val* | Specifies the maximum MSS value for a TCP connection. | The value is an integer ranging from 32 to 9600, in bytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To establish a TCP connection, the MSS value is negotiated, which indicates the maximum length of packets that the local device can receive. This length is the TCP payload length, excluding that of the TCP header. If the path MTU is unavailable on one end of a TCP connection, this end cannot adjust the TCP packet size based on the MTU. As a result, this end may send TCP packets that are longer than the MTUs on intermediate devices, which will discard these packets. To prevent this problem, run the **tcp max-mss** command on either end of a TCP connection to set the maximum MSS value of TCP packets. Then the MSS value negotiated by both ends will not exceed this maximum MSS value, and accordingly TCP packets sent from both ends will not be longer than this maximum MSS value and can travel through the intermediate network.



**Precautions**



The maximum MSS value configured using the **tcp max-mss** command must be greater than the minimum MSS value. The default minimum MSS value is 216. If the minimum MSS value is not configured and the maximum MSS value is less than 216, the value 216 takes effect.




Example
-------

# Set the maximum MSS value for a TCP connection to 1024 bytes.
```
<HUAWEI> system-view
[~HUAWEI] tcp max-mss 1024

```
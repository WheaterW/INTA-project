dns forward retry-timeout
=========================

dns forward retry-timeout

Function
--------



The **dns forward retry-timeout** command sets the retransmission timeout period that the device sends Query packets to the destination DNS server.

The **undo dns forward retry-timeout** command restores the default retransmission timeout period.



By default, the retransmission timeout period for which the device sends DNS query requests to the destination DNS server is 3 seconds.


Format
------

**dns forward retry-timeout** *timeout-value*

**undo dns forward retry-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timeout-value* | Specifies the retransmission timeout period that the device sends Query packets to the destination DNS server. | The value is an integer that ranges from 1 to 15. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device can select the destination DNS server in auto or fixed mode. For details about the mode in which the device sends DNS request packets to the destination DNS server in each mode and precautions, see the **dns-server-select-algorithm** command.If the number of times for the device to retransmit DNS request packets to each destination DNS server is relatively large and the packet retransmission timeout period is relatively long, the time for the DNS client to wait for the response from the DNS server is too long. However, the request timeout period of the DNS client is shorter, so that the DNS client fails to properly receive response packets from the server. To enable the DNS server to quickly respond to DNS request packets, run the dns forward retry-number and **dns forward retry-timeout** commands to adjust the number of retransmission times and retransmission timeout period for the device to send DNS request packets to each DNS server, ensuring that the DNS client can properly receive response packets from the DNS server.You need to consider the number of times for the device to retransmit DNS query requests to the destination DNS server, retransmission timeout period, and mode for the device to select the DNS server into consideration before configuring the query timeout period on a device.

* When the mode for selecting the destination DNS server is auto, the query timeout period of the DNS device is calculated as follows: (Number of retransmission times + 1) x Retransmission timeout period.
* When the mode for selecting the destination DNS server is fixed, the query timeout period of the DNS device is calculated using the following formula: Query timeout period of the DNS device = (Number of retransmission times + 1) x Retransmission timeout period x Number of DNS servers.

Example
-------

# Set the retransmission timeout period that the device sends Query packets to the destination DNS server to 2 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dns forward retry-timeout 2

```
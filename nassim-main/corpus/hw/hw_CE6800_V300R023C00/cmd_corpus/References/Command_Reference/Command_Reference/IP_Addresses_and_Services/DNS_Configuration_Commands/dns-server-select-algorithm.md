dns-server-select-algorithm
===========================

dns-server-select-algorithm

Function
--------



The **dns-server-select-algorithm** command configures the DNS server selection mode of the device.

The **undo dns-server-select-algorithm** command restores the default setting.



By default, the device selects a DNS server in auto mode.


Format
------

**dns-server-select-algorithm** { **fixed** | **auto** }

**undo dns-server-select-algorithm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fixed** | Selects a DNS server in fixed mode. | - |
| **auto** | Selects a DNS server in auto mode. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device selects a DNS server in either of the following modes:

* When the DNS server mode is set to auto, the device uses an internal algorithm to calculate the priorities of all configured DNS servers (IP addresses of DNS servers can be configured using the **dns server** command) before sending a DNS query request. (The difference between the number of sent DNS request packets and the number of valid response packets from the DNS server is used as the criterion. If the difference is less than 3, the DNS server is available. If the difference is 0, the DNS server is of the high priority. Other DNS servers are of the second highest priority. The priority is updated each time a packet is sent or received.) Then, the DNS server sends a DNS query request to the DNS server with a higher priority. If the DNS server does not receive a response within the specified period, the DNS server sends a DNS query request to another DNS server with a higher priority. If the device still does not receive any response from the DNS server, it sends a DNS query request to the DNS server with the second highest priority. Repeat the preceding steps until a response is received or all configured DNS servers are queried in sequence. (If all available servers are used but retransmission is still required, the difference is cleared and the request is sent again according to the preceding rule.)
* When the DNS server mode is set to fixed, the device sends a DNS query request to the first configured DNS server. If no response is received within a specified period, the device resends the DNS query request. If the device does not receive any response from the DNS server after sending the DNS query request multiple times, the device sends a DNS query request to the next DNS server until it receives a response or queries all configured DNS servers.

**Precautions**

This function is supported when the device functions as a DNS client.When the device functions as a DNS client:

* This function is supported for DNS asynchronous query requests sent by the IPsec, PKI, HeathCheck, and AAA services.
* The DNS server selection mode cannot be configured for DNS synchronization query requests (for example, pinging domain names) initiated by the data-agent service. The device sends the requests according to the sequence in which DNS servers are configured. If no response is received, the device retransmits the requests according to the sequence in which DNS servers are configured.


Example
-------

# Configure the device to select a DNS server in fixed mode.
```
<HUAWEI> system-view
[~HUAWEI] dns-server-select-algorithm fixed

```
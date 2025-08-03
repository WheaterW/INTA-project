arp anti-attack rate-limit (System view)
========================================

arp anti-attack rate-limit (System view)

Function
--------



The **arp miss anti-attack rate-limit** command sets the rate limit of Address Resolution Protocol (ARP) Miss messages.

The **undo arp miss anti-attack rate-limit** command restores the default value.

The **arp anti-attack rate-limit** command sets the rate limit of Address Resolution Protocol (ARP) packets.

The **undo arp anti-attack rate-limit** command restores the default value.



By default, the global ARP miss message rate limit is enabled, and the value is 3000 pps.

By default, the global ARP packet rate limit is disabled.




Format
------

**arp anti-attack rate-limit** *limit*

**arp miss anti-attack rate-limit** *maximum*

**undo arp anti-attack rate-limit**

**undo arp miss anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit* | Specifies the rate limit of ARP packets globally. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP packets rate limit is disabled. |
| *maximum* | Specifies the rate limit of ARP miss messages globally. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP miss messages rate limit is disabled. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If unauthorized users use specific tools to send a large number of ARP packets to hosts in the local network segment or other network segments. Many ARP Miss packets are generated because MAC addresses corresponding to the destination IP addresses do not exist. As a result, the CPU will be busy with processing these ARP Miss messages, affecting other services. To resolve this problem, run the arp miss anti-attack rate-limit command to set a rate-limit value of ARP Miss messages, so that only a specified number of ARP Miss messages will be sent to the device for processing.If unauthorized users send a large number of ARP packets to a device. Many resources are diverted into processing these ARP packets, and the processing of other services is affected. To resolve this problem, run the arp anti-attack rate-limit (system view) command to set the limit-value of ARP packets, so that only a specified number of ARP packets will be sent to the device for processing.



**Configuration Impact**



After the rate-limit value of ARP Miss messages is set, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the upper limit, the device discards the excess ARP Miss messages. As a result, the device may fail to process some valid ARP Miss messages, causing service interruptions.After the rate-limit value is set, the device counts the number of received ARP packets. If the number of ARP packets received in a specified period exceeds the upper limit, the device discards the excess ARP packets. As a result, the device may fail to process some valid ARP packets, causing service interruptions.



**Precautions**



If the global rate limit is too low and the login through Telnet fails because the device receives a large number of attack packets, you can log in to the device through the Console port to increase the rate limit.




Example
-------

# Set the rate limit of Address Resolution Protocol (ARP) Miss messages.
```
<HUAWEI> system-view
[~HUAWEI] arp miss anti-attack rate-limit 100

```
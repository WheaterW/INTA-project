arp miss anti-attack rate-limit source-ip
=========================================

arp miss anti-attack rate-limit source-ip

Function
--------



The **arp miss anti-attack rate-limit source-ip** command sets a rate limit for ARP Miss messages based on source IP addresses.

The **undo arp miss anti-attack rate-limit source-ip** command restores the default rate limit of ARP Miss messages based on source IP addresses.



By default:

Source IP address-based ARP Miss message rate limiting is enabled, and a maximum of 50 ARP Miss messages can be processed per second. Global ARP Miss message rate limiting is enabled, and a maximum of 3000 ARP Miss messages can be processed per second.




Format
------

**arp miss anti-attack rate-limit source-ip maximum** *limit-value50*

**arp miss anti-attack rate-limit source-ip** *ipaddr-value* [ **mask** { *maskLen-value* | *mask-value* } ] **maximum** *limit-value50*

**undo arp miss anti-attack rate-limit source-ip**

**undo arp miss anti-attack rate-limit source-ip** *ipaddr-value* [ **mask** { *maskLen-value* | *mask-value* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-ip** *ipaddr-value* | Limits the rate of ARP Miss messages based on source IP addresses. | The value is in dotted decimal notation. |
| **mask** | Specifies ARP Miss message rate limit based on source IP addresses and masks. | - |
| *maskLen-value* | Specifies the mask length of a source IP address. | The value is an integer that ranges from 1 to 32. |
| *mask-value* | Specifies the mask of a source IP address. | The value is in dotted decimal notation. |
| **maximum** *limit-value50* | Specifies a rate limit of ARP Miss messages that carry a specified source IP address. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP or ARP Miss message rate limiting is disabled. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If unauthorized users use specific tools to send a large number of ARP packets to hosts in the local network segment or other network segments, many ARP Miss packets are generated because MAC addresses corresponding to the destination IP addresses do not exist. As a result, the CPU will be busy with processing these ARP Miss messages, affecting other services. To resolve this problem, run this command to set a rate limit for ARP Miss messages, so that only a specified number of ARP Miss messages will be sent to the device for processing.



**Configuration Impact**



After the rate limit of ARP Miss messages is set, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the upper limit, the device discards the excess ARP Miss messages. As a result, the device may fail to process some valid ARP Miss messages, causing service interruptions.



**Precautions**



If the global rate limit is too low and the login through Telnet fails because the device receives a large number of attack packets, you can log in to the device through the Console port to increase the rate limit.




Example
-------

# Set the value of ARP Miss message rate limit based on source IP addresses to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] arp miss anti-attack rate-limit source-ip 10.1.1.1 maximum 100

```
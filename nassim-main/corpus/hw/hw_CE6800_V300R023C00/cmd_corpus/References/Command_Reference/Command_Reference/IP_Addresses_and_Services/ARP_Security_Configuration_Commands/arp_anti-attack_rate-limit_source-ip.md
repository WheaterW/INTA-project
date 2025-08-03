arp anti-attack rate-limit source-ip
====================================

arp anti-attack rate-limit source-ip

Function
--------



The **arp anti-attack rate-limit source-ip** command configures a rate limit for ARP packets with a specified source IP address.

The **undo arp anti-attack rate-limit source-ip** command restores the default configuration.

The **arp anti-attack rate-limit source-mac** command configures a rate limit for ARP packets with a specified source MAC address.

The **undo arp anti-attack rate-limit source-mac** command restores the default configuration.

The **arp anti-attack rate-limit destination-ip** command configures a rate limit for ARP packets with a specified destination IP address.

The **undo arp anti-attack rate-limit destination-ip** command restores the default configuration.



By default:

ARP packet rate limiting based on source MAC addresses is disabled. However, ARP packet rate limiting based on source IP addresses is enabled and the rate limit is set to 50. ARP packet rate limiting based on destination IP addresses is also enabled and the rate limit is set to 500. The PAF file can be used for customization.




Format
------

**arp anti-attack rate-limit source-ip** [ *ipaddr-value* ] **maximum** *limit-value50*

**arp anti-attack rate-limit source-mac** [ *macaddr-value* ] **maximum** *limit-value0*

**arp anti-attack rate-limit destination-ip maximum** *limit-value500*

**undo arp anti-attack rate-limit source-ip** [ *ipaddr-value* ]

**undo arp anti-attack rate-limit source-mac** [ *macaddr-value* ]

**undo arp anti-attack rate-limit destination-ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **maximum** *limit-value50* | Specifies a rate limit for ARP packets with a specified source IP address. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP packets rate limit is disabled. |
| **maximum** *limit-value0* | Specifies a rate limit for ARP packets with a specified source MAC address. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP packets rate limit is disabled. |
| **maximum** *limit-value500* | Specifies a rate limit for ARP packets with a specified destination IP address. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP packets rate limit is disabled. |
| **source-mac** *macaddr-value* | Limits the rate of ARP packets based on source MAC addresses. | The value is in dotted decimal notation. |
| **destination-ip** | Limits the rate of ARP packets based on destination IP addresses. | - |
| **source-ip** *ipaddr-value* | Limits the rate of ARP packets based on source IP addresses. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When unauthorized users send a large number of ARP packets to attack a device, the device wastes a large number of resources in processing ARP packets, affecting the processing of other services. To solve this problem, you can configure the device to limit the rate of ARP packets so that the device can process a specified number of ARP packets within a specified period. This prevents a large number of resources from being wasted in processing ARP packets and ensures normal service running.



**Configuration Impact**



After a rate limit is configured for ARP packets, the device counts the number of ARP packets. If the number of ARP packets in a specified period exceeds the threshold, the device does not process the excess ARP packets. In this case, normal ARP packets may not be processed in time, causing service interruption.



**Precautions**



If a small global attack defense value has been configured and a large number of attacks occur, Telnet fails. Users can log in through the console port and change the global attack defense value to a proper value.




Example
-------

# Set the value of ARP packet rate limit based on source IP addresses to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] arp anti-attack rate-limit source-ip 10.1.1.1 maximum 100

```
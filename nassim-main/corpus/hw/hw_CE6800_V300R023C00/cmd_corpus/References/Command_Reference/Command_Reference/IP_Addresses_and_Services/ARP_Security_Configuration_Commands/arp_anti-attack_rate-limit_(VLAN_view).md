arp anti-attack rate-limit (VLAN view)
======================================

arp anti-attack rate-limit (VLAN view)

Function
--------



The **arp miss anti-attack rate-limit** command sets a rate limit for Address Resolution Protocol (ARP) Miss messages in a specified VLAN.

The **undo arp miss anti-attack rate-limit** command restores the default value.

The **arp anti-attack rate-limit** command sets a rate limit for Address Resolution Protocol (ARP) packets in a specified VLAN.

The **undo arp anti-attack rate-limit** command restores the default value.



By default, the default value is 0 pps.


Format
------

**arp anti-attack rate-limit** *limit-value*

**arp miss anti-attack rate-limit** *limit-value*

**undo arp anti-attack rate-limit**

**undo arp miss anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-value* | Specifies a rate limit for ARP Miss messages or ARP Packets in a specified VLAN. | The value is an integer ranging from 0 to 65536, in pps. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If unauthorized users use specific tools to send a large number of ARP packets to hosts in the local network segment or other network segments. Many ARP Miss packets are generated because MAC addresses corresponding to the destination IP addresses do not exist. As a result, the CPU will be busy with processing these ARP Miss messages, affecting other services. To resolve this problem, run the arp miss anti-attack rate-limit command to set the limit-value of ARP Miss messages, so that only a specified number of ARP Miss messages will be sent to the device for processing.If unauthorized users send a large number of ARP packets to a device. Many resources are diverted into processing these ARP packets, and the processing of other services is affected. To resolve this problem, run the arp anti-attack rate-limit command to set the limit-value of ARP packets, so that only a specified number of ARP packets will be sent to the device for processing.



**Configuration Impact**



After a rate limit is set for ARP Miss messages in a VLAN, the device counts the number of received ARP Miss messages in this VLAN. If the number of ARP Miss messages received in a specified period exceeds the upper limit, the device discards the excess ARP Miss messages. As a result, the device may fail to process some valid ARP Miss messages, causing service interruptions.After the rate-limit value is set, the specified VLAN counts the number of received ARP packets. If the number of ARP packets received in a specified period exceeds the upper limit, the device discards the excess ARP packets. As a result, the device may fail to process some valid ARP packets, causing service interruptions.



**Precautions**



If a small global attack defense value has been configured and a large number of attacks occur, Telnet fails. Users can log in through the console port and change the global attack defense value to a proper value.




Example
-------

# Set the rate-limit value of ARP packets for VLAN 20 to 100pps.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI-vlan20] arp anti-attack rate-limit 100

```

# Set the value of ARP Miss message rate limit for VLAN 20 to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI-vlan20] arp miss anti-attack rate-limit 100

```
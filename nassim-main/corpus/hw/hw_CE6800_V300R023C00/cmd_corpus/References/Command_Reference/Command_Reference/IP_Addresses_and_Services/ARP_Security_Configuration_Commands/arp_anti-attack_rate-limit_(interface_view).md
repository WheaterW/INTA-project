arp anti-attack rate-limit (interface view)
===========================================

arp anti-attack rate-limit (interface view)

Function
--------



The **arp anti-attack rate-limit** command sets a rate limit for ARP packets on an interface.

The **undo arp anti-attack rate-limit** command restores the default rate limit for ARP packets on an interface.



By default, the maximum rate of ARP packets is set to 0, that is, the rate of ARP packets is not limited on an interface.


Format
------

**arp anti-attack rate-limit** *limit-value*

**undo arp anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rate-limit** *limit-value* | Specifies a rate limit for ARP packets on an interface. | The value is an integer that ranges from 0 to 10000, in pps. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If unauthorized users send a large number of ARP packets to a device. Many resources are diverted into processing these ARP packets, and the processing of other services is affected. To resolve this problem, run the arp anti-attack rate-limit command to set the ARP packet rate limit, enabling the device to discard excessive ARP packets.

**Configuration Impact**

After the rate limit value is set, the device counts the number of received ARP packets. If the number of ARP packets received on an interface in a specified period exceeds the upper limit, the device discards the excess ARP packets.

**Precautions**



For the CE6885-LL in low latency mode, ARP port rate limiting and DAI are mutually exclusive and cannot be configured together.




Example
-------

# Set the rate limit of ARP packets to 100 pps.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] arp anti-attack rate-limit 100

```
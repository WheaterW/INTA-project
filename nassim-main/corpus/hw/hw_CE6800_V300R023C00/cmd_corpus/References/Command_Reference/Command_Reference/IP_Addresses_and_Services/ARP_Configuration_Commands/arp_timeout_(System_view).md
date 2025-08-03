arp timeout (System view)
=========================

arp timeout (System view)

Function
--------



The **arp timeout** command sets the aging time of dynamic Address Resolution Protocol (ARP) entries.

The **undo arp timeout** command restores the default setting.



By default, the aging time of dynamic ARP entries is 1200 seconds, namely, 20 minutes.


Format
------

**arp timeout** *expire-time*

**undo arp timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-time* | Specifies the aging time of dynamic ARP entries. | The value is an integer ranging from 30 to 86400, |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To ensure communication reliability, you need to update ARP entries when they are invalid. A dynamic ARP entry has a life cycle. If a dynamic ARP entry is not updated before its life cycle ends, this dynamic ARP entry will be deleted from the ARP table. The life cycle is called aging time. If the entry is updated before its life cycle expires, the aging time of the entry is recalculated. You can run the arp timeout command to adjust aging time for ARP entries to ensure their updating.



**Prerequisites**



The **arp constant-send enable** command has been run in the system view to enable the device to send ARP packets at a constant rate if the aging time of ARP entries is shorter than 60 seconds.



**Configuration Impact**

* If the aging time set for a dynamic ARP entry is short, the refreshment for the ARP entry will consume huge number of system resources, causing adverse impacts on other services, a network flapping and even traffic forwarding.
* If the aging time set for a dynamic ARP entry is long, the ARP entry will not be promptly updated when it is invalid. For example, if a device fails to work or a network card is changed but the invalid ARP entry has not updated yet, the device sends packets to the peer device based on the existing ARP entry. As a result, the service will be interrupted.

**Precautions**



After this command is run, the aging time of dynamic ARP entries is changed on an interface.




Example
-------

# Set the aging time of dynamic ARP entries on system-view to 600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] arp timeout 600

```
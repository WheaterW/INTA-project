arp timeout
===========

arp timeout

Function
--------



The **arp timeout** command sets the aging time of dynamic ARP entries.

The **undo arp timeout** command deletes the aging time of dynamic ARP entries.



By default, the aging time of dynamic ARP entries is 1200 seconds, namely, 20 minutes.


Format
------

**arp timeout** *expire-time*

**undo arp timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-time* | Specifies the aging time of dynamic ARP entries. | The value is an integer ranging from from 30 to 86400. The value range of this parameter is controlled by the PAF file. After the PAF file is loaded, the value range of this parameter is 1 to 86400. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure communication reliability, you need to update ARP entries when they are invalid. A dynamic ARP entry has a life cycle. If a dynamic ARP entry is not updated before its life cycle ends, this dynamic ARP entry will be deleted from the ARP table. The life cycle is called aging time. If the entry is updated before its life cycle expires, the aging time of the entry is recalculated. You can run the **arp timeout** command to adjust aging time for ARP entries to ensure their updating. An aging time configured using the **arp timeout** command takes effect from the next lifetime after the current lifetime expires.

**Prerequisites**



Before setting the aging time to a value less than 60 seconds, run the **arp constant-send enable** command in the system view to enable the device to send ARP packets at a constant rate.If the aging time is set to a value less than 30s, you need to enable the device to send ARP packets at a constant rate and run the **arp detect mode unicast** command on the interface to unicast ARP aging probe packets.



**Configuration Impact**

* If the aging time set for a dynamic ARP entry is short, the refreshment for the ARP entry will consume huge number of system resources, causing adverse impacts on other services, a network flapping and even traffic forwarding.
* If the aging time set for a dynamic ARP entry is long, the ARP entry will not be promptly updated when it is invalid. For example, if a device fails to work or a network card is changed but the invalid ARP entry has not updated yet, the device sends packets to the peer device based on the existing ARP entry. As a result, the service will be interrupted.

**Precautions**

After this command is run, the aging time of dynamic ARP entries is changed on an interface.


Example
-------

# Set the aging time of dynamic ARP entries on the interface to 600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp timeout 600

```
arp constant-send enable
========================

arp constant-send enable

Function
--------



The **arp constant-send enable** command enables the device to send ARP packets at a constant rate.

The **undo arp constant-send enable** command restores the default setting.



By default, the device is not enabled to send ARP packets at a constant rate.


Format
------

**arp constant-send enable**

**undo arp constant-send enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, a device broadcasts ARP aging probe and Miss messages at varied rates. If the number of ARP packets received by the peer device exceeds its processing capability, packets may be lost and services may be affected. To resolve the problem, run the **arp constant-send enable** command to enable the device to send ARP packets at a constant rate. Then, run the **arp constant-send maximum** command to set a proper constant rate as needed.




Example
-------

# Enable the device to send ARP packets at a constant rate.
```
<HUAWEI> system-view
[~HUAWEI] arp constant-send enable

```
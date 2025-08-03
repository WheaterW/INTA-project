arp gratuitous-arp send interval (System view)
==============================================

arp gratuitous-arp send interval (System view)

Function
--------



The **arp gratuitous-arp send interval** command sets an interval at which a device sends gratuitous Address Resolution Protocol (ARP) packets.

The **undo arp gratuitous-arp send interval** command restores the default interval at which a device sends gratuitous ARP packets.



By default, a device sends gratuitous ARP packets at an interval of 60s.


Format
------

**arp gratuitous-arp send interval** *interval*

**undo arp gratuitous-arp send interval** [ *interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which a device sends gratuitous ARP packets. | The value is an integer ranging from 1 to 86400, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, after a device or interface is enabled to send gratuitous ARP packets, the device sends them at an interval of 60s. To change the interval, you can run thearp gratuitous-arp send interval command.

* If the interval is configured only in the system view, the configuration takes effect on all interfaces.
* If the interval is configured in both the system and interface views, the configuration in the interface view takes precedence.

**Prerequisites**



A device has been enabled to periodically send gratuitous ARP packets using the **arp gratuitous-arp send enable** command.




Example
-------

# Enable a device to send gratuitous ARP packets at an interval of 100s.
```
<HUAWEI> system-view
[~HUAWEI] arp gratuitous-arp send interval 100

```
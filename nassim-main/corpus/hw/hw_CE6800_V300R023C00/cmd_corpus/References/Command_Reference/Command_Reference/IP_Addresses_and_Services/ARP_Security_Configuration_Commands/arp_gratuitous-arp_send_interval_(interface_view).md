arp gratuitous-arp send interval (interface view)
=================================================

arp gratuitous-arp send interval (interface view)

Function
--------

The **arp gratuitous-arp send interval** command sets an interval at which an interface sends gratuitous Address Resolution Protocol (ARP) packets.

The **undo arp gratuitous-arp send interval** command restores the default interval at which an interface sends gratuitous ARP packets.

By default, an interface sends gratuitous ARP packets at an interval of 60s.



Format
------

**arp gratuitous-arp send interval** *interval*

**undo arp gratuitous-arp send interval** [ *interval* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which an interface sends gratuitous ARP packets. | The value is an integer ranging from 1 to 86400, in seconds. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

By default, after a device or interface is enabled to send gratuitous ARP packets, the interface sends them at an interval of 60s. To change the interval, you can run the arp gratuitous-arp send interval command.

* If the interval is configured only in the system view, the configuration takes effect on all interfaces.
* If the interval is configured in both the system and interface views, the configuration in the interface view takes precedence.

**Prerequisites**

An interface has been enabled to periodically send gratuitous ARP packets using the **arp gratuitous-arp send enable** command.



Example
-------

# Enable an interface to send gratuitous ARP packets at an interval of 100s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/3
[~HUAWEI-100GE1/0/3] undo portswitch
[*HUAWEI-100GE1/0/3] arp gratuitous-arp send interval 100

```
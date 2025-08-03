arp constant-send maximum
=========================

arp constant-send maximum

Function
--------



The **arp constant-send maximum** command sets a constant rate for a device to send ARP packets.

The **undo arp constant-send maximum** command restores the default setting.



By default, the device sends 5 packets per 10 ms.


Format
------

**arp constant-send maximum** *maximum-value*

**undo arp constant-send maximum** [ *maximum-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *maximum-value* | Specifies a constant rate at which ARP packets are sent. Specifically, this parameter indicates the number of ARP packets that the device can send per 10 ms. | The value is an integer ranging from 1 to 20. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a device is enabled to send ARP packets at a constant rate, the device sends 5 ARP packets every 10 ms by default. To adjust the constant rate, run the **arp constant-send maximum** command. A proper constant rate can help prevent services from being affected on the peer device.



**Prerequisites**



The **arp constant-send enable** command has been run to enable the device to send ARP packets at a constant rate.



**Precautions**



The default setting is recommended.




Example
-------

# Set the constant rate for sending ARP packets to 8 packets per 10 ms.
```
<HUAWEI> system-view
[~HUAWEI] arp constant-send enable
[*HUAWEI] arp constant-send maximum 8

```
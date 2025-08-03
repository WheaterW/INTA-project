arp smart-discover interval count
=================================

arp smart-discover interval count

Function
--------



The **arp smart-discover interval count** command configures an interval at which a device sends ARP probe messages and the number of ARP probe messages to be sent in each interval.

The **undo arp smart-discover interval count** command restores the default configuration.



By default, the interval at which a device sends ARP probe messages and the number of ARP probe messages to be sent in each interval are 1 second and 128, respectively.


Format
------

**arp smart-discover interval** *interval-value* **count** *count-value*

**undo arp smart-discover interval** *interval-value* **count** *count-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies an interval at which a device sends ARP probe messages. | The value is an integer ranging from 1 to 60, in seconds. The default value is 1. |
| *count-value* | Specifies the number of ARP probe messages to be sent in each interval. | The value is an integer ranging from 1 to 512, in steps of 8. For example, the value can be 1, 8, or 16. The default value is 128. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **arp smart-discover interval count** command to configure an interval at which a device sends ARP probe messages and the number of ARP probe messages to be sent in each interval, improving the flexibility of ARP active detection.

**Precautions**

1. If a large interval is configured or the number of ARP probe messages to be sent within the interval is set to a small value, a device learns ARP entries of hosts connected to it at a low rate.
2. If the number of ARP probe messages to be sent within the interval is set to a large value, a device sends a large number of ARP probe messages per second, affecting the performance of hosts connected to the device.

Example
-------

# Set an interval at which a device sends ARP probe messages and the number of ARP probe messages to be sent in each interval to 5 seconds and 256, respectively.
```
<HUAWEI> system-view
[~HUAWEI] arp smart-discover interval 5 count 256

```
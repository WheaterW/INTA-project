qos statistics ifg
==================

qos statistics ifg

Function
--------



The **qos statistics ifg enable** command configures the device to count the inter-frame gap and preamble of Ethernet frames when the device collects traffic statistics.

The **undo qos statistics ifg enable** command restores the default configuration.



By default, the frame gap and preamble of Ethernet frames are not included in the traffic statistics.


Format
------

**qos statistics ifg enable**

**undo qos statistics ifg enable**


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

The gap between Ethernet frames is called the inter-frame gap, which is of 12 bytes.The Ethernet frame length is from the destination MAC address to the FCS. The 8-byte preamble is appended to an outgoing Ethernet frame and used for synchronization. When the receiver receives the preamble, it determines that the received one is an Ethernet frame.After the statistics enable (traffic behavior view) command is used to configure traffic statistics, the device does not count the inter-frame gap and preamble of Ethernet frames by default during traffic statistics collection. After the **qos statistics ifg enable** command is used, the device calculates the inter-frame gap and preamble of Ethernet frames during traffic statistics collection.


Example
-------

# Configure the device to count the inter-frame gap and preamble of packets when the device calculates traffic statistics.
```
<HUAWEI> system-view
[~HUAWEI] qos statistics ifg enable

```
qos car ifg disable
===================

qos car ifg disable

Function
--------



The **qos car ifg disable** command configures the device not to count the inter-frame gap and preamble of packets when the device calculates the traffic policing rate or inbound rate limit of an interface.

The **undo qos car ifg disable** command restores the default configuration.



By default, the device counts the inter-frame gap and preamble of packets when the device calculates the traffic policing rate or inbound rate limit of an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos car ifg disable**

**undo qos car ifg disable**


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



An inter-frame gap is required between Ethernet frames. The default length of an inter-frame gap is 12 bytes.The length of an Ethernet frame starts from the destination MAC address and ends with the FCS. A preamble is added before the Ethernet frame is sent. The preamble is used for synchronization. After receiving the preamble, the receiver determines that the received packet is an Ethernet frame. The preamble has eight bytes.After traffic policing or inbound rate limiting is configured on an interface, the device counts the inter-frame gap and preamble of packets when calculating the traffic policing rate and inbound rate limiting rate. As a result, the calculated rate is inaccurate. After this command is configured, the device does not count the inter-frame gap and preamble when calculating the rate. This ensures the accuracy of the traffic policing rate and inbound rate limiting rate on an interface.The qos car ifg disable command affects rate calculation for traffic policing and inbound rate limiting only after the car (traffic behavior view) and qos car inbound commands are used to configure traffic policing and inbound rate limiting on an interface. The device does not count the inter-frame gap and preamble when calculating the rate.



**Precautions**

* Before this command is run, the formula for calculating the traffic policing rate or inbound rate limit on an interface is as follows: Traffic policing rate or inbound rate limit on an interface = (Original packet length + Inter-frame gap + Preamble) x Number of forwarded packets per second.
* After this command is run, the formula for calculating the traffic policing rate or inbound rate limit on an interface is as follows: Traffic policing rate or inbound rate limit on an interface = Original packet length x Number of forwarded packets per second.


Example
-------

# Configure the device not to count the inter-frame gap and preamble of packets when the device calculates the traffic policing rate or inbound rate limit of an interface.
```
<HUAWEI> system-view
[~HUAWEI] qos car ifg disable

```
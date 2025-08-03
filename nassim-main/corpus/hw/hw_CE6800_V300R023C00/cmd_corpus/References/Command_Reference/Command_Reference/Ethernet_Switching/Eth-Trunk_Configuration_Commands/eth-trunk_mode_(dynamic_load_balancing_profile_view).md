eth-trunk mode (dynamic load balancing profile view)
====================================================

eth-trunk mode (dynamic load balancing profile view)

Function
--------



The **eth-trunk mode** command configures the dynamic load balancing mode for a LAG.

The **undo eth-trunk mode** command restores the default dynamic load balancing mode for a LAG.



By default, a LAG uses the eligible dynamic load balancing mode, in which the flowlet interval is 1000.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**eth-trunk mode** { **spray** | **fixed** | **eligible** [ **flowlet-gap-time** *gap-time* ] }

**undo eth-trunk mode** [ **spray** | **fixed** | **eligible** [ **flowlet-gap-time** *gap-time* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **spray** | Enables the spray dynamic load balancing mode for a LAG.  In spray dynamic load balancing mode, a device selects a member link with the lightest load to forward data packets. | - |
| **fixed** | Enables the fixed dynamic load balancing mode for a LAG.  In fixed dynamic load balancing mode, a device forwards a data packet through the link for forwarding the previous data packet. The time interval is 2 seconds. If the data packet to be forwarded is the first packet in a flow, the device forwards it through one of the member links in static load balancing mode based on the hash result. | - |
| **eligible** | Enables the eligible dynamic load balancing mode for a LAG.  In eligible dynamic load balancing mode, based on the flowlet, a device selects a member link with the lightest load to forward the data packet. Data packets in the same flowlet are forwarded through the same link. | - |
| **flowlet-gap-time** *gap-time* | Specifies the flowlet interval. A device splits a flow into flowlets based on this parameter. | The value is an integer that ranges from 16 to 32000. The unit is 1024 nanoseconds. |



Views
-----

Dynamic load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can change the dynamic load balancing mode for a LAG based on the network traffic to provide maximum load balancing between member links. The eligible dynamic load balancing mode is recommended.

**Precautions**

* If you run the eth-trunk mode command multiple times, only the latest configuration takes effect.- Load balancing is valid only for outgoing traffic; therefore, the load balancing modes for the interfaces at both ends of a link can be different and do not affect each other.- The value of flowlet-gap-time must be greater than or equal to the maximum transmission delay on links that are load balanced.- In the spray dynamic load balancing mode, if the interval between two neighboring data packets in the same flow is less than the maximum transmission delay on links that are load balanced and the data packets are forwarded through different links, packet mis-sequencing may occur when the two packets arrive at the receive end. Therefore, the spray dynamic load balancing mode is applicable only to scenarios where packet mis-sequencing is allowed.

Example
-------

# Enable the fixed dynamic load balancing mode for a LAG in the dynamic load balancing profile test.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile dynamic test
[*HUAWEI-load-balance-profile-dynamic-test] eth-trunk mode fixed

```
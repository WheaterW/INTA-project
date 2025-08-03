ecmp mode(ECMP load balancing view)
===================================

ecmp mode(ECMP load balancing view)

Function
--------



The **ecmp mode** command configures the dynamic load balancing mode for an ECMP.

The **undo ecmp mode** command restores the default dynamic load balancing mode for an ECMP.



By default, the dynamic load balancing mode of an ECMP is eligible, and the interval in a flowlet is 2000.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**ecmp mode** { **spray** | **fixed** | **eligible** [ **flowlet-gap-time** *gap-time* ] }

**undo ecmp mode** { **spray** | **fixed** | **eligible** [ **flowlet-gap-time** *gap-time* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **spray** | Enables the spray dynamic load balancing mode for an ECMP.  In spray dynamic load balancing mode, a device selects a member link with the lightest load to forward data packets. | - |
| **fixed** | Sets the dynamic load balancing mode of an ECMP to fixed.  In this mode, the to-be-forwarded data packet is forwarded along the forwarding path of the previous data packet in the flow to which the to-be-forwarded data packet belongs at an interval of 2 seconds. If the data packet to be forwarded is the first data packet in the flow to which the data packet belongs, the device selects a member link to forward the data packet based on the hash result in static load balancing mode. | - |
| **eligible** | Enables the eligible dynamic load balancing mode for an ECMP.  In eligible dynamic load balancing mode, based on the flowlet, a device selects a member link with the lightest load to forward data packets. Data packets in the same flowlet are forwarded through the same link. | - |
| **flowlet-gap-time** *gap-time* | Specifies the interval at which data packets in a flowlet are transmitted. The device splits data flows into flowlets based on the flowlet interval. | The value is an integer that ranges from 16 to 32000. The unit is 1024 nanoseconds. |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can change the dynamic load balancing mode for an ECMP based on the network traffic to provide maximum load balancing between member links. The eligible dynamic load balancing mode is recommended.

**Precautions**

* If you run this command multiple times, only the latest configuration takes effect.
* Load balancing is valid only for outgoing traffic. Therefore, the load balancing modes of the devices at both ends of a link can be different and do not affect each other.
* After the dynamic load balancing mode is set to Spray, if the interval between two adjacent data packets of the same flow is less than the maximum transmission delay of each member link, and the device selects different forwarding links for the two data packets, in this case, packet disorder may occur at the receive end. Therefore, dynamic load balancing in spray mode applies only to scenarios where the packet time sequence is not concerned.
* If the value of flowlet-gap-time is less than the maximum transmission delay of each member link in load balancing mode, packet disorder may occur on the receive end. Therefore, the value of flowlet-gap-time must be greater than or equal to the maximum transmission delay of each member link in load balancing mode.

Example
-------

# Enable the fixed dynamic load balancing mode for an ECMP in the dynamic load balancing profile test.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[*HUAWEI-ecmp] ecmp mode fixed

```
maxage-lsa route-calculate-delay (OSPFv3 view)
==============================================

maxage-lsa route-calculate-delay (OSPFv3 view)

Function
--------



The **maxage-lsa route-calculate-delay** command configures a route calculation delay that is triggered when the device receives a MaxAge Router LSA.

The **undo maxage-lsa route-calculate-delay** command restores the default configuration.



By default, the delay time of route calculation is not set.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**maxage-lsa route-calculate-delay** *delay-interval*

**undo maxage-lsa route-calculate-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-interval* | Specifies a route calculation delay that is triggered when the device receives a MaxAge Router LSA. | The value is an integer ranging from 0 to 65535, in seconds. The default value is 20 seconds. If the value is set to 0, route calculation is not delayed when the device receives a MaxAge Router LSA. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device on the network fails, OSPFv3 LSAs are continuously aged or updated, causing route flapping and affecting normal service traffic. When a device receives a router LSA that has reached the maximum aging time, route calculation is delayed. To prevent route flapping, you can run the **maxage-lsa route-calculate-delay** command to set a delay for route calculation.


Example
-------

# Configure the device to delay route calculation for 200s when the device receives a MaxAge Router LSA.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] maxage-lsa route-calculate-delay 200

```
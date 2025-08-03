long-distance mode
==================

long-distance mode

Function
--------



The **long-distance mode** command configures the long-distance mode for an interface and enables the distance-based headroom check function.

The **undo long-distance mode** command cancels the configured long-distance mode for an interface.



By default, the distance-based headroom check function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**long-distance mode** { **level-1** | **level-10** | **level-25** | **level-50** | **level-100** }

**undo long-distance mode** { **level-1** | **level-10** | **level-25** | **level-50** | **level-100** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Limits the long distance to 1 km. | - |
| **level-10** | Limits the long distance to 10 km. | - |
| **level-25** | Limits the long distance to 25 km. | - |
| **level-50** | Limits the long distance to 50 km. | - |
| **level-100** | Limits the long distance to 100 km. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After PFC is enabled on an interface, a headroom buffer is allocated from the plane buffer of the interface to a lossless queue, and this headroom buffer will store the packets received after the queue sends PFC notification packets but before the upstream device stops sending packets. When lossless services on the live network have a long communication distance, a larger headroom buffer is required. Otherwise, packet loss may occur.The distance-based headroom buffer check function calculates the theoretically required headroom buffer space based on the configured long-distance mode (that is, link distance) and interface rate. The purpose of this function is to help avoid packet loss, which may occur if the required headroom buffer space is greater than the remaining buffer space of the plane where the current interface resides. After the headroom buffer optimization function is enabled on the interfaces at both ends of a direct link, the interfaces can send detection packets to each other to calculate the required headroom buffer space for lossless transmission on the link.

**Precautions**

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:You can run the display buffer optimization configuration command to view the calculation result of the distance-based headroom buffer check function.For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:You can run the display long-distance configuration command to view the calculation result of the distance-based headroom buffer check function.


Example
-------

# Set the long-distance mode of an interface to level-100.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] long-distance mode level-100

```
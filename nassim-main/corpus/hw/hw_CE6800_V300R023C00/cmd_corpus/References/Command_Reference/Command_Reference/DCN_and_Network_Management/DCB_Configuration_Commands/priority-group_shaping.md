priority-group shaping
======================

priority-group shaping

Function
--------



The **priority-group shaping** command enables traffic shaping for a priority group and sets shaping parameters.

The **undo priority-group shaping** command disables traffic shaping for a priority group.



By default, traffic shaping is disabled for a priority group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority-group** *pg-group-value* **shaping** **cir** *cir-value* { **kbps** | **mbps** | **gbps** } **pir** *pir-value* { **kbps** | **mbps** | **gbps** } [ **cbs** *cbs-value* { **kbytes** | **mbytes** } **pbs** *pbs-value* { **kbytes** | **mbytes** } ]

**undo priority-group** *pg-group-value* **shaping** [ **cir** *cir-value* { **kbps** | **mbps** | **gbps** } **pir** *pir-value* { **kbps** | **mbps** | **gbps** } [ **cbs** *cbs-value* { **kbytes** | **mbytes** } **pbs** *pbs-value* { **kbytes** | **mbytes** } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pg-group-value* | Specifies the value of a priority group. | Enumerated type. The values are as follows:   * 0:PG0 * 1:PG1 * 2:PG2 * 3:PG3 * 4:PG4 * 5:PG5 * 6:PG6 * 7:PG7 * 15:PG15 |
| **cir** *cir-value* | Specifies the committed information rate (CIR) for a priority group. | The value is an integer that ranges from 1 Mbit/s to 400 Gbit/s. |
| **kbps** | Specifies the rate unit as kbit/s. | - |
| **mbps** | Specifies the rate unit as mbit/s. | - |
| **gbps** | Specifies the rate unit as gbit/s. | - |
| **pir** *pir-value* | Specifies the peak information rate (PIR) for a priority group. | The value is an integer that ranges from 1 Mbit/s to 400 Gbit/s. |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS), which is the committed volume of burst traffic that can pass through an interface.  If this parameter is not specified, the CBS is 125 times the CIR.If this parameter is not specified, the CBS is 125 times the CIR. If the CBS exceeds the maximum value, the maximum value takes effect. | The value is an integer that ranges from 1 kilobyte to 512 megabytes. The default unit is kilobyte. |
| **kbytes** | Specifies that the CBS is expressed in kilobytes. | - |
| **mbytes** | Specifies that the CBS is expressed in megabytes. | - |
| **pbs** *pbs-value* | Specifies the peak burst size (PBS), which is the maximum volume of burst traffic that can pass through an interface.  If this parameter is not specified, the PBS is 125 times the PIR.If this parameter is not specified, the PBS is 125 times the PIR. If the PBS exceeds the maximum value, the maximum value takes effect. | The value is an integer that ranges from 1 kilobyte to 512 megabytes. The default unit is kilobyte. |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the rate of an interface on a downstream device is lower than that of an interface on an upstream device, traffic congestion may occur on the interface of the downstream device. In this case, you can configure traffic shaping for priority groups on the outbound interface of the upstream device and adjust the transmit rates of the priority groups.

**Precautions**

After traffic shaping is configured for priority groups, the system first processes traffic of the priority group configured with the CIR. Packets of other priority groups may be discarded. For example, when traffic shaping is configured for PG0 and the CIR approximates to the interface bandwidth, packets in PG1 and PG15 may be discarded.


Example
-------

# Set the CIR to 2 mbit/s, PIR to 4 mbit/s, CBS to 12 kbytes, and PBS to 24 kbytes for PG1.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] priority-group 1 shaping cir 2 mbps pir 4 mbps cbs 12 kbytes pbs 24 kbytes

```
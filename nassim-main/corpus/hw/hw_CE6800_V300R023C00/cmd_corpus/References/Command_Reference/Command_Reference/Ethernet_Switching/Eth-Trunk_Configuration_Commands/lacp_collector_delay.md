lacp collector delay
====================

lacp collector delay

Function
--------



The **lacp collector delay** command configures the value of the CollectorMaxDelay field in an LACPDU.

The **undo lacp collector delay** command restores the default value of the CollectorMaxDelay field in an LACPDU.



The default value of the CollectorMaxDelay field is 0 in an LACPDU.


Format
------

**lacp collector delay** *delay-time*

**undo lacp collector delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay** *delay-time* | Specifies the value of the CollectorMaxDelay field in an LACPDU. | The value is an integer ranging from 0 to 65535, in 10 microseconds. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A non-Huawei device is dual-homed to PE1 and PE2 through Eth-Trunk interfaces in static LACP mode. If PE1 and PE2 have different system software versions, the CollectorMaxDelay field in LACPDUs that PE1 and PE2 send may have different default values. As a result, the member interfaces of the non-Huawei CE will receive LACPDUs with different CollectorMaxDelay values, burdening the CE's CPU and affecting CE performance.To address this problem, run the **lacp collector delay** command on a PE to configure the value of the CollectorMaxDelay field, so that the CollectorMaxDelay field has the same value in LACPDUs sent by PE1 and PE2.



**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.




Example
-------

# Set the value of the CollectorMaxDelay field to 65535.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp collector delay 65535

```
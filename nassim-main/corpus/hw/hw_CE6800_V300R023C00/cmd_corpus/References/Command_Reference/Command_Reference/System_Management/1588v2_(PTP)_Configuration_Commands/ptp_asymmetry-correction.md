ptp asymmetry-correction
========================

ptp asymmetry-correction

Function
--------

The **ptp asymmetry-correction** command sets the asymmetrical delay correction value on a 1588v2 interface.

The **undo ptp asymmetry-correction** command cancels the configured asymmetrical delay correction value on a 1588v2 interface.

By default, the asymmetrical delay correction value is not configured on a 1588v2 interface.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp asymmetry-correction** { **negative** *negative-asymmetry-correction-value* | **positive** *positive-asymmetry-correction-value* }

**undo ptp asymmetry-correction**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **negative** *negative-asymmetry-correction-value* | Indicates the negative asymmetrical delay correction value. | The value is an integer that ranges from 0 to 2000000, in nanoseconds. |
| **positive** *positive-asymmetry-correction-value* | Indicates the positive asymmetrical delay correction value. | The value is an integer that ranges from 0 to 2000000, in nanoseconds. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

During path delay calculation, 1588v2 considers that the delays in the sending and receiving paths are the same by default and performs asymmetrical correction.

If the two delays are different, you need to configure an asymmetrical delay correction value. In this case, the device automatically considers this value in the path delay calculation complying with the Pdelay or Delay measurement mechanism.

Example
-------

# Set the delay correction value to 1 ns on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp asymmetry-correction positive 1

```
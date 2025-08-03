display clock source freq-deviation
===================================

display clock source freq-deviation

Function
--------



The **display clock source freq-deviation** command displays the frequency deviation values of clock sources.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display clock source freq-deviation**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display clock source freq-deviation command to view the frequency deviation values of clock sources. If the frequency deviation absolute value of a clock source is larger than or equal to 9.2, the frequency deviation detection status is abnormal. If the frequency deviation absolute value is less than 9.2, the frequency deviation detection status is normal.You can view the frequency deviation values of clock sources only after you enable synchronous Ethernet and frequency deviation detection.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the frequency deviation values of clock sources.
```
<HUAWEI> system-view
[~HUAWEI] display clock source freq-deviation
  Frequency deviation detect:     enable
  Source                               Freq-deviation-value
  ----------------------------------------------------------
    100GE1/0/1                          0.45ppm(normal)

```

**Table 1** Description of the **display clock source freq-deviation** command output
| Item | Description |
| --- | --- |
| Frequency deviation detect | Whether clock frequency deviation detection is enabled.   * enable: Clock frequency deviation detection is enabled. * disable: Clock frequency deviation detection is disabled. |
| Source | Interface clock reference source.  The asterisk (\*) indicates the clock source traced by the system. |
| Freq-deviation-value | Frequency deviation value. The format is Symbol (only negative signs are displayed)+Frequency deviation value+Unit (ppm)+Frequency deviation detection status.  If this field displays ---, the frequency deviation value of the clock source cannot be detected. |
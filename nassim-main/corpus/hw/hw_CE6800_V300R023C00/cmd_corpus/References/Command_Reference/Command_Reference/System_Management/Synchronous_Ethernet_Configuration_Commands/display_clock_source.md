display clock source
====================

display clock source

Function
--------



The **display clock source** command displays clock source information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display clock source**

**display clock source interface** { *interface-name* | *interface-type* *interface-number* }

**display clock source ptp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source** | Displays attributes of all clock sources. | - |
| **interface** *interface-name* | Displays information about a line clock source. | - |
| **interface** *interface-type* *interface-number* | Displays information about a line clock source. | - |
| **ptp** | Displays information about a PTP clock source. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

During routine maintenance, you can run the **display clock source** command to view information about all clock sources, including the traced clock source.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all clock sources, including the synchronized clock source.
```
<HUAWEI> display clock source
  System trace source State:   lock mode
  Current system trace source: ptp
  Frequency lock success:      yes

  Master board
  Source               Pri(sys)   In-SSM   Out-SSM   State          Ref
  ------------------------------------------------------------------------------
  ptp                  2          --       --        normal         yes

```

**Table 1** Description of the **display clock source** command output
| Item | Description |
| --- | --- |
| System trace source State | System clock status:   * lock mode: The system clock works in lock state. * free mode: The system clock works in free state. * hold mode: The system clock works in hold state. * into pull-in range: The system clock is within the frequency deviation range. * out of pull-in range: The system clock is out of the frequency deviation range. |
| Current system trace source | The clock source synchronized with the current system clock. |
| Frequency lock success | Whether frequency locking succeeds:   * yes: Frequency locking succeeds. * no: Frequency locking fails. |
| Master board | Master clock card. |
| Source | Name of a clock source. |
| Pri(sys) | Priority of a clock source. |
| In-SSM | SSM level of the received or configured clock signals. |
| Out-SSM | SSM quality level of output clock signals. |
| State | Status of a clock source.   * initial: The clock source is offline. * normal: The clock source works in normal state. * normal\*: The clock source is not included in the frequency offset detection range. * abnormal: The clock source works in abnormal state. * abnormal(phy): The port negotiation status of the electrical port card is abnormal. * abnormal(ssm): The ssm packet received by the clock source is abnormal. * holdoff: The clock source works in holdoff state. * wtr: The clock source works in WTR state. |
| Ref | Whether this clock source participates in clock source selection.   * Yes: This clock source participates in clock source selection. * No: This clock source does not participate in clock source selection. |
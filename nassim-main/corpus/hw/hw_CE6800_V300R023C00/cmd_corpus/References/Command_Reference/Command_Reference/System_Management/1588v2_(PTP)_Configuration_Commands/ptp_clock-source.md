ptp clock-source
================

ptp clock-source

Function
--------



The **ptp clock-source** command sets clock source parameters.

The **undo ptp clock-source** command restores default clock source parameters.



For details about the default parameter values of each attribute, see the parameter description.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp clock-source local** { **time-source** *time-source-value* | **clock-accuracy** *clock-accuracy-value* | **clock-class** *clock-class-value* | **priority1** *priority1-value* | **priority2** *priority2-value* }

**undo ptp clock-source local** { **time-source** | **clock-accuracy** | **clock-class** | **priority1** | **priority2** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **time-source** *time-source-value* | Specifies the value of a time source attribute. This parameter is configured only for the grandmaster clock. | The value is an integer ranging from 1 to 8. The default value for local is 8. The values supported (mapping between time-source-value values and time-source attributes) are as follows:   * 1 ATOMIC\_CLOCK * 2 GPS * 3 TERRESTRIAL\_RADIO * 4 PTP * 5 NTP * 6 HAND\_SET * 7 OTHER * 8 INTERNAL\_OSCILLATOR |
| **clock-accuracy** *clock-accuracy-value* | Specifies the precision of the clock source. | The value is a 2-digit hexadecimal number. The default value for local is 0x31. In 1588v2 mode, the values supported (mapping between clock-accuracy-value values and clock-accuracy attributes) are as follows:   * 20 The time is accurate to within 25 ns. * 21 The time is accurate to within 100 ns. * 22 The time is accurate to within 250 ns. * 23 The time is accurate to within 1 Î¼s. * 24 The time is accurate to within 2.5 Î¼s. * 25 The time is accurate to within 10 Î¼s. * 26 The time is accurate to within 25 Î¼s. * 27 The time is accurate to within 100 Î¼s. * 28 The time is accurate to within 250 Î¼s. * 29 The time is accurate to within 1 ms. * 2A The time is accurate to within 2.5 ms. * 2B The time is accurate to within 10 ms. * 2C The time is accurate to within 25 ms. * 2D The time is accurate to within 100 ms. * 2E The time is accurate to within 250 ms. * 2F The time is accurate to within 1s. * 30 The time is accurate to within 10s. * 31 The time is accurate to larger than 10s. * 80-FD Reserved for a PTP template. |
| **clock-class** *clock-class-value* | Specifies the class of a clock source. | The value is an integer ranging from 0 to 255. The default value for local is 187. The values supported (mapping between clock-class-value values and clock-class attributes) are as follows:   * 6. A clock of class 6 traces clock signals of the primary reference time source. The timescale distributed is the Precise Time Protocol (PTP). A clock of class 6 cannot function as a slave clock for other clocks in the same domain. * 7. If a clock of class 6 becomes incapable of tracing clock signals of the primary reference time source, the clock obtains class 7 and works in hold mode. The timescale distributed is PTP. A clock of class 7 cannot function as a slave clock for other clocks in the same domain. * 13. A clock of class 13 synchronizes clock signals with a specific clock source. The timescale distributed is arbitrary waveform (ARB). A clock of class 13 cannot function as a slave clock for other clocks in the same domain. * 14. If a clock of class 13 becomes incapable of tracing clock signals of a specific clock source, the clock obtains class 14 and works in hold mode. The timescale distributed is ARB. A clock of class 14 cannot function as a slave clock for other clocks in the same domain. * 52. A clock of class 7 becomes an alternative A clock because this clock of class 7 cannot meet hold requirements. A clock of class 52 cannot function as a slave clock for other clocks in the same domain. * 58. A clock of class 14 becomes an alternative A clock because this clock of class 14 cannot meet hold requirements. A clock of class 58 cannot function as a slave clock for other clocks in the same domain. * 187. A clock of class 7 becomes an alternative B clock because this clock of class 7 cannot meet hold requirements. A clock of class 187 can function as a slave clock for other clocks in the same domain. * 193. A clock of class 14 becomes an alternative B clock because this clock of class 14 cannot meet hold requirements. A clock of class 193 can function as a slave clock for other clocks in the same domain. * 248. Default clock class. A clock obtains class 248 if no class is defined for it. * 255. A clock of class 255 works in slave-only mode. |
| **priority1** *priority1-value* | Specifies the priority 1 value of clock signals. | The value is an integer that ranges from 0 to 255. The default value is 128. A smaller value indicates a higher priority. |
| **priority2** *priority2-value* | Specifies the priority 2 value of clock signals. | The value is an integer that ranges from 0 to 255. The default value is 128. A smaller value indicates a higher priority. |
| **local** | Indicates a local clock source. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In dynamic 1588v2 scenarios, the BMC clock source selection algorithm can automatically select the grandmaster clock and master node. This command is used to configure BMC parameters for the local clock source or external clock source.

**Precautions**

When a 1588v2-enabled device performs the dynamic BMC clock source selection algorithm, the device selects a clock source in the sequence of priority1> clock-class> clock-accuracy> priority2. That is, the device compares priority1 of the selected clock source first. If priority1 is the same, the device compares clock-class. The clock source with a higher priority becomes the master clock.


Example
-------

# Set the class of the local clock to 10.
```
<HUAWEI> system-view
[~HUAWEI] ptp enable
[*HUAWEI] ptp clock-source local clock-class 10

```

# Set the priority 1 value of the local clock to 1.
```
<HUAWEI> system-view
[~HUAWEI] ptp enable
[*HUAWEI] ptp clock-source local priority1 1

```

# Set the time precision of the local clock to be greater than 10s.
```
<HUAWEI> system-view
[~HUAWEI] ptp enable
[*HUAWEI] ptp clock-source local clock-accuracy 31

```

# Select an atomic clock as a local clock source.
```
<HUAWEI> system-view
[~HUAWEI] ptp enable
[*HUAWEI] ptp clock-source local time-source 1

```

# Set the priority 2 value of the local clock to 1.
```
<HUAWEI> system-view
[~HUAWEI] ptp enable
[*HUAWEI] ptp clock-source local priority2 1

```
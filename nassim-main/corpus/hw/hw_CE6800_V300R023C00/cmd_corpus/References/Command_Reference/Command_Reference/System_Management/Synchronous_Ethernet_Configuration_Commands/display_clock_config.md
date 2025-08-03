display clock config
====================

display clock config

Function
--------



The **display clock config** command displays clock synchronization configurations.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display clock config**


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

After you complete clock synchronization configurations on the switch, you can run the **display clock config** command to view the configuration results.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display clock synchronization configurations.
```
<HUAWEI> display clock config
 ethernet synchronization   :enable
 clock freq deviation detect:disable
 clock unk map              :dnu
 system pll run mode        :normal
 source input threshold     :sec

 switch config
    sys pll                 :auto mode
    SSM control             :off
    Extend SSM control      :off
    internal clockid        :0
    switch mode             :revertive
    wtr                     :5min
    holdoff time            :1000ms

 source config
 100GE1/0/1
    Sync enable
    Pri(sys)                :1

 ptp
    Sync enable
    Pri(sys)                :2

```

**Table 1** Description of the **display clock config** command output
| Item | Description |
| --- | --- |
| clock freq deviation detect | Whether frequency deviation detection is enabled for clock signals:   * enable: Frequency deviation detection is enabled for clock signals. * disable: Frequency deviation detection is disabled for clock signals. |
| clock unk map | Mapped SSM quality level of the clock source with an SSM quality level of UNK. |
| ethernet synchronization | Whether synchronous Ethernet is enabled:   * enable: Synchronous Ethernet is enabled. * disable: Synchronous Ethernet is disabled. |
| system pll run mode | Status of the system PLL. |
| source input threshold | Input SSM threshold of the clock source:   * prc. * ssua. * ssub. * sec. * dnu. |
| source config | Clock source configuration. |
| switch config | Clock source selection configuration. |
| switch mode | Clock recovery mode:   * revertive: revertive mode. * non-revertive: non-revertive mode. |
| sys pll | System PLL. |
| SSM control | Whether SSM quality levels are used for clock source selection:   * on: SSM quality levels are used for clock source selection. * off: SSM quality levels are not used for clock source selection. |
| Extend SSM control | Whether extended SSM function is enabled:   * on: Extended SSM function is enabled. * off: Extended SSM function is disabled. |
| internal clockid | Clock ID of an internal clock source. |
| wtr | WTR time for the status change after the failed clock source recovers (the effective clock source type does not include the PTP frequency source). |
| holdoff time | Hold time after clock source signals become invalid. |
| Sync enable | Clock synchronization enabled for the clock source. |
| Pri(sys) | Indicates the priority of the clock source participating in system clock source selection. |
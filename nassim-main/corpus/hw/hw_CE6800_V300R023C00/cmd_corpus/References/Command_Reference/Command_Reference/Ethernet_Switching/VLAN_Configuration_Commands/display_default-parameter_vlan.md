display default-parameter vlan
==============================

display default-parameter vlan

Function
--------



The **display default-parameter vlan** command displays default configurations of a VLAN.




Format
------

**display default-parameter vlan** *vlan-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays default configurations of a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

No configuration file is generated for default configurations. To view default VLAN configurations, run the display default-parameter vlan command. The default configurations do not change with VLAN configurations.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display default configurations of VLAN 4.
```
<HUAWEI> display default-parameter vlan 4
  VLAN ID             : 4
  Type                : Common
  Status              : Undo shutdown
  Broadcast           : Forward
  Unknown multicast   : Forward
  Unknown unicast     : Forward
  Statistics          : Disable
  MAC learning        : Enable
  Property            : Default
  Description         : VLAN 0004

```

**Table 1** Description of the **display default-parameter vlan** command output
| Item | Description |
| --- | --- |
| VLAN ID | VLAN ID. |
| Type | VLAN type:   * Common: common VLAN. * \*common: management VLAN.   The default value is Common. |
| Status | VLAN status:   * undo shutdown. * shutdown.   The default value is undo shutdown. |
| Broadcast | Action on broadcast packets:   * Forward. * Discard.   The default value is Forward. |
| Unknown multicast | Action on unknown multicast packets:   * Forward. * Discard.   The default value is Forward. |
| Unknown unicast | Action on unknown unicast packets:   * Forward. * Discard.   The default value is Forward. |
| Statistics | Whether collection of statistics about VLAN packets are enabled:   * Enable. * Disable.   The default value is Disable. |
| MAC learning | Whether MAC address learning is enabled:   * Enable. * Disable.   The default value is Enable. |
| Property | VLAN attribute:   * backboneVLAN: backbone network VLAN. * multicastVLAN: multicast VLAN without changing the VLAN attribute. * userVLAN: multicast VLAN without changing the VLAN attribute. * default: common VLAN.   The default value is default. |
| Description | VLAN description that helps users learn VLAN functions.  You can run the description command in the VLAN view to configure or modify the description. |
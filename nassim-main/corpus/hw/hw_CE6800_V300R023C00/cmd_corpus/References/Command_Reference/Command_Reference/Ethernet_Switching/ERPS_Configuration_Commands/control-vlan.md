control-vlan
============

control-vlan

Function
--------



The **control-vlan** command configures a control VLAN for an ERPS ring to forward R-APS PDUs.

The **undo control-vlan** command deletes the configured control VLAN.



By default, no control VLAN is configured on an ERPS ring.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**control-vlan** *vlan-id*

**undo control-vlan**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the ID of a control VLAN for an ERPS ring. | The value is an integer that ranges from 1 to 4094. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an ERPS ring is created, run the **control-vlan** command to create a control VLAN. Unlink data VLAN which is used to transmit data packets, the control VLAN is used only to transmit R-APS PDUs in an ERPS ring. This improves ERPS security.

**Configuration Impact**

ERPS control and service VLANs are mutually exclusive.

**Precautions**

* The same control VLAN must be configured for all devices on an ERPS ring
* The same control VLAN cannot be used by different ERPS rings.
* If you need to check whether the control VLAN is created or determine which control VLAN is configured to transmit R-APS PDUs, run the **display erps** command.

Example
-------

# Configure control VLAN 5 for ERPS ring 1.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1
[*HUAWEI-erps-ring1] control-vlan 5

```
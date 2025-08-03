igmp snooping report-suppress
=============================

igmp snooping report-suppress

Function
--------



The **igmp snooping report-suppress** command enables the suppression of IGMP Report messages.

The **undo igmp snooping report-suppress** command disables the suppression of IGMP Report messages.



By default, the suppression for IGMP Report messages is disabled.


Format
------

**igmp snooping report-suppress**

**undo igmp snooping report-suppress**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the igmp snooping report-suppress command is enabled, the device is set to the host mode. When sending Report or Leave messages to the upstream multicast device for the first time, the device sends a robustness variable number of Report or Leave message copies. Subsequently, when periodically responding to IGMP Query messages from the upstream multicast device, the device sends only one IGMP Report message to the upstream multicast device, regardless of the number of ports in the corresponding multicast group. This reduces traffic on the network side. The default robustness variable is 2. You can run the igmp snooping robust command to change the robustness variable.

**Precautions**

The configuration in the VLAN view fails in the following situations:

* PIM-SM has been enabled on the VLANIF interface of the VLAN using the **pim sm** command.
* The IGMP snooping proxy function has been configured for the VLAN using the **igmp snooping proxy** command.

It is recommended that the IGMP version configured on the upstream device be the same as that configured on the local device.



Example
-------

# Enable the suppression of IGMP Report messages in the view of VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping report-suppress

```
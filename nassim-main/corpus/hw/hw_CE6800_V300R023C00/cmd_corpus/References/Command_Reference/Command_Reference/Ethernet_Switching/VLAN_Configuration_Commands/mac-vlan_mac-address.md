mac-vlan mac-address
====================

mac-vlan mac-address

Function
--------



The **mac-vlan mac-address** command configures VLAN classification based on MAC addresses and sets 802.1p priorities for the MAC address-based VLANs.

The **undo mac-vlan mac-address** command deletes the configuration.



By default, MAC address-based VLAN classification is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-vlan mac-address** *mac-address* [ **priority** *priority* ]

**undo mac-vlan mac-address** { *mac-address* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a unicast MAC address. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number, such as 00e0 and fc01. If an H contains less than four hexadecimal digits, 0s are added ahead. For example, e0 is equal to 00e0. A MAC address cannot be full 0s or full 1s. |
| **priority** *priority* | Specifies the 802.1p priority of the VLAN to be associated with the MAC address.  You can specify the 802.1p priority of the VLAN to be associated with the specific MAC address. In this manner, when the switching device is congested, the switching device preferentially sends frames with high priorities. | The value is an integer that ranges from 0 to 7. The greater the value, the higher the priority. The default value is 0. |
| **all** | Indicates all static MAC-VLAN entries. | - |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure VLAN classification based on MAC addresses, run the mac-vlan mac-address command. MAC address-based VLAN classification frees you from reconfiguring VLANs for users whose physical locations change. This improves user security and increases user access flexibility.

**Configuration Impact**

VLANs configured based on MAC addresses process only untagged frames, and treat tagged frames in the same way as VLANs configured based on interfaces.After receiving an untagged frame, an interface searches for a MAC-VLAN mapping entry based on the source MAC address in the frame.

* If an entry is found, the interface forwards the frame based on the VLAN ID and priority value in the entry.
* If no entry is found, the interface matches the frame against other rules.

Example
-------

# Assign MAC address 00e0-fc12-3456 to VLAN 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] mac-vlan mac-address 00e0-fc12-3456

```
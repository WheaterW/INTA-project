mac-address limit (VLAN view)
=============================

mac-address limit (VLAN view)

Function
--------



The **mac-address limit** command configures a MAC address learning limit rule for a VLAN to set the maximum number of MAC addresses that can be learned in the VLAN.

The **undo mac-address limit** command deletes a MAC address learning limit rule applied to a VLAN.



By default, no MAC address learning limit rule is configured for a VLAN.


Format
------

**undo mac-address limit**

**mac-address limit** { **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **maximum** *max* | Specifies the maximum number of MAC address entries that can be learned. | The value is an integer ranging from 0 to 130048.  When the value is 0, the number of MAC addresses that can be learned is not set. |
| **action** | Specifies an action to be taken when the number of MAC address entries in the MAC address table reaches the limit. | - |
| **discard** | The packet with the source MAC address not contained in the MAC address table is discarded. | - |
| **forward** | The packet with the source MAC address not contained in the MAC address table is forwarded but its MAC address is not recorded. | - |
| **alarm** | Specifies whether an alarm is generated when the number of the MAC address entries in the MAC address table reaches the limit. | - |
| **enable** | Indicates that the system generates an alarm when the number of MAC address entries reaches the limit. | - |
| **disable** | Indicates that the system does not send an alarm when the number of MAC address entries reaches the limit. | - |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To control the number of users and protect a MAC address table against attacks, you can limit the number of MAC addresses that a device can learn. You can also configure the system to discard packets to improve network security.Configuring a VLAN-based MAC address learning limit rule can control the number of users in a VLAN. When the number of learned MAC addresses in the VLAN reaches the limit, no new MAC addresses will be learned. You can also configure the system to discard packets or generate an alarm to improve network security.

**Precautions**



Before configuring a MAC address learning limit rule, run the **reset mac-address** command to clear the learned MAC addresses to ensure that the number of MAC addresses that can be learned is limited accurately.Trustworthy MAC addresses may not be recorded after the number of learned MAC addresses reaches the limit. If an enterprise or a family is attacked by different source MAC addresses, only the network of the enterprise or family, not the whole network is affected.




Example
-------

# Configure a MAC address learning limit rule in VLAN 2: a maximum of 1000 MAC addresses can be learned, when the number of learned MAC addresses reaches the limit, the packet with the destination MAC address not contained in the MAC address table is forwarded.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] mac-address limit action forward alarm enable maximum 1000

```
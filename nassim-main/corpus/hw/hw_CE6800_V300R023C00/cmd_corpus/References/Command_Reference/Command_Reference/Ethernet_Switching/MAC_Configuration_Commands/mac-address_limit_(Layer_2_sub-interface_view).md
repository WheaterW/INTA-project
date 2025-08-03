mac-address limit (Layer 2 sub-interface view)
==============================================

mac-address limit (Layer 2 sub-interface view)

Function
--------



The **mac-address limit** command configures a MAC address learning limit rule for a sub-interface to set the maximum number of MAC addresses that can be learned in the sub-interface.

The **undo mac-address limit** command deletes a MAC address learning limit rule applied to a sub-interface.



By default, no MAC address learning limit rule is configured for a sub-interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address limit** { **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } } \*

**undo mac-address limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **maximum** *max* | Specifies the maximum number of MAC address entries that can be learned. | The value is an integer ranging from 0 to 32767.  When the value is 0, the number of MAC addresses that can be learned is not set. |
| **action** | Specifies an action to be taken when the number of MAC address entries in the MAC address table reaches the limit. | - |
| **discard** | The packet with the source MAC address not contained in the MAC address table is discarded. | - |
| **forward** | The packet with the source MAC address not contained in the MAC address table is forwarded but its MAC address is not recorded. | - |
| **alarm** | Specifies whether an alarm is generated when the number of the MAC address entries in the MAC address table reaches the limit. | - |
| **enable** | Indicates that the system generates an alarm when the number of MAC address entries reaches the limit. | - |
| **disable** | Indicates that the system does not send an alarm when the number of MAC address entries reaches the limit. | - |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To control the number of users and protect a MAC address table against attacks, you can limit the number of MAC addresses that a device can learn. You can also configure the system to discard packets or generate an alarm to improve network security.Configuring interface-based MAC address learning limit rule can control the number of access users on an interface. When the number of MAC addresses reaches the limit, no new MAC addresses will be learned. You can also configure the system to discard packets or generate an alarm to improve network security.

**Precautions**



Before configuring a MAC address learning limit rule, run the **reset mac-address** command to clear the learned MAC addresses to ensure that the number of MAC addresses that can be learned is limited accurately.Trustworthy MAC addresses may not be recorded after the number of learned MAC addresses reaches the limit. If an enterprise or a family is attacked by different source MAC addresses, only the network of the enterprise or family, not the whole network is affected.




Example
-------

# Configure a MAC address learning limit rule in a subinterface: a maximum of 1000 MAC addresses can be learned, when the number of learned MAC addresses reaches the limit, the packet with the destination MAC address not contained in the MAC address table is forwarded.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1
[*HUAWEI-100GE1/0/1.1] mac-address limit action forward alarm enable maximum 1000

```
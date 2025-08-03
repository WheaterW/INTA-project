mac-address limit (Layer 2 interface view)
==========================================

mac-address limit (Layer 2 interface view)

Function
--------



The **mac-address limit** command configures a MAC address learning limit rule on an interface to set the maximum number of MAC addresses that can be learned on the interface.

The **undo mac-address limit** command deletes a MAC address learning limit rule applied on an interface.



By default, no MAC address learning limit rule is configured for a VLAN.


Format
------

**mac-address limit** { **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } } \*

**undo mac-address limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **maximum** *max* | Specifies the maximum number of MAC address entries that can be learned. | The value is an integer ranging from 0 to 131072.  When the value is 0, the number of MAC addresses that can be learned is not set. |
| **action** | Specifies an action to be taken when the number of MAC address entries in the MAC address table reaches the limit. | - |
| **discard** | The packet with the source MAC address not contained in the MAC address table is discarded. | - |
| **forward** | The packet with the source MAC address not contained in the MAC address table is forwarded but its MAC address is not recorded. | - |
| **alarm** | Indicates whether an alarm is generated when the number of learned MAC addresses reaches the upper limit. | - |
| **disable** | Indicates that no alarm is generated when the number of learned MAC addresses reaches the upper limit. | - |
| **enable** | Indicates that an alarm is generated when the number of learned MAC addresses reaches the upper limit. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


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

# Configure a MAC address learning limit rule in an interface: a maximum of 1000 MAC addresses can be learned, when the number of learned MAC addresses reaches the limit, the packet with the destination MAC address not contained in the MAC address table is forwarded.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] mac-address limit action forward alarm enable maximum 1000

```
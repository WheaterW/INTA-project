peer mac-address limit
======================

peer mac-address limit

Function
--------



The **peer mac-address limit** command configures a MAC address learning limit rule to control the maximum number of MAC addresses that can be learned from a remote VTEP of a static VXLAN tunnel.

The **undo peer mac-address limit** command cancels the configuration.



By default, no MAC address learning limit rule is configured for a remote VTEP of a static VXLAN tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ip-address* **mac-address** **limit** { **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } } \*

**source** *sourceIP* **peer** *ip-address* **mac-address** **limit** { **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } } \*

**undo peer** *ip-address* **mac-address** **limit** [ **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } ] \*

**undo source** *sourceIP* **peer** *ip-address* **mac-address** **limit** [ **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } ] \*

**undo peer** *ip-address* **mac-address** **limit** **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a remote VTEP. | The value is in dotted decimal notation. |
| **maximum** *max* | Specifies the maximum number of MAC address entries that can be learned. | The value is an integer ranging from 1 to 32767. |
| **action** | Specifies an action to be taken when the number of MAC address entries in the MAC address table reaches the limit. | - |
| **discard** | Indicates that the packet with the source MAC address not contained in the MAC address table is discarded. | - |
| **forward** | The packet with the source MAC address not contained in the MAC address table is forwarded but its MAC address is not recorded. | - |
| **alarm** | Specifies whether an alarm is generated when the number of the MAC address entries in the MAC address table reaches the limit. | - |
| **enable** | Indicates that the system generates an alarm when the number of MAC address entries reaches the limit. | - |
| **disable** | Indicates that the system does not send an alarm when the number of MAC address entries reaches the limit. | - |
| **source** *sourceIP* | Specifies the source IP address. | The value is in dotted decimal notation. |
| **all** | Indicates the limit on all MAC addresses. | - |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A MAC address table has limited capacity. When the number of dynamically learned and stored MAC addresses reaches the upper limit of the MAC address table, a device fails to learn source MAC addresses from subsequent incoming packets. Attackers may use this vulnerability of the MAC address table to attack a device.To protect the device against such attacks and control the access user quantity, run the peer mac-address limit command to limit the maximum number of MAC addresses that can be learned from a specified remote VTEP of a static VXLAN tunnel. When the maximum number of MAC addresses learned from the specified remote VTEP is reached, the device can discard subsequent packets and report an alarm as configured.

**Prerequisites**

The **vni head-end peer-list** command has been run in the NVE interface view to set an IP address for the target remote VTEP of a static VXLAN tunnel.The **reset mac-address** command has been run to clear existing MAC address entries, if present. If the existing MAC address entries are not cleared, MAC addresses that have been learned before the peer mac-address limit command is run are also counted into the current number of learned MAC addresses. As a result, the configured MAC address learning limit rule fails to function as expected.

**Configuration Impact**

After the peer mac-address limit command is run, the device cannot identify trusted MAC addresses. If a malicious user attacks an enterprise or a home user by changing MAC addresses, only the enterprise or home network is affected, but other networks are not.

**Precautions**



After the **vtep-src ip-address** command is run (namely, when the source VTEP address of a VXLAN tunnel is configured in a BD instance), run the source peer mac-address limit { maximum | action { discard | forward } | alarm { enable | disable } } command to configure the maximum number of MAC addresses that can be learned from a remote VTEP.




Example
-------

# Allow NVE1 to learn a maximum of 1000 MAC addresses from the remote VTEP 2.2.2.2.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] vni 1 head-end peer-list 2.2.2.2
[*HUAWEI-Nve1] peer 2.2.2.2 mac-address limit maximum 1000

```
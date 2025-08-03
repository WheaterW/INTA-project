mac-address limit
=================

mac-address limit

Function
--------



The **mac-address limit** command sets a MAC address learning limit rule, including the maximum number of MAC addresses that a device can learn.

The **undo mac-address limit** command deletes MAC address learning limit rules.



By default, a device can learn MAC addresses without limit.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address limit** { **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } } \*

**undo mac-address limit** [ **maximum** *max* | **action** { **discard** | **forward** } | **alarm** { **enable** | **disable** } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **maximum** *max* | Specifies the maximum number of MAC address entries that can be learned. | The value is an integer ranging from 0 to 130048.  When the value is 0, the number of MAC addresses that can be learned is not set. |
| **action** | Specifies an action to be taken when the number of MAC address entries in the MAC address table reaches the limit. | - |
| **discard** | The packet with the source MAC address not contained in the MAC address table is discarded. | - |
| **forward** | The packet with the source MAC address not contained in the MAC address table is forwarded but its MAC address is not recorded. | - |
| **alarm** | Indicates whether an alarm is generated when the number of learned MAC addresses reaches the upper limit. | - |
| **enable** | Indicates that an alarm is generated when the number of learned MAC addresses reaches the upper limit. | - |
| **disable** | Indicates that no alarm is generated when the number of learned MAC addresses reaches the upper limit. | - |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On insecure networks, devices are prone to attacks using forged MAC addresses. The capacity of a MAC address table on a device is limited. A hacker can forge a great number of source MAC addresses to a device. Upon receipt, the device adds the MAC addresses to the dynamic MAC address table, resulting in a dynamic MAC address table overflow. As a result, the device cannot learn more source MAC addresses carried in valid packets.To set a MAC address learning limit rule, run the **mac-address limit** command. This command helps control the number of access users. If the number of learned MAC addresses reaches the upper limit, the device can be configured to discard packets carrying new MAC addresses, which prevents MAC address attacks and improves network security.

**Prerequisites**

If a device has learned some MAC addresses, run the **reset mac-address bridge-domain bd-id** command to delete them.

**Configuration Impact**

The device with the MAC address learning limit configured cannot verify MAC addresses. If an attack to an enterprise or home is initiated by changing MAC addresses, the attack affects transmission of the enterprise or home network, not the entire network.


Example
-------

# Configure a maximum of 1000 MAC addresses that a device can learn in a BD. After the number of learned MAC addresses reaches the limit, the packets with new MAC addresses are still forwarded, and an alarm is generated.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] mac-address limit action forward maximum 1000 alarm enable

```
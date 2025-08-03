arp resource-mode
=================

arp resource-mode

Function
--------



The **arp resource-mode** command sets the ARP resource allocation mode.



By default, the global ARP resource allocation mode is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**arp resource-mode** { **global** | **extend** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Sets the global ARP resource allocation mode. | - |
| **extend** | Sets the extended ARP resource allocation mode. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ARP resource allocation modes are classified into the following types:

* Global allocation mode (global mode)In global mode, ARP information is identified based on a key composed of the IP address and logical interface index. ARP information is stored on all chips based on the same resource index, meaning that ARP information stored on each chip is the same.In this mode, the maximum number of ARP resources supported by the device refers to that of the chip with minimum specifications among all chips.
* Extended allocation mode (extend mode)In extend mode, ARP information is identified based on a key composed of 43 most significant bits of a MAC address. ARP information is stored on all chips based on the same resource index, meaning that ARP information stored on each chip is the same. The extend mode differs from the global mode in that ARP information corresponding to contiguous MAC addresses is aggregated in extend mode. This means that ARP information with the same 43 most significant bits of a MAC address corresponds to the same ARP resource.In this mode, the maximum number of ARP resources supported by the device depends on whether the MAC addresses corresponding to ARP information are contiguous.
* If the MAC addresses corresponding to all ARP information are not contiguous, the maximum number of ARP resources supported by the device refers to that of the chip with minimum specifications among all chips.
* If the MAC addresses corresponding to all ARP information are contiguous, the maximum number of ARP resources supported by the device refers to that of the chip with minimum specifications among all chips multiplied by 32.

**Follow-up Procedure**

After running the **arp resource-mode** command to configure the ARP resource allocation mode, run the **save** command to save the configuration and run the **reboot** command to restart the device to make the configuration take effect. Otherwise, packet forwarding may be abnormal.


Example
-------

# Set the ARP resource allocation mode to extend.
```
<HUAWEI> system-view
[~HUAWEI] arp resource-mode extend

```
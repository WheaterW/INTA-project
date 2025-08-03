vrrp compatible-version
=======================

vrrp compatible-version

Function
--------



The **vrrp compatible-version** command configures a VRRPv3-enabled device to send Advertisement packets of a specified version in the system view.

The **undo vrrp compatible-version** command restores the default configuration in the system view.



By default, a VRRPv3-enabled device sends only VRRPv3 Advertisement packets.


Format
------

**vrrp compatible-version** { **2** | **3** | **all** }

**undo vrrp compatible-version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **2** | Indicates that a VRRPv3-enabled device sends only VRRPv2 Advertisement packets. | - |
| **3** | Indicates that a VRRPv3-enabled device sends only VRRPv3 Advertisement packets. | - |
| **all** | Indicates that a VRRPv3-enabled device sends both VRRPv2 and VRRPv3 Advertisement packets. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If different VRRP versions are configured for devices in a VRRP backup group, a VRRPv2-enabled device receives only VRRPv2 Advertisement packets. After the VRRPv2-enabled device receives VRRPv3 Advertisement packets, it discards them. As a result, the devices in the VRRP backup group cannot negotiate their status. To resolve this issue, run the vrrp version-3 send-packet-mode command to configure a VRRPv3-enabled device to send VRRPv2 Advertisement packets so that the VRRPv2- and VRRPv3-enabled devices can negotiate their status.

**Prerequisites**

The VRRP version number of a device has been configured as 3 using this command.

**Configuration Impact**

If both the vrrp version-3 send-packet-mode and **vrrp vrid compatible-version** commands are run, the vrrp vrid version-3 send-packet-mode command takes precedence over the vrrp version-3 send-packet-mode command.

**Precautions**

Only a VRRPv3-enabled device can be configured to send Advertisement packets of a specified version.


Example
-------

# Configure a VRRPv3-enabled device to send only VRRPv2 Advertisement packets.
```
<HUAWEI> system-view
[~HUAWEI] vrrp version 3
[*HUAWEI] vrrp compatible-version 2

```
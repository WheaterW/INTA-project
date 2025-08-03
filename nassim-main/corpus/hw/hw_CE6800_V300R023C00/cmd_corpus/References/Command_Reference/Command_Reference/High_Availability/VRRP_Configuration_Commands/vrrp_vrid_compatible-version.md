vrrp vrid compatible-version
============================

vrrp vrid compatible-version

Function
--------



The **vrrp vrid compatible-version** command configures a VRRPv3-enabled device to send Advertisement packets of a specified version in the system view.

The **undo vrrp vrid compatible-version** command restores the default configuration in the system view.



By default, the mode in which VRRPv3 sends Advertisement packets is the same as that configured in the system view.


Format
------

**vrrp vrid** *vrid-value* **compatible-version** { **2** | **3** | **all** }

**undo vrrp vrid** *vrid-value* **compatible-version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vrid-value* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **2** | Indicates that a VRRPv3-enabled device sends only VRRPv2 Advertisement packets. | - |
| **3** | Indicates that a VRRPv3-enabled device sends only VRRPv3 Advertisement packets. | - |
| **all** | Indicates that a VRRPv3-enabled device sends both VRRPv2 and VRRPv3 Advertisement packets. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If devices in a VRRP group use different VRRP versions, the VRRP group may fail to negotiate the status. This is because a VRRPv2-enabled device can only receive VRRPv2 Advertisement packets and discards the received VRRPv3 Advertisement packets. To resolve this issue, run the **vrrp vrid compatible-version** command to configure a VRRPv3-enabled device to send VRRPv2 Advertisement packets so that the VRRPv2- and VRRPv3-enabled devices can negotiate their status.

**Prerequisites**

* A VRRP group has been created using the **vrrp vrid virtual-ip** command.
* The VRRP version number of a device has been configured as 3 using the **vrrp version 3** command.

**Precautions**

Only a VRRPv3-enabled device can be configured to send Advertisement packets of a specified version.


Example
-------

# Configure a VRRPv3-enabled device to send only VRRPv2 Advertisement packets in the view of 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] vrrp version 3
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
[*HUAWEI-100GE1/0/1] vrrp vrid 1 compatible-version 2

```
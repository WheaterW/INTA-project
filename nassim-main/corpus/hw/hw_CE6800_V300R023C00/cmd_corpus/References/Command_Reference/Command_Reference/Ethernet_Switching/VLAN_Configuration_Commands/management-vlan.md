management-vlan
===============

management-vlan

Function
--------



The **management-vlan** command configures a management VLAN.

The **undo management-vlan** command deletes a management VLAN.



By default, no management VLAN is configured.


Format
------

**management-vlan**

**undo management-vlan**


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



To use a remote network management system (NMS) to manage devices in a centralized manner, configure a VLANIF interface on each device and use the interface IP address as the management IP address of the device. If a user connected to another interface of the device is added to the VLAN, the user can also access the switching device. This increases security risks on the switching device.After a VLAN is configured as a management VLAN, no access or dot1q-tunnel interface can be added to the VLAN. The access and dot1q-tunnel interfaces are usually used to connect users. If the access and dot1q-tunnel interfaces are not added to the management VLAN, users connected to the access and dot1q-tunnel interfaces cannot access the device. This improves the security of the switching device.



**Configuration Impact**



After a VLAN is configured as the management VLAN, trunk and hybrid interfaces can be added to the VLAN.



**Follow-up Procedure**



Configure a VLANIF interface for the management VLAN and IP address for the VLANIF interface.



**Precautions**



After you run the **display vlan** command to view management VLAN configurations, the VLAN with an asterisk (\*) is the management VLAN.




Example
-------

# Configure VLAN 100 as the management VLAN.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] management-vlan

```
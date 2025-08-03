authorization-info check-fail policy
====================================

authorization-info check-fail policy

Function
--------



The **authorization-info check-fail policy** command determines whether the device allows users to go online after the authorization information check fails.

The **undo authorization-info check-fail policy** command restores the default configuration.



By default, the device allows users to go online after the authorization information check fails.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authorization-info check-fail policy** { **offline** | **online** }

**undo authorization-info check-fail policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **offline** | Indicates that the device prohibits users from going online after the authorization information check fails. | - |
| **online** | Indicates that the device allows users to go online after the authorization information check fails. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The device supports dynamic user authorization through the ACL, UCL group, user group, VLAN, and service scheme delivered from the RADIUS server. The UCL group can be identified by UCL group name or UCL group ID. The ACL, UCL group name and user group are delivered with the Filter-Id attribute of packets sent from the RADIUS server. The VLAN is delivered with the Tunnel-Type, Tunnel-Medium-Type, or Tunnel-Private-Group-ID attribute of packets sent from the RADIUS server. The UCL group ID is delivered with the HW-UCL-Group attribute of packets sent from the RADIUS server, and the name of the service scheme is delivered with the HW-User-Policy attribute of packets sent from the RADIUS server. If the ACL, UCL group, user group, VLAN, or service scheme corresponding to the dynamic authorization information is not configured on the device, the device fails to check authorization information.If you want users to go online even if authorization fails, run the **authorization-info check-fail policy** command to allow the users to go online. In this case, authorization information delivered by the RADIUS server does not take effect.




Example
-------

# Configure the device to allow users to go online after the authorization information check fails.
```
<HUAWEI> system-view
[~HUAWEI] authorization-info check-fail policy online

```
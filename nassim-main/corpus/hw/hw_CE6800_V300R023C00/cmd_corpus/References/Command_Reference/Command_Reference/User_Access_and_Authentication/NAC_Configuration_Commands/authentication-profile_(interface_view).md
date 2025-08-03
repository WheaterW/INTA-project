authentication-profile (interface view)
=======================================

authentication-profile (interface view)

Function
--------



The **authentication-profile** command applies an authentication profile to an interface.

The **undo authentication-profile** command restores the default setting.



By default, no authentication profile is applied to the interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication-profile** *authentication-profile-name*

**undo authentication-profile**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *authentication-profile-name* | Specifies the name of an authentication profile. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The value must be an existing authentication profile name. |



Views
-----

100GE interface view,10GE interface view,25GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An authentication profile uniformly manages NAC configuration. The authentication profile is bound to the interface view to enable NAC, implementing access control over users on the interface. The authentication type of the users on the interface is determined by the access profile bound to the authentication profile.

**Prerequisites**

An authentication profile has been created using the **authentication-profile** command in the system view.

**Precautions**

NAC support on different interfaces is as follows:

* 802.1X authentication is supported on Layer 2 interfaces and Eth-Trunk interfaces.
* In NETCONF mode, the VLAN through which a user goes online cannot be changed when the user is online.
* After NAC is enabled on a physical interface, Layer 2 sub-interfaces cannot be configured on the physical interface, and vice versa.
* After NAC is enabled on an interface, the following commands cannot be run on the interface, and vice versa.
  + mac-address limit: sets the maximum number of MAC addresses that can be learned by the interface.
  + mac-address learning disable: disables MAC address learning on the interface.
  + mac-vlan enable: enables MAC address-based VLAN assignment on the interface.
  + ip-subnet-vlan enable: enables IP subnet-based VLAN assignment on the interface.
  + dfs-group in the system view: enables the DFS group function in the system view.


Example
-------

# Apply the authentication profile m1 to an interface.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name m1
[*HUAWEI-authen-profile-m1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] authentication-profile m1

```
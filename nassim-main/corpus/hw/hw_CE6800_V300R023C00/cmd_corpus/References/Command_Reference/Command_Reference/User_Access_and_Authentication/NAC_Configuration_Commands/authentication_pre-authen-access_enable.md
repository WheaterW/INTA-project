authentication pre-authen-access enable
=======================================

authentication pre-authen-access enable

Function
--------



The **authentication pre-authen-access enable** command enables the pre-connection function.

The **undo authentication pre-authen-access enable** command disables the pre-connection function.



By default, the pre-connection function is enabled. That is, if a user does not have any network access rights before being authenticated, the user is in the pre-connection state.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication pre-authen-access enable**

**undo authentication pre-authen-access enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* When a user terminal is connected to an NAC-enabled interface on the device, a pre-connection is established between the terminal and device. If the user fails the authentication, the device still sets the user to the pre-connection state by default. Because the device permits DHCP packets from pre-connection users, the users can still obtain IP addresses although they do not have any network access rights. This wastes IP addresses and brings network security risks.
* To prevent users from having certain network access rights before they are authenticated successfully, disable the pre-connection function. After the pre-connection function is disabled, users do not have network access rights before they are authenticated successfully and cannot obtain IP addresses.
* In pre-connection authorization scenarios, including authentication-free rules and pre-connection authorization, broadcast packets, multicast data packets and protocol packets such as ARP, ND, DHCP, and DHCPv6 packets are allowed to pass through.In pre-connection scenarios without authorization, IP addresses cannot be obtained through DHCP by default.
* In policy association scenarios, protocol packets such as ARP, ND, DHCP, and DHCPv6 packets are allowed to pass through by default.

**Precautions**

* The **undo authentication pre-authen-access enable** command does not take effect for users who have pre-connection authorization configured.
* If the device is connected to some terminals such as a MacBook laptop that is not authenticated after obtaining an IP address, it is recommended that you run the **undo authentication pre-authen-access enable** command on the device to disable the pre-connection function and then connect the terminal to the network again.
* If a user in pre-connection state fails to go online using DHCP packets containing Option 82, it is recommended that you run the **undo authentication pre-authen-access enable** command to disable the pre-connection function on the device.

Example
-------

# Disable the pre-connection function.
```
<HUAWEI> system-view
[~HUAWEI] undo authentication pre-authen-access enable

```
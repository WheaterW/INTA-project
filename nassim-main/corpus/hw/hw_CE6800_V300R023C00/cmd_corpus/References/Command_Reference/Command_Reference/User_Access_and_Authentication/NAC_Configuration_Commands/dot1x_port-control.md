dot1x port-control
==================

dot1x port-control

Function
--------



The **dot1x port-control** command sets the authorization state of an interface.

The **undo dot1x port-control** command restores the default authorization state of an interface.



By default, the authorization state of an interface is auto.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x port-control** { **auto** | **authorized-force** | **unauthorized-force** }

**undo dot1x port-control**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **auto** | Indicates the auto identification mode. In this mode, an interface is initially in Unauthorized state and only allows users to send and receive EAPOL packets. Users cannot access network resources. After the users are authenticated, the interface becomes authorized and allows the users to access network resources. | - |
| **authorized-force** | Indicates the forcible authorization mode. In this mode, the interface is always in Authorized state and allows users to access network resources without authentication and authorization. | - |
| **unauthorized-force** | Indicates the forcible unauthorized mode. In this mode, the interface is always in Unauthorized state and forbids users to access network resources. | - |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In most cases, configuring the port control method as auto is recommended. After that, a user can access network resources only after being authenticated. To allow all users on an interface to access network resources, run the dot1x port-control authorized-force command. To disable all users on an interface from accessing network resources, run the dot1x port-control unauthorized-force command.

**Precautions**

If 802.1X users on an interface have gone online, changing the authorization state in the 802.1X access profile bound to the interface will make the online 802.1X users go offline.It is recommended that you set the authorization state of an interface in the early stage of network deployment. When the network is running properly, run the **cut access-user** command to disconnect all users from the interface before changing the authorization state.


Example
-------

# Configure the authorization state of an interface as unauthorized-force in 802.1X access profile d1.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] dot1x port-control unauthorized-force
Warning: Changing the configuration will cause online users to go offline. Continue? [Y/N]:y

```
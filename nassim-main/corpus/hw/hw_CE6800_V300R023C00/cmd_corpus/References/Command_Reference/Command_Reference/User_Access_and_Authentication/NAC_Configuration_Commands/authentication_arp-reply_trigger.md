authentication arp-reply trigger
================================

authentication arp-reply trigger

Function
--------



The **authentication arp-reply trigger** command enables the function of triggering authentication by ARP response packets.

The **undo authentication arp-reply trigger** command disables the function of triggering authentication by ARP response packets.



By default, the function of triggering authentication by ARP response packets is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication arp-reply trigger**

**undo authentication arp-reply trigger**


Parameters
----------

None

Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a client in sleep mode receives an ARP request packet, it replies with an ARP response packet, which triggers authentication. However, the authentication fails because no user name or password is entered when the client is in sleep mode. If the client is awakened before the re-authentication interval (specified by the **authentication timer re-authen authen-fail re-authen-time** command) expires, the user has to wait for a period of time before triggering authentication again. In this case, you can disable the function of triggering authentication by ARP response packets so that authentication is not triggered by ARP response packets sent by clients in sleep mode.

**Precautions**

The function of triggering authentication by ARP response packets takes precedence over the function of triggering authentication by any packets. When the function of triggering authentication by ARP response packets is disabled and the function of triggering authentication by any packets is enabled, authentication cannot be triggered by ARP response packets.


Example
-------

# Enable the function of triggering authentication by ARP response packets.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name test
[*HUAWEI-authen-profile-test] authentication arp-reply trigger

```
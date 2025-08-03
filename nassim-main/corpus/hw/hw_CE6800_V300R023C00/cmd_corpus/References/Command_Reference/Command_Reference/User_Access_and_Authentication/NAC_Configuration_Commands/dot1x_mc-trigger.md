dot1x mc-trigger
================

dot1x mc-trigger

Function
--------



The **dot1x mc-trigger** enables multicast-triggered 802.1X authentication.

The **undo dot1x mc-trigger** disables multicast-triggered 802.1X authentication.



By default, multicast-triggered 802.1X authentication is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x mc-trigger**

**undo dot1x mc-trigger**


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

If a client (for example, the built-in 802.1X client of the Windows operating system) cannot send an EAPOL-Start packet to perform 802.1X authentication, you can enable multicast-triggered 802.1X authentication. After that, the device multicasts an Identity EAP-Request frame to the client to trigger authentication.


Example
-------

# Enable multicast-triggered 802.1X authentication.
```
<HUAWEI> system-view
[~HUAWEI] dot1x mc-trigger

```
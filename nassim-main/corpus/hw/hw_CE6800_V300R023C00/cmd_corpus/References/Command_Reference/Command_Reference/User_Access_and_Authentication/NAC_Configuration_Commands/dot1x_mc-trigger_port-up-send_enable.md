dot1x mc-trigger port-up-send enable
====================================

dot1x mc-trigger port-up-send enable

Function
--------



The **dot1x mc-trigger port-up-send enable** command enables the function of triggering 802.1X authentication through multicast packets immediately after an interface goes Up.

The **undo dot1x mc-trigger port-up-send enable** command disables the function of triggering 802.1X authentication through multicast packets immediately after an interface goes Up.



By default, the function of triggering 802.1X authentication through multicast packets immediately after an interface goes Up is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x mc-trigger port-up-send enable**

**undo dot1x mc-trigger port-up-send enable**


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

By default, the device periodically multicasts EAP-Request/Identity packets to clients so that the clients are triggered to send EAPOL-Start packets for 802.1X authentication. If the device interface connecting to a client changes from Down to Up, the client needs to send EAPOL-Start packets again for 802.1X authentication, which takes a long time. You can run the **dot1x mc-trigger port-up-send enable** command on the device to enable the device interface to multicast EAP-Request/Identity packets to the client to trigger 802.1X authentication immediately after the interface goes Up. This configuration shortens the re-authentication time.


Example
-------

# Enable the function of triggering 802.1X authentication through multicast packets immediately after an interface goes Up.
```
<HUAWEI> system-view
[~HUAWEI] dot1x mc-trigger port-up-send enable

```
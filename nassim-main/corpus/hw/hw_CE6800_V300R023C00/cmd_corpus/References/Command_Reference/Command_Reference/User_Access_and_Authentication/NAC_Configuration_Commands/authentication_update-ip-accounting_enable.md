authentication update-ip-accounting enable
==========================================

authentication update-ip-accounting enable

Function
--------



The **authentication update-ip-accounting enable** command enables a device to send accounting packets for terminal address updating.

The **undo authentication update-ip-accounting enable** command disables a device from sending accounting packets for terminal address updating.



By default, the device is enabled to send accounting packets for terminal address updating.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication update-ip-accounting enable**

**undo authentication update-ip-accounting enable**


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

By default, the device immediately sends accounting packets to the accounting server when users' terminal addresses are updated. Some accounting servers may not require the accounting packets. In this case, a large number of accounting packets occupy device resources. You can run the **undo authentication update-ip-accounting enable** command to disable the device from sending accounting packets to the accounting server upon terminal address update, reducing resource consumption. After the terminal address is updated, the device sends accounting packets again and the accounting function is not affected.For the command:

* update-ip-accounting: indicates that accounting packets are immediately sent upon terminal address update.
* After the **undo authentication update-ip-accounting enable** command is run, the device does not send accounting packets immediately after obtaining the updated terminal address. Instead, the device sends the packets after the real-time accounting timer expires.

Example
-------

# Disable a device from sending accounting packets for address updating.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name test
[*HUAWEI-authen-profile-test] undo authentication update-ip-accounting enable

```
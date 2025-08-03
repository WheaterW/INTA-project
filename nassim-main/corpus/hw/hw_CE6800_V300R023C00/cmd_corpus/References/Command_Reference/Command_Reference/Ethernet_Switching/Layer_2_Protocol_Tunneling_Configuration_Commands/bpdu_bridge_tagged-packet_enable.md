bpdu bridge tagged-packet enable
================================

bpdu bridge tagged-packet enable

Function
--------



The **bpdu bridge tagged-packet enable** command enables an interface to transparently transmit tagged BPDUs.

The **undo bpdu bridge tagged-packet enable** command disables the transparent transmission of tagged BPDUs.



By default, transparent transmission of tagged BPDUs is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**bpdu bridge tagged-packet enable**

**undo bpdu bridge tagged-packet enable**


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

The function of transparently transmitting tagged BPDUs is configured globally and has a higher priority than the ACL delivered by each protocol. This ensures that tagged BPDUs can be transparently transmitted when LACP, LLDP, and other protocols are enabled.


Example
-------

# Configure the device to forward BPDUs carrying VLAN tags through the hardware.
```
<HUAWEI> system-view
[~HUAWEI] bpdu bridge tagged-packet enable

```
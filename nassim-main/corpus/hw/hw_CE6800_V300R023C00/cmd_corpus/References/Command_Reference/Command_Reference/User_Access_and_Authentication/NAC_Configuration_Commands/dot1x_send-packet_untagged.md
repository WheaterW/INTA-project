dot1x send-packet untagged
==========================

dot1x send-packet untagged

Function
--------



The **dot1x send-packet untagged** command enables an access device to remove VLAN tags from 802.1X packets to be sent to terminals.

The **undo dot1x send-packet untagged** command disables an access device from removing VLAN tags from 802.1X packets to be sent to terminals.



By default, access devices do not remove VLAN tags from 802.1X packets to be sent to terminals.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x send-packet untagged**

**undo dot1x send-packet untagged**


Parameters
----------

None

Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Some terminals (mainly some models of IP phones) cannot identify the tagged 802.1X packets received from access devices, resulting in 802.1X authentication failures. To resolve this problem, you can run the dot1x send-packet untagged command to enable access devices to remove VLAN tags from 802.1X packets to be sent to terminals.


Example
-------

# In the 802.1X access profile d1, enable the access device to remove VLAN tags from 802.1X packets to be sent to terminals.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] dot1x send-packet untagged

```
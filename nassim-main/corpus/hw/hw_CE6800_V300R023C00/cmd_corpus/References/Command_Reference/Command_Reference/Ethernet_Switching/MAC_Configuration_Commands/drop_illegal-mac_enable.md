drop illegal-mac enable
=======================

drop illegal-mac enable

Function
--------



The **drop illegal-mac enable** command enables a device to drop packets with an invalid MAC address (all zeros).

The **undo drop illegal-mac enable** command disables a device from dropping packets with an invalid MAC address (all zeros).



By default, a device is disabled from dropping packets with an invalid MAC address (all zeros).


Format
------

**drop illegal-mac enable**

**undo drop illegal-mac enable**


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

Hosts of early versions may send packets with an invalid source or destination MAC address (all zeros) if network adapters on a device become faulty. You can run the **drop illegal-mac enable** command to enable the device to discard such packets.

**Configuration Impact**

This function reduces incorrect MAC entries on a device.


Example
-------

# Enable a device to drop packets with an invalid MAC address (all zeros).
```
<HUAWEI> system-view
[~HUAWEI] drop illegal-mac enable

```
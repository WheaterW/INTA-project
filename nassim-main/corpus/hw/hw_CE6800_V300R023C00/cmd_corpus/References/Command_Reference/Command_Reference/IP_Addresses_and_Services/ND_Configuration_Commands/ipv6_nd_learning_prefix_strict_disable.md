ipv6 nd learning prefix strict disable
======================================

ipv6 nd learning prefix strict disable

Function
--------



The **ipv6 nd learning prefix strict disable** command disables the strict prefix learning function for dynamic neighbor entries.

The **undo ipv6 nd learning prefix strict disable** command restores the default configuration.



By default, the strict prefix learning function for dynamic neighbor entries is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd learning prefix strict disable**

**undo ipv6 nd learning prefix strict disable**


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

When a device receives a valid NS message on an interface, the device checks whether IPv6 addresses with the same network prefix exist on the interface. If so, the device replies with an NA message and generates dynamic neighbor entries. If not, the device performs the following operations:

* If the strict prefix learning function for dynamic neighbor entries is enabled on the interface, the device simply discards the NS message and does not generate dynamic neighbor entries.
* If the strict prefix learning function for dynamic neighbor entries is disabled on the interface, the device replies with an NA message and generates dynamic neighbor entries.

**Precautions**

* Strict prefix learning cannot be disabled for dynamic ND entries on interfaces that need to generate host routes. The configuration in the system view does not take effect on such interfaces.
* After strict prefix learning is enabled for dynamic ND entries, the device does not delete the learned dynamic ND entries corresponding to different address prefixes. Instead, the device waits for the entries to age automatically.
* For strict prefix learning of dynamic ND entries, the configuration in the interface view takes precedence over that in the system view.

Example
-------

# Disable the strict prefix learning function for dynamic neighbor entries on all interfaces.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd learning prefix strict disable

```
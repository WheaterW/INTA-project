ipv6 nd learning prefix strict disable (interface view)
=======================================================

ipv6 nd learning prefix strict disable (interface view)

Function
--------



The **ipv6 nd learning prefix strict disable** command disables the strict prefix learning function for dynamic neighbor entries.

The **undo ipv6 nd learning prefix strict disable** command restores the default configuration.



By default, an interface is not enabled with the strict prefix learning function for dynamic neighbor entries. The interface behavior is consistent with the configuration in the system view.

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

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device receives a valid NS message on an interface, the device checks whether IPv6 addresses with the same network prefix exist on the interface. If so, the device replies with an NA message and generates dynamic neighbor entries. If not, the device performs the following operations:

* If the strict prefix learning function for dynamic neighbor entries is enabled on the interface, the device simply discards the NS message and does not generate dynamic neighbor entries.
* If the strict prefix learning function for dynamic neighbor entries is disabled on the interface, the device replies with an NA message and generates dynamic neighbor entries.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command.

**Precautions**

* After the strict prefix learning function is enabled for dynamic neighbor entries, the device does not delete the learned dynamic neighbor entries corresponding to different address prefixes. Instead, the device waits for the entries to automatically age out.
* The configuration of the strict prefix learning function for dynamic neighbor entries in the interface view has a higher priority than that in the system view.

Example
-------

# Disable the strict prefix learning function for dynamic neighbor entries on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd learning prefix strict disable

```
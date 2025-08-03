require-router-alert (MLD view)
===============================

require-router-alert (MLD view)

Function
--------



The **require-router-alert** command enables the device to discard the Multicast Listener Discovery (MLD) messages that do not contain Router-Alert options in IPv6 headers.

The **undo require-router-alert** command restores the default configuration.



By default, the device accepts and processes the MLD messages that do not contain Router-Alert options in IPv6 headers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**require-router-alert**

**undo require-router-alert**


Parameters
----------

None

Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as that of the mld require-router-alert command used in the interface view. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.


Example
-------

# Enable the device to discard the MLD messages that do not contain Router-Alert options in IPv6 headers.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] require-router-alert

```
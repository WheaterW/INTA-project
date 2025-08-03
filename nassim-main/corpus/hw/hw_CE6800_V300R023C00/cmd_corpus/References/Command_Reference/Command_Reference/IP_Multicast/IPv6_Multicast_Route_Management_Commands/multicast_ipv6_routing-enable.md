multicast ipv6 routing-enable
=============================

multicast ipv6 routing-enable

Function
--------



The **multicast ipv6 routing-enable** command enables IPv6 multicast.

The **undo multicast ipv6 routing-enable** command restores the default configuration.



By default, IPv6 multicast is not enabled. If IPv6 multicast is not enabled, the router cannot forward IPv6 multicast packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 routing-enable**

**undo multicast ipv6 routing-enable**


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

Other IPv6 multicast-related commands can be run only after the IPv6 multicast function is enabled.

**Precautions**

Running the **undo multicast ipv6 routing-enable** command will clear all IPv6 multicast configurations and terminate the running IPv6 multicast services. If you want to restore the IPv6 multicast services, re-configure multicast commands for which configurations have been deleted.For security purposes, after the **configuration re-authentication enable** command is configured, you need to enter the password and pass the authentication when running the **undo multicast ipv6 routing-enable** command to make the configuration take effect.


Example
-------

# Enable IPv6 multicast.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable

```
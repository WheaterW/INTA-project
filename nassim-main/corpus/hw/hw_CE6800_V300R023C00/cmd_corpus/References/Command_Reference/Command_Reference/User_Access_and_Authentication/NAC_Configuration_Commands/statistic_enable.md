statistic enable
================

statistic enable

Function
--------



The **statistic enable** command enables traffic statistics collection for domain users.

The **undo statistic enable** command disables traffic statistics collection for domain users.



By default, traffic statistics collection is disabled for domain users.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**statistic enable**

**undo statistic enable**


Parameters
----------

None

Views
-----

AAA domain view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To implement traffic-based accounting, you can use this command to enable traffic statistics collection for a domain. Then the device collects traffic statistics for the users in the domain. If an accounting server is configured, the device sends traffic statistics to the accounting server through accounting packets so that the server performs accounting for the IPv4 and IPv6 users based on traffic statistics.


Example
-------

# Enable traffic statistics collection for domain users.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain huawei
[*HUAWEI-aaa-domain-huawei] statistic enable

```
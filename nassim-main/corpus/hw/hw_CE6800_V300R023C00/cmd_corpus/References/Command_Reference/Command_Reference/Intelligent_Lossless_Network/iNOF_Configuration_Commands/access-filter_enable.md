access-filter enable
====================

access-filter enable

Function
--------



The **access-filter enable** command enables the iNOF host access interface whitelist function.

The **undo access-filter enable** command disables the iNOF host access interface whitelist function.



By default, the iNOF host access interface whitelist function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**access-filter enable**

**undo access-filter enable**


Parameters
----------

None

Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to enable the iNOF host access interface whitelist function. When this function is disabled, the whitelist does not take effect and host access to iNOF is not restricted.When the iNOF host access interface whitelist function is enabled, hosts access to iNOF is restricted based on the configured whitelist information.

* If a host and its access interface are configured in the whitelist, the host can access the iNOF only through the specified interface.
* If a host is not configured in the whitelist, the host cannot access the iNOF.

Example
-------

# Enable the iNOF host access interface whitelist function.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] access-filter enable

```
multicast-nat enable
====================

multicast-nat enable

Function
--------



The **multicast-nat enable** command enables multicast NAT globally.

The **undo multicast-nat enable** command disables multicast NAT globally and deletes all multicast NAT configurations.



By default, multicast NAT is disabled globally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat enable**

**undo multicast-nat enable**


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

Before translating an input multicast stream into output multicast streams with different characteristics (source IP address, destination IP address, and destination port number), you must run the multicast-nat enable command to enable multicast NAT globally.


Example
-------

# Enable multicast NAT globally.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable

```
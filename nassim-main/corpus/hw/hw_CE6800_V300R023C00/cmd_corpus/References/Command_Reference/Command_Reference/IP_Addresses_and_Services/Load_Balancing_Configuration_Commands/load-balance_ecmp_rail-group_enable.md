load-balance ecmp rail-group enable
===================================

load-balance ecmp rail-group enable

Function
--------



The **load-balance ecmp rail-group enable** command enables the rail group function.

The **undo load-balance ecmp rail-group enable** command disables the rail group function.



By default, the rail group function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**load-balance ecmp rail-group enable**

**undo load-balance ecmp rail-group enable**


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

You can run this command to enable the rail group function.

**Precautions**

* This command and the **load-balancing ucmp** commands are mutually exclusive and cannot be configured together.
* This command and the **load-balance ecmp stateful enable** command are mutually exclusive and cannot be configured together.
* This command and the **vxlan-overlay all local-preference enable** command are mutually exclusive and cannot be configured together.
* This command and the **vxlan-overlay network local-preference enable** command are mutually exclusive and cannot be configured together.
* For the CE8851-32CQ8DQ-P, CE8851K, CE8850-HAM, CE8850-SAN, CE8855, and CE8851-32CQ4BQ, this command and the **load-balancing adaptive-routing** command are mutually exclusive and cannot be configured together.
* For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode, this command and the ecmp underlay seed <under-seed-data> command are mutually exclusive and cannot be configured together.
* For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode, this command and the ecmp underlay universal-id <under-universal-id> command are mutually exclusive and cannot be configured together.


Example
-------

# Enable the rail group function.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp rail-group enable

```
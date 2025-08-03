statistics enable (Tunnel interface view)
=========================================

statistics enable (Tunnel interface view)

Function
--------



The **statistics enable** command enables traffic statistics collection on a GRE tunnel interface.

The **undo statistics enable** command disables traffic statistics collection on a GRE tunnel interface.



By default, traffic statistics collection is disabled on a GRE tunnel interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**statistics enable**

**undo statistics enable**


Parameters
----------

None

Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To monitor or charge the incoming and outgoing traffic of a GRE tunnel interface, run the **statistics enable** command to enable traffic statistics collection on the interface first.

**Follow-up Procedure**

Run the **display interface tunnel** command to check traffic statistics.


Example
-------

# Enable traffic statistics collection on a GRE tunnel interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Tunnel 10
[*HUAWEI-Tunnel10] tunnel-protocol gre
[*HUAWEI-Tunnel10] statistics enable

```
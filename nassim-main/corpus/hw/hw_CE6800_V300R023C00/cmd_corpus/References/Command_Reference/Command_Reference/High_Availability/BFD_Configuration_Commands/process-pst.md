process-pst
===========

process-pst

Function
--------



The **process-pst** command enables a BFD session to modify the port state table or link state table upon detection of a fault.

The **undo process-pst** command disables a BFD session from modifying the port state table or link state table upon detection of a fault.



By default, a BFD session does not modify the port state table or link state table upon detection of a fault.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**process-pst**

**undo process-pst**


Parameters
----------

None

Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In BFD-based link protection scenarios, you are advised to run the **process-pst** command to enable a BFD session to modify the port state table or link state table upon detection of a fault so that a fast link switchover can be performed.

**Configuration Impact**

After the **process-pst** command is run, the BFD session is associated with the port state table or link state table of the interface to which the BFD session is bound. After the BFD session detects a link down event, the system sets the port state table or link state table of the interface bound to the BFD session to down. Then, the system switches traffic to a working link accordingly.

**Precautions**



The **process-pst** command can be used for a single-hop BFD session bound to an interface. If multiple BFD sessions are bound to the same physical or logical interface, the **process-pst** command can be run for only one BFD session to enable the session to modify the PST.If a BFD session is bound to a sub-interface, the **process-pst** command cannot be run for the BFD session to enable the session to modify the PST or link state table (LST).




Example
-------

# Enable a BFD session to modify the PST.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.10.20.1 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2 interface 100GE 1/0/1
[*HUAWEI-bfd-session-session] process-pst

```
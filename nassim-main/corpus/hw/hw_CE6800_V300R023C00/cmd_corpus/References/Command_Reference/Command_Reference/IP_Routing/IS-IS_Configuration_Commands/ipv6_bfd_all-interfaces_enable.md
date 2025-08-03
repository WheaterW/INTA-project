ipv6 bfd all-interfaces enable
==============================

ipv6 bfd all-interfaces enable

Function
--------



The **ipv6 bfd all-interfaces enable** command enables IPv6 BFD in an IS-IS process.

The **undo ipv6 bfd all-interfaces enable** command disables IPv6 BFD from an IS-IS process.



By default, IPv6 BFD is disabled in an IS-IS process.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 bfd all-interfaces enable**

**undo ipv6 bfd all-interfaces enable**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly,and instruct IS-IS to recalculate routes for correct packet forwarding. You can run the **ipv6 bfd all-interfaces enable** command to enable IPv6 BFD in an IS-IS process.

**Prerequisites**

BFD has been enabled globally, An IS-IS process has been created, and the IS-IS process has been started on a specified interface.

**Configuration Impact**

After the **ipv6 bfd all-interfaces enable** command is run, the local end can establish an IPv6 BFD session with its neighbor through a specified interface and periodically send BFD packets on this session.

**Precautions**

If BFD is not configured globally, you can configure IPv6 BFD for IS-IS, but IPv6 BFD sessions cannot be established.After BFD is enabled for an IS-IS process using the **ipv6 bfd all-interfaces enable** command, no BFD session is established on an interface in the following situations:

* The **isis ipv6 bfd block** command is run on the interface to block the BFD capability of the interface. To create a session on the interface, run the **undo isis ipv6 bfd block** command.
* The **isis ipv6 bfd static** command is run on the interface. In this case, no BFD session is created on the interface. To create a session on the interface, run the **undo isis ipv6 bfd static** command.This command and the **multi-instance enable iid** command are mutually exclusive.

Example
-------

# Configure IPv6 BFD in an IS-IS process.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 bfd all-interfaces enable

```
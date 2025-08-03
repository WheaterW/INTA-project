isis ipv6 bfd enable
====================

isis ipv6 bfd enable

Function
--------



The **isis ipv6 bfd enable** command enables IPv6 BFD on an IS-IS interface to establish IPv6 BFD sessions using default parameters.

The **undo isis ipv6 bfd enable** command cancels the configuration.



By default, IPv6 BFD is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 bfd enable**

**undo isis ipv6 bfd enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly, and instruct IS-IS to recalculate routes for correct packet forwarding. The isis ipv6 bfd enable command can be used to enable IPv6 BFD on an IS-IS interface to establish IPv6 BFD sessions using default parameters.

**Prerequisites**

BFD has been enabled globally, and the IS-IS process has been started on a specified interface.

**Configuration Impact**

After the isis ipv6 bfd enable command is run on an interface, the interface is enabled to establish BFD sessions using default parameter values for fast link fault detection.

**Precautions**

If BFD is not enabled globally, you can set IPv6 BFD parameters on an interface, but the interface cannot establish an IPv6 BFD session.The priority of BFD configured on an interface is higher than that of BFD configured in a process. If IPv6 BFD is enabled on an interface, IPv6 BFD sessions are established based on IPv6 BFD parameters on the interface.If the isis ipv6 bfd block, isis ipv6 bfd enable, isis ipv6 bfd static, and isis ipv6 bfd track session-name commands are run at the same time, only the last command takes effect.


Example
-------

# Enable IPv6 BFD on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 bfd enable

```
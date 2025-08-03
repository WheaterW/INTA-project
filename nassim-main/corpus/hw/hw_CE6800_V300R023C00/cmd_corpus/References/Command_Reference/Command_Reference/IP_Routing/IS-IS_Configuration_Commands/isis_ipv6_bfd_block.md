isis ipv6 bfd block
===================

isis ipv6 bfd block

Function
--------



The **isis ipv6 bfd block** command disables an interface from dynamically establishing IPv6 BFD sessions.

The **undo isis ipv6 bfd block** command cancels the configuration.



By default, no interface is disabled from dynamically establishing IPv6 BFD sessions.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 bfd block**

**undo isis ipv6 bfd block**


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

IPv6 BFD can provide millisecond-level fault detection, help IS-IS to detect the faults on neighboring devices more quickly, and instruct IS-IS to recalculate routes for correct packet forwarding. To enable all IS-IS interfaces to dynamically establish IPv6 BFD sessions, run the **ipv6 bfd all-interfaces enable** command. You can run this command to disable an interface from dynamically establishing IPv6 BFD sessions. To restore the BFD function on an interface, run the **undo isis ipv6 bfd block** command.If the **isis ipv6 bfd enable**, **isis ipv6 bfd static**, or **isis ipv6 bfd track session-name** command is run on an interface, the corresponding function is disabled after the **isis ipv6 bfd block** command is run. To restore the configuration, reconfigure the corresponding command on the interface.

**Prerequisites**

BFD has been enabled globally, and the IS-IS process has been started on a specified interface.

**Configuration Impact**

After the isis ipv6 bfd block command is run on an interface, the interface is disabled from dynamically establishing BFD sessions. As a result, fast link fault detection cannot be implemented.

**Precautions**

If the **isis ipv6 bfd block**, **isis ipv6 bfd enable**, **isis ipv6 bfd static**, and **isis ipv6 bfd track session-name** commands are configured, only the last configuration takes effect.


Example
-------

# Disable 100GE1/0/1 from dynamically establishing IPv6 BFD sessions.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 bfd block

```
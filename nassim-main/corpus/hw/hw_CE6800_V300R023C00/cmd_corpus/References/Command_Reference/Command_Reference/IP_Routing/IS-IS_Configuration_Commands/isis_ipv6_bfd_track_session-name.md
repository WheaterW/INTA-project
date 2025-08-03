isis ipv6 bfd track session-name
================================

isis ipv6 bfd track session-name

Function
--------



The **isis ipv6 bfd track session-name** command binds an IS-IS interface to a link-bundle IPv6 BFD session.

The **undo isis ipv6 bfd track session-name** command unbinds an IS-IS interface from a link-bundle IPv6 BFD session.



By default, IPv6 BFD for IS-IS is disabled on an IS-IS interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 bfd track session-name** *bfd-session-name*

**undo isis ipv6 bfd track session-name** *bfd-session-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bfd-session-name* | Specifies an IPv6 link-bundle BFD session to be bound to an IS-IS interface. The IPv6 BFD session needs to be manually configured. | The value is a string of 1 to 64 case-sensitive characters. |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An IS-IS interface can be bound to an IPv6 BFD session of the link-bundle type by specifying a session name. The IPv6 BFD session needs to be manually configured to quickly detect link faults. You can run the isis ipv6 bfd track session-name command to enable track IPv6 BFD on a specified interface and bind a link-bundle IPv6 BFD session to the interface.

**Prerequisites**

BFD has been enabled globally, and a specified interface has been bound to an IS-IS process using the **isis ipv6 enable** command.

**Precautions**

If the isis ipv6 bfd block, isis ipv6 bfd enable, isis ipv6 bfd static, and isis ipv6 bfd track session-name commands are run at the same time, only the last command takes effect.


Example
-------

# Enable the function of tracking IPv6 BFD on the interface.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface Eth-Trunk1
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] bfd AtoB bind link-bundle peer-ipv6 2001:db8:1::2 interface Eth-Trunk1 source-ipv6 2001:db8:1::1
[*HUAWEI] interface Eth-Trunk1
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] isis ipv6 enable 1
[*HUAWEI-Eth-Trunk1] isis ipv6 bfd track session-name AtoB

```
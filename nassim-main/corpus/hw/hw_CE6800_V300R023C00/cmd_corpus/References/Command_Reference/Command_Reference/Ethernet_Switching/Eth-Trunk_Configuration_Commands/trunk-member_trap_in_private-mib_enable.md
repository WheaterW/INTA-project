trunk-member trap in private-mib enable
=======================================

trunk-member trap in private-mib enable

Function
--------



The **trunk-member trap in private-mib enable** command enables Eth-Trunk member interfaces to send trap messages about their status changes through a private MIB.

The **undo trunk-member trap in private-mib enable** command disables Eth-Trunk member interfaces from sending trap messages about their status changes through a private MIB.



By default, Eth-Trunk member interfaces send trap messages about their status changes through a public MIB.


Format
------

**trunk-member trap in private-mib enable**

**undo trunk-member trap in private-mib enable**


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



MIBs include public and private MIBs. Public MIBs are defined in RFCs and mainly used for structured design and interface standardization of various public protocols. Private MIBs are used by companies to implement proprietary protocols or perform specific functions. Private MIBs can also help a third-party NMS to manage devices running proprietary protocols or specific functions.When Eth-Trunk member interfaces change from Up to Down or Down to Up, you need to learn the status changes through trap messages so to determine whether the status changes are caused by device faults. By default, Eth-Trunk member interfaces use a public MIB to send trap messages. The trap content can be checked through linkDown\_active and linkDown\_clear in the log reference. Trap messages do not carry the physical status information of a specific Eth-Trunk member interface if sent through a public MIB, whereas carry the desired information if sent through a private MIB. To obtain the physical status of a specific Eth-Trunk member interface, run the trunk-member trap in private-mib enable command. The Eth-Trunk member interface then uses a private MIB to send trap messages about its status changes. You can check the trap content through TRUNK\_MEM\_LINKDOWN and TRUNK\_MEM\_LINKUP in the log reference.




Example
-------

# Enable Eth-Trunk member interfaces to send trap messages through a private MIB.
```
<HUAWEI> system-view
[~HUAWEI] trunk-member trap in private-mib enable

```
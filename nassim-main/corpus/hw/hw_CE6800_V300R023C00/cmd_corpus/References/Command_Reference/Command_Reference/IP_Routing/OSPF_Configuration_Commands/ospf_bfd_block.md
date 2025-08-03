ospf bfd block
==============

ospf bfd block

Function
--------



The **ospf bfd block** command prevents an interface from dynamically setting up a BFD session.

The **undo ospf bfd block** command cancels the configuration.



By default, BFD is enabled in the OSPF interface view.


Format
------

**ospf bfd block**

**undo ospf bfd block**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **bfd all-interfaces enable** command is run in an OSPF process, all interfaces on which neighbor relationships are in Full state in the OSPF process create BFD sessions. To disable BFD on a multi-area adjacency interface, run the ospf bfd block multi-area command.

**Prerequisites**

BFD has been enabled on these interfaces.

**Precautions**

The ospf bfd enable and ospf bfd block commands cannot both take effect. The later configuration overrides the previous one.


Example
-------

# Prevent 100GE 1/0/1 from dynamically setting up a BFD session.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf bfd block

```
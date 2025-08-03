silent-interface (OSPF view)
============================

silent-interface (OSPF view)

Function
--------



The **silent-interface** command disables an interface from receiving and sending OSPF packets.

The **undo silent-interface** command restores the default setting.



By default, an interface can receive and send OSPF packets.


Format
------

**silent-interface** { **all** | { *interface-name* | *interface-type* *interface-number* } }

**undo silent-interface** { **all** | { *interface-name* | *interface-type* *interface-number* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all interfaces in a specified process. | - |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the interface number. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent the local router from sending its OSPF routing information to other routers on a network and from receiving routing update information advertised by other routers, run the **silent-interface** command.Disabling interfaces from receiving or sending OSPF packets is a solution to routing loops.

**Configuration Impact**

After an OSPF interface is set to be in the silent state, the interface can still advertise its direct routes. Hello packets on the interface, however, will be blocked, and no neighbor relationship can be established on the interface. This can enhance the networking adaptability of OSPF and reduce the consumption of system resources.

**Precautions**

1. If the **undo silent-interface** command has been run in the current process, running the **silent-interface all** command deletes the **undo silent-interface** command. As a result, the OSPF neighbor relationship established on the interface specified by the **undo silent-interface** command goes Down.
2. After the **silent-interface** command is run, if an OSPF neighbor relationship has been established on the interface of the local device, the OSPF neighbor relationship goes Down immediately. However, the peer device needs to wait until the Hello timer expires. As a result, routes may be unreachable before the peer device goes Down.

Example
-------

# Disable an interface from sending or receiving OSPF packets.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] silent-interface 100GE1/0/1

```
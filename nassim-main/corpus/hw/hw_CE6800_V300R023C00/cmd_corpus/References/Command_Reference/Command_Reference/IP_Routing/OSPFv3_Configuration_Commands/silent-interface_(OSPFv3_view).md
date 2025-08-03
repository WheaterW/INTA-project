silent-interface (OSPFv3 view)
==============================

silent-interface (OSPFv3 view)

Function
--------



The **silent-interface** command disables an interface from receiving and sending OSPFv3 packets.

The **undo silent-interface** command restores the default setting.



By default, an interface can receive and send OSPFv3 packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**silent-interface** { **all** | { *interface-name* | *interface-type* *interface-number* } }

**undo silent-interface** { **all** | { *interface-name* | *interface-type* *interface-number* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all interfaces in a specified process. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent OSPFv3 routes from being received by other routers on the network and disable the local router from receiving updated routes, run the **silent-interface** command. After an interface is disabled from receiving and sending OSPFv3 packets, the interface can still advertise its routes but cannot exchange Hello packets with others. Therefore, no neighbor relationship can be established between the interface and others. This can enhance the networking adaptability of OSPFv3 and reduce system resource consumption.For example, when no OSPFv3 neighbor relationship is required between a user-side interface and a user terminal, but routes of the interface still need to be advertised to implement user-and-network interworking, run this command.Disabling interfaces from receiving or sending OSPFv3 packets is a solution to routing loops.

**Configuration Impact**

Different processes can disable the same interface from sending and receiving OSPFv3 packets. However, the **silent-interface** command takes effect only on the OSPFv3 interface of the process.

**Precautions**

If the **undo silent-interface** command has been run in the current process, running the **silent-interface all** command causes the **undo silent-interface** command configuration to be deleted. As a result, the OSPFv3 neighbor relationship established using the interface specified in the **undo silent-interface** command goes down.


Example
-------

# Disable 100GE 1/0/1 from sending and receiving OSPFv3 packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] silent-interface 100GE1/0/1

```

# Disable all interfaces in process 1 from receiving and sending OSPFv3 packets.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] silent-interface all

```
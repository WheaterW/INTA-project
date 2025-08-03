silent-interface (RIP view)
===========================

silent-interface (RIP view)

Function
--------



The **silent-interface** command enables an interface to receive RIP packets to update its routing table but disables it from sending RIP packets.

The **undo silent-interface** command re-enables an interface to send updated packets.



By default, an interface is not suppressed.


Format
------

**silent-interface** [ **disable** ] { *interface-type* *interface-number* | *interface-name* }

**undo silent-interface** { *interface-type* *interface-number* | *interface-name* }

**undo silent-interface disable** { *interface-type* *interface-number* | *interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Enables interfaces to send RIP packets. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device running RIP is connected to a network running other routing protocols, you can run the **silent-interface** command on the interface that connects the device to the network to prevent the interface from sending packets to the network. This also prevents routing loops.If you want only a small number of interfaces to be active while the rest interfaces are suppressed, run the **silent-interface all** command to suppress all interfaces and then run the **silent-interface disable interface-type interface-number** command to activate specified interfaces.This command can be used together with the peer (RIP) command to advertise routes to a specified device.

**Precautions**



The **silent-interface** command that is run in a RIP process takes precedence over the rip input or rip output command that is run on an interface.




Example
-------

# Configure all interfaces as silent interfaces, and then activate 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] silent-interface all
[*HUAWEI-rip-100] silent-interface disable 100GE 1/0/1

```

# Configure the RIP interface 100GE 1/0/1 as a silent interface and enable it to send routes to the neighbor with IP address 10.1.1.1/24.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] silent-interface 100GE 1/0/1
[*HUAWEI-rip-100] peer 10.1.1.1

```
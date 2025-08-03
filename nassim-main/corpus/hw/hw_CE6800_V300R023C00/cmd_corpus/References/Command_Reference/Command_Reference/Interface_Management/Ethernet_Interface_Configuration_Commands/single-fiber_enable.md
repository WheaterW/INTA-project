single-fiber enable
===================

single-fiber enable

Function
--------



The **single-fiber enable** command enables the single-fiber communication function of the optical interface.

The **undo single-fiber enable** command to disable the single-fiber communication function of the optical interface.



By default, the single-fiber communication function of the optical interface is disabled.


Format
------

**single-fiber enable**

**undo single-fiber enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network management and maintenance, the administrator may send user traffic to a specified server for analysis, recording, and processing. If a server can receive and send packets, there is a possibility that the server forwards user traffic to other devices, causing a security risk. The unidirectional single-fiber communication function can address this issue. A single fiber means that two optical modules are connected by only one fiber, and unidirectional communication means that packets can be sent in only one direction. With this function, a device can only send but not receive packets, and an analysis server can only receive but not send packets, thereby ensuring data security.After you run the **single-fiber enable** command on an interface of the local device, the interface can only send or receive packets through a single fiber. The specific value depends on the connection mode between the transmit end (TX) and the receive end (RX) of the optical module. For example, if the TX end of the optical module on the local device is connected to the RX end of the optical module on the peer device, the local device only sends packets, and the peer device only receives packets. Conversely, if the RX end of the optical module on the local device is connected to the TX end of the optical module on the peer device, the local device only receives packets, and the peer device only sends packets.

**Precautions**

* This command is supported only when an optical module is pre-configured or an optical interface has an optical module (not a single-fiber bidirectional optical module) installed. After the command is run and an optical module is installed on an optical interface, the interface is in Up state. For details about optical module types, see Optical Module in the Hardware Description. You can run the **display interface transceiver** command to check optical module information on an interface.
* Split optical interfaces do not support this command.
* After the **single-fiber enable** command is run on an interface, the interface is Down and the single-fiber communication function cannot be used if no optical module is installed, a single-fiber bidirectional optical module is installed, an MPO optical module is installed, or a high-speed cable is connected to the interface.
* The peer device also needs to support single-fiber communication. The local and remote interfaces must work in non-auto-negotiation mode and have the same rate configured.
* The single-fiber enable and loopback internal commands cannot be used together.

Example
-------

# Enable the single-fiber communication function of the optical interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] single-fiber enable

```
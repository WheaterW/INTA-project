isis timer holding-multiplier (interface view)
==============================================

isis timer holding-multiplier (interface view)

Function
--------



The **isis timer holding-multiplier** command sets the IS-IS holdtime to be a multiple of the interval at which Hello packets are sent.

The **undo isis timer holding-multiplier** command restores the default value.



By default, the holdtime is three times the interval at which Hello packets are sent.


Format
------

**isis timer holding-multiplier** *number* [ **level-1** | **level-2** ]

**undo isis timer holding-multiplier** [ *number* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the IS-IS holdtime to be a multiple of the interval at which Hello packets are sent. | The value is an integer ranging from 3 to 1000. |
| **level-1** | Specifies the holdtime of a Level-1 neighbor. | - |
| **level-2** | Specifies the holdtime of a Level-2 neighbor.  If neither Level-1 nor Level-2 is specified, the default level is Level-1 and Level-2.  level-1 and level-2 can be configured only on IS-IS broadcast interfaces. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Devices at both ends of a link establish a neighbor relationship by sending Hello packets. After the neighbor relationship is established, Hello packets need to be periodically sent to maintain the neighbor relationship. If a device at one end of a link does not receive Hello packets from the peer device within a specified period, the device considers the peer neighbor Down. The interval is called the neighbor holdtime.For example, if the interval for sending Hello packets is set to 20 seconds using the **isis timer hello 20** command and the isis timer holding-multiplier 4 command is run on the local device, the suppression time is 80 seconds (4 x 20 = 80). When you run the **isis timer hello** command to change the interval for sending Hello packets, the holdtime of the neighbor changes accordingly.On a broadcast network, to ensure fast route convergence, the interval at which the DIS sends Hello packets is short, and the holdtime of the DIS neighbor observed on the DIS neighbor is also short. DIS neighbor holdtime = Interval at which Hello packets are sent x Number. The non-DIS neighbor holdtime is 1/3 of the DIS neighbor holdtime.

**Configuration Impact**

If the value of number is set too large, the local device needs to wait a long time before detecting its neighbor Down, which slows down IS-IS route convergence. If the value of number is set too small, the neighbor relationship will alternate between Up and Down when some Hello packets are lost due to transmission delays and errors on the network. This causes route flapping on the IS-IS network. Setting the same interval at which Hello packets are sent and the same neighbor holdtime for all devices on the IS-IS network is recommended so that all devices detect link failures at the same time.

**Precautions**

If a broadcast interface is emulated as a P2P interface using the **isis circuit-type** command or an emulated P2P interface is restored to the broadcast interface using the **undo isis circuit-type** command, the multiplier of the neighbor holdtime relative to the interval for sending Hello packets is restored to the default value.When you run the **isis timer hello** command to set the interval for sending Hello packets and specify the conservative parameter, if the holdtime of an IS-IS neighbor is less than 20, the neighbor relationship is disconnected without delay after the holdtime expires. If conservative is not specified and the holdtime of an IS-IS neighbor relationship is less than 20, the holdtime is delayed to 20s after the holdtime expires. After the holdtime expires, the neighbor relationship is disconnected.


Example
-------

# Set the number of IS-IS Level-2 Hello packets sent by the neighbor but not received by IS-IS when the neighbor is declared Down to 6 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis timer holding-multiplier 6 level-2

```
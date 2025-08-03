isis timer holding-multiplier
=============================

isis timer holding-multiplier

Function
--------



The **isis timer holding-multiplier** command sets the IS-IS holdtime to be a multiple of the interval at which Hello packets are sent.

The **undo isis timer holding-multiplier** command restores the default value.



By default, the holdtime is three times the interval at which Hello packets are sent.


Format
------

**isis timer holding-multiplier** *number*

**undo isis timer holding-multiplier** [ *number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Sets the holdtime of a neighbor to a multiple of the interval at which Hello packets are sent. | The value is an integer ranging from 3 to 1000. The default value is 3. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Devices at both ends of a link establish a neighbor relationship by sending Hello packets to each other. After the neighbor relationship is established, both devices need to send Hello packets at a specified interval to maintain the neighbor relationship. If a device does not receive any Hello packet from its neighbor within a specified period of time, the device considers the neighbor to be Down. The specified time period is known as the neighbor holdtime.For example, if you run the **isis timer hello 20** command to set the interval for sending Hello packets to 20s on the local device, and then run the isis timer holding-multiplier 4 command, the holdtime is 80s (4\ x 20 = 80). If the interval for sending Hello packets is changed using the **isis timer hello** command, the holdtime will be changed accordingly.

**Configuration Impact**

If the value of number is set too large, the local device needs to wait a long time before detecting its neighbor Down, which slows down IS-IS route convergence. If the value of number is set too small, the neighbor relationship will alternate between Up and Down when some Hello packets are lost due to transmission delays and errors on the network. This causes route flapping on the IS-IS network. Setting the same interval at which Hello packets are sent and the same neighbor holdtime for all devices on the IS-IS network is recommended so that all devices detect link failures at the same time.

**Precautions**

If a broadcast interface is emulated as a P2P interface using the **isis circuit-type** command or an emulated P2P interface is restored to the broadcast interface using the **undo isis circuit-type** command, the multiplier of the neighbor holdtime relative to the interval for sending Hello packets is restored to the default value.When you run the **isis timer hello** command to set the interval for sending Hello packets and specify the conservative parameter, if the holdtime of an IS-IS neighbor is less than 20, the neighbor relationship is disconnected without delay after the holdtime expires. If conservative is not specified and the holdtime of an IS-IS neighbor relationship is less than 20, the holdtime is delayed to 20s after the holdtime expires. After the holdtime expires, the neighbor relationship is disconnected.


Example
-------

# Set the number of IS-IS Level-2 Hello packets sent by the neighbor but not received by IS-IS when the neighbor is declared Down to 6 on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis circuit-type p2p
[*HUAWEI-100GE1/0/1] isis timer holding-multiplier 6 level-2

```
isis circuit-type
=================

isis circuit-type

Function
--------



The **isis circuit-type** command sets the network type of an interface to emulate a P2P interface.

The **undo isis circuit-type** command restores the default network type.



By default, the network type of an interface is determined by the physical type of the interface.


Format
------

**isis circuit-type p2p** [ **strict-snpa-check** ]

**isis process-id** *process-id* **circuit-type** **p2p** [ **strict-snpa-check** ]

**undo isis circuit-type**

**undo isis process-id** *process-id* **circuit-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **strict-snpa-check** | Enables IS-IS to check the SNPA address of each received LSP or SNP. | - |
| **process-id** *process-id* | Specifies the IID of an IS-IS multi-instance process. | The value is an integer ranging from 1 to 4294967295. |
| **p2p** | Sets the interface network type as P2P. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The network type of IS-IS interfaces at the ends of a link must be the same. Otherwise, the two interfaces cannot set up a neighbor relationship.The **isis circuit-type** command sets the network type of an interface to emulate a P2P interface so that the IS-IS interfaces at the ends of the link have the same network type and a neighbor relationship can be established between them.When an IS-IS neighbor relationship is established between a P2P interface and a simulated P2P interface and the simulated P2P interface has direct neighbors, the P2P interface may receive unneeded packets from these direct neighbors. To prevent the P2P interface from accepting these unneeded packets, specify strict-snpa-check in the **isis circuit-type** command to enable IS-IS to check the SNPA address of each received LSP or SNP. After the command is run, the P2P interface accepts only the packets whose SNPA addresses are included in the local neighbor address list, which improves network security.

**Prerequisites**

IS-IS has been enabled on interfaces using the **isis enable** command.

**Configuration Impact**

For an IS-IS interface, when the network type of the interface changes, corresponding configurations change accordingly. Details are as follows:

* After a broadcast interface is emulated as a P2P interface using the **isis circuit-type** command, the interval at which Hello packets are sent, the number of Hello packets that IS-IS does not receive from a neighbor before the neighbor is declared Down, interval at which LSPs are retransmitted on a P2P link, and the IS-IS authentication mode are restored to the default settings; other configurations such as the DIS priority, DIS name, and the interval at which CSNPs are sent on a broadcast network become invalid.
* After the **undo isis circuit-type** command is run to restore the network type of the interface, the interval at which Hello packets are sent, the number of Hello packets that IS-IS does not receive from a neighbor before the neighbor is declared Down, interval at which LSPs are retransmitted on a P2P link, the IS-IS authentication mode, DIS priority, and the interval at which CSNPs are sent on a broadcast network are restored to the default settings.

**Precautions**

If the network type of an interface is changed, some parameters of the IS-IS process are restored to the default settings. Exercise caution before running the command.This command is applicable only to broadcast interfaces. If it is run on a P2P or P2MP interface, it does not take effect, and its configuration is not recorded in the configuration file.


Example
-------

# Set the network type of 100GE 1/0/1 as P2P.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis circuit-type p2p

```
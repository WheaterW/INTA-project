Overview of Interface Management
================================

This section provides the physical and logical interfaces supported by the NE40E and describes the interface views and prompts and common link protocols and access technologies.

#### Interface Types

Devices exchange data and interact with other devices on a network through interfaces. Interfaces are classified into physical and logical interfaces.

* Physical Interfaces
  
  Physical interfaces physically exist on boards. They are classified into the following types:
  
  + LAN interfaces: interfaces through which the Router can exchange data with other devices on a LAN.
  + WAN interfaces: interfaces through which the Router can exchange data with remote devices on external networks.
* Logical Interfaces
  
  Logical interfaces are manually configured interfaces that do not exist physically. Logical interfaces can be used to exchange data.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The management network port of the main control board does not forward services.



#### Interface Views and Prompts

[Table 1](#EN-US_CONCEPT_0172362528__en-us_concept_0172352039_ifm_05) lists the commands, views, and prompts of physical interfaces supported by the NE40E. [Table 2](#EN-US_CONCEPT_0172362528__en-us_concept_0172352039_table942771145415) lists the commands, views, and prompts of logical interfaces supported by the NE40E.

**Table 1** Commands, views, and prompts of physical interfaces supported by the NE40E
| Interface Name | Command View | Operation | Prompt |
| --- | --- | --- | --- |
| GE interface | GE interface view | Run the **interface** **gigabitethernet** 0/2/0 command in the system view. | [~HUAWEI-GigabitEthernet0/2/0] |
| 10GE interface | 10GE interface view | Run the **interface** **gigabitethernet** 0/1/0 command in the system view.  NOTE:  The interfaces marked with **10G** displayed in the [**display interface brief**](cmdqueryname=display+interface+brief) command output indicate GE interfaces whose bandwidth is 10 Gbit/s. | [~HUAWEI-GigabitEthernet0/1/0] |
| 25GE interface | 25GE interface view | Run the **interface** **25GE** 0/2/0 command in the system view. | [~HUAWEI-25GE0/2/0] |
| 40GE interface | 40GE interface view | Run the **interface** **40GE** 0/2/0 command in the system view. | [~HUAWEI-40GE0/2/0] |
| 100GE interface | 100GE interface view | Run the **interface** **100GE** 0/1/0 command in the system view. | [~HUAWEI-100GE0/1/0] |
| 200GE interface | 200GE interface view | Run the **interface** **200GE** 0/1/0 command in the system view. | [~HUAWEI-200GE0/1/0] |
| XGE interface | XGE interface view | Run the **interface** **XGigabitEthernet** 0/1/0 command in the system view. | [~HUAWEI-XGigabitEthernet0/1/0] |
| CPOS interface | CPOS interface view | Run the **controller** **cpos** 0/3/0 command in the system view. | [~HUAWEI-Cpos0/3/0] |
| POS interface | POS interface view | Run the **interface** **pos** 0/3/0 command in the system view. | [~HUAWEI-Pos0/3/0] |
| 50GE interface | 50GE interface view | Run the **interface** **50GE** 0/1/0 command in the system view. | [~HUAWEI-50GE0/1/0] |
| 50|100GE interface | 50|100GE interface view  NOTE:  The default rate of this type of interface is 50 Gbit/s and can be switched to 100 Gbit/s. | Run the **interface** **50|100GE** 0/1/0 command in the system view. | [~HUAWEI-50|100GE0/1/0] |
| FlexE-50G interface | FlexE-50G interface view | Run the **interface** **FlexE-50G** 0/1/0 command in the system view. | [~HUAWEI-FlexE-50G0/1/0] |
| FlexE-100G interface | FlexE-100G interface view | Run the **interface** **FlexE-100G** 0/1/0 command in the system view. | [~HUAWEI-FlexE-100G0/1/0] |
| FlexE-50|100G interface | FlexE-50|100G interface view | Run the **interface** **FlexE-50|100G** 0/1/0 command in the system view. | [~HUAWEI-FlexE-50|100G0/1/0] |
| E1 interface | E1 interface view  NOTE:  The NE40E-M2K-B does not support E1. | Run the **controller** **E1** 0/3/0 command in the system view. | [~HUAWEI-E10/3/0] |


**Table 2** Commands, views, and prompts of logical interfaces
| Interface Name | Command View | Operation | Prompt |
| --- | --- | --- | --- |
| Sub-interface | Sub-interface view | Run the **interface gigabitethernet 0/1/0.1** command in the system view. | [~HUAWEI-GigabitEthernet0/1/0.1] |
| Eth-Trunk interface | Eth-Trunk interface view | Run the **interface eth-trunk 2** command in the system view. | [~HUAWEI-Eth-Trunk2] |
| VE interface | VE interface view | Run the **interface virtual-ethernet 0/1/0** command in the system view. | [~HUAWEI-Virtual-Ethernet0/1/0] |
| Global VE interface | Global VE interface view | Run the **interface global-ve 0** command in the system view. | [~HUAWEI-Global-VE0] |
| VLANIF interface | VLANIF interface view | Run the **interface vlanif 2** command in the system view. | [~HUAWEI-Vlanif2] |
| Loopback interface | Loopback interface view | Run the **interface loopback 2** command in the system view. | [~HUAWEI-LoopBack2] |
| Null interface | Null interface view | Run the **interface null 0** command in the system view. | [~HUAWEI-NULL0] |
| IP-Trunk interface | IP-Trunk interface view | Run the **interface ip-trunk 2** command in the system view. | [~HUAWEI-Ip-Trunk2] |
| Tunnel interface | Tunnel interface view | Run the **interface tunnel 2** command in the system view. | [~HUAWEI-Tunnel 2] |
| NVE interface | NVE interface view | Run the **interface nve 1** command in the system view. | [~HUAWEI-Nve1] |
| FlexE interface | FlexE interface view | Run the **interface** **FlexE** 0/2/5 command in the system view. | [~HUAWEI-FlexE0/2/5] |
| PW-VE interface | PW-VE interface view | Run the **interface pw-ve 1** command in the system view. | [~HUAWEI-pw-ve1] |



#### Commonly-used Link Protocols and Access Technologies

The link layer is responsible for accurately sending data from a node to a neighboring node. It receives packets from the network layer, encapsulates the packets in frames, and then sends the frames to the physical layer.

Major link layer protocols supported by the NE40E are listed as follows:

* Ethernet
  
  Currently, the LAN mostly refers to the Ethernet. The Ethernet is a broadcast network, which is flexible and simple in configuration as well as easy to expand. For these reasons, the Ethernet is widely used.
* Trunk
  
  Trunks can be classified into Eth-Trunks and IP-Trunks. An Eth-Trunk must be composed of Ethernet links, and an IP-Trunk must be composed of POS links.
  
  The trunk technology has the following advantages:
  
  + Bandwidth increase: The bandwidth of a trunk is the total bandwidth of all member interfaces.
  + Reliability enhancement: When a link fails, other links in the same trunk automatically take over the services on the faulty link to prevent traffic interruption.
* PPP
  
  The Point-to-Point Protocol (PPP) is used to encapsulate IP packets on serial links. It supports both the asynchronous transmission of 8-bit data without the parity check and the bit-oriented synchronous connection.
  
  PPP consists of the Link Control Protocol (LCP) and the Network Control Protocol (NCP). LCP is used to create, configure, and test links; NCP is used to control different network layer protocols.
* HDLC
  
  The High-Level Data Link Control (HDLC) is a suite of protocols that are used to transmit data between network nodes. HDLC is widely used at the data link layer.
  
  In HDLC, the receiver responds with an acknowledgment when it receives frames transmitted over the network. In addition, HDLC manages data flows and the interval at which data packets are transmitted.

#### Interface Flapping Control

The status of an interface on a device may alternate between up and down for various reasons, including physical signal interference and incorrect link layer configurations. The changing status causes routing protocols and Multiprotocol Label Switching (MPLS) to flap. As a result, the device may break down, causing network interruption. Control-flap controls the frequency of interface status alternations between up and down to minimize the impact on device and network stability.

The following two control modes are available.

**Table 3** Flapping control modes
| Control Mode | Function | Usage Scenario |
| --- | --- | --- |
| control-flap | Controls the frequent flappings of interfaces at the network layer to minimize the impact on device and network stability. | * This control mode is interface-specific. * This control mode suppresses interface flappings from the network layer and reports the flappings to the routing management module, thereby improving network-layer stability. * This control mode allows you to precisely configure parameters based on service requirements. * This control mode involves complex algorithms and is highly demanding to use. |
| damp-interface | Controls the frequent flappings of interfaces at the physical layer to minimize the impact on device and network stability. | * This function is supported globally or on a specified interface. * This control mode suppresses the flappings from the physical layer, thereby improving link-layer and network-layer stability. * This control mode prevents the upper-layer protocols from frequently alternating between enabled and disabled, thereby reducing the consumption of CPU and memory resources. * This control mode does not involve any complex algorithms and is easy to use. |
Basic Concepts of 1588v2
========================

Basic Concepts of 1588v2

#### Clock Synchronization

Network clock synchronization, which includes frequency synchronization and phase synchronization, ensures that the frequency or time difference between devices on the entire network is within an appropriate range.

* **Frequency synchronization**
  
  Signals use the same frequency and a fixed difference between phases. Frequency synchronization enables signals to be sent or received at an average rate, enabling all devices on a communications network to operate at the same rate.
* **Phase synchronization**
  
  Phase synchronization, also known as time synchronization, refers to the consistency of both frequencies and phases between signals, whereby the phase difference between signals is always 0.

[Figure 1](#EN-US_CONCEPT_0000001563878921__en-us_concept_0141108986_fig_dc_cfg_ecsyn_000401) illustrates the differences between frequency synchronization and phase synchronization. If Watch A and Watch B show different time but maintain a constant time difference, this is called frequency synchronization. If Watch A and Watch B maintain the same time, this is called phase synchronization.

**Figure 1** Frequency synchronization and phase synchronization  
![](figure/en-us_image_0000001563759329.png)

#### Clock Synchronization Network Hierarchy

A clock synchronization network implements clock synchronization between network devices. [Figure 2](#EN-US_CONCEPT_0000001563878921__fig_dc_cfg_ptp_000401) shows the structure of a clock synchronization network. In the two-level clock synchronization network, level-1 nodes use stratum-1 clocks, and level-2 nodes use stratum-2 clocks. Below level-2 nodes are client devices, which require clock synchronization.

Across an entire 1588v2 network, all clocks are organized into a master-slave synchronization hierarchy, with the grandmaster clock at the top. The clocks exchange 1588v2 messages with each other to implement synchronization. A slave clock calculates its offset and delay compared with the master clock based on the timestamp carried in a 1588v2 message to synchronize its local clock with the master clock.

**Figure 2** Clock synchronization network hierarchy  
![](figure/en-us_image_0000001513158966.png "Click to enlarge")

#### PTP Domain

A PTP domain is a set of clocks running PTP, and each network can contain multiple PTP domains. Each PTP domain has only one clock source, and all devices in the PTP domain are synchronized with it. In addition, each PTP domain has its own synchronization time which is independent of the others.


#### Clock Node

The nodes in a PTP domain are referred to as clock nodes. PTP defines the following types of clock nodes:

* Ordinary clock (OC)
  
  In a PTP domain, an OC is a clock with a single port that can participate in PTP clock synchronization. An OC uses this interface to synchronize its time with an upstream device or to advertise the time to downstream devices.
* Boundary clock (BC)
  
  In a PTP domain, a BC is a clock with two or more ports that can participate in PTP clock synchronization. A BC synchronizes its time with an upstream device through one port and advertises the time to downstream interfaces through the others.
  
  A clock node is also a BC device if it functions as the clock source and advertises the time to downstream devices through multiple PTP ports.


#### Supported Clock Types

* OC
* BC

#### PTP Port

A PTP port refers to a port on which the PTP function is enabled. PTP ports are classified into the following types by role:

* Master port: advertises the time to downstream devices and can be configured on a BC or OC.
* Slave port: receives the time information from an upstream device, and can be a BC or OC port.
* Passive port: is an idle port on a BC device and does not send or receive synchronization clock signals.


#### 1588v2 Message

1588v2 messages are exchanged between master and slave devices to establish master-slave hierarchy and implement clock synchronization. PTP messages can be classified into the following types, depending on whether they carry timestamps:

* Event message: is tagged with a timestamp when reaching or leaving a port. PTP devices calculate the path delay based on such timestamps. Four types of event messages exist: Sync, Delay\_Req, Pdelay\_Req, and Pdelay\_Resp.
* General message: is not tagged with a timestamp and is used to establish master-slave hierarchy and to request and send time information. Six types of general messages exist: Announce, Follow\_Up, Delay\_Resp, Pdelay\_Resp\_Follow\_Up, Management, and Signaling.

| Message | Function |
| --- | --- |
| Sync | A Sync message is sent from the master to the slave and carries the timestamp t1 added by the master. Sync messages can be sent in one-step or two-step mode.  * In one-step mode, a Sync message carries a timestamp of identifying when the message was sent. * In two-step mode, a Sync message records the time when the message was sent, but does not contain the transmit timestamp. Instead, a transmit timestamp is carried in a Follow\_Up message. |
| Delay\_Req | A Delay\_Req message is sent from the slave to the master during time synchronization in the Delay mechanism and carries the timestamp t3 added by the slave. |
| Pdelay\_Req | The device currently does not support Pdelay\_Req and Pdelay\_Resp messages. |
| Pdelay\_Resp |
| Announce | An Announce message is used to exchange time source information between clock nodes in order to establish the master-slave hierarchy. |
| Follow\_Up | In two-step mode, a Follow\_Up message is sent by the master to the slave during time synchronization in the Delay mechanism and carries the timestamp t1 added by the master. |
| Delay\_Resp | A Delay\_Resp message is sent by the master to the slave during time synchronization in the Delay mechanism and carries the timestamp t4 and port ID added by the master. |
| Pdelay\_Resp\_Follow\_Up | The device currently does not support Pdelay\_Resp\_Follow\_Up, Management, and Signaling messages. |
| Management |
| Signaling |



#### Master-Slave Hierarchy

The master-slave relationship is relative. For a pair of clock nodes that are synchronized with each other, the master-slave relationship is as follows:

* The node that advertises the time to the downstream node is the master node, and the node that synchronizes the time from the upstream node is the slave node.

* The clock on the master node is the master clock, and the clock on the slave node is the slave clock.

* The port that advertises the time is the master port, and the port that receives the time is the slave port.

A device can concurrently synchronize the time with an upstream device and advertise the time to downstream devices.


#### Grandmaster Clock

All clock nodes in a PTP domain are organized into the master-slave hierarchy. The grandmaster clock is at the top of this hierarchy and is the PTP domain's reference clock. Through 1588v2 message exchanges between clock nodes, all devices in the PTP domain synchronize the time with the grandmaster clock. As such, the grandmaster clock is also referred to as the PTP domain's clock source. [Selecting the Grandmaster Clock and Determining the Master-Slave Hierarchy](galaxy_1588v2_cfg_0005.html) describes how to dynamically select the grandmaster clock through the best master clock (BMC) algorithm.
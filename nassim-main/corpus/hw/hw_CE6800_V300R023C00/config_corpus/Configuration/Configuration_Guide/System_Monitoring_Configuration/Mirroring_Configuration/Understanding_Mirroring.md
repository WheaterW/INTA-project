Understanding Mirroring
=======================

Understanding Mirroring

#### Basic Concepts

[Figure 1](#EN-US_CONCEPT_0000001563886321__fig354991715599) describes the two basic concepts in mirroring: mirrored ports and observing ports.

**Mirrored port****s**

A mirrored port is a port on which packets are copied and then sent to an observing port for analysis.

**Observing port****s**

An observing port is connected to a monitoring device and transmits the packets copied from a mirrored port to the monitoring device.

An observing port group is a group of ports, each of which connects to a monitoring device. Packets mirrored to an observing port group are copied to all the member ports in the observing port group.

**Figure 1** Networking diagram of mirroring  
![](figure/en-us_image_0000001513046358.png)

#### Mirroring Types

[Table 1](#EN-US_CONCEPT_0000001563886321__table528974220561) lists types of mirroring functions in different dimensions.

**Table 1** Mirroring types
| Dimension | Mirroring Function | Description |
| --- | --- | --- |
| Mirrored source (most widely used method) | Port mirroring | Copies packets received or sent by a mirrored port to an observing port. |
| Flow mirroring | Copies traffic matching specified rules to an observing port. |
| VLAN mirroring | Copies packets received or sent by all active interfaces in a specified VLAN to an observing port. |
| Packet flow direction | Inbound mirroring | Copies packets received by a mirrored port to an observing port. Inbound mirroring is also called upstream mirroring. |
| Outbound mirroring | Copies packets sent by a mirrored port to an observing port. Outbound mirroring is also called downstream mirroring. |
| Bidirectional mirroring | Copies packets received and sent by a mirrored port to an observing port. |
| Ratio of mirrored sources to observing ports | 1:1 mirroring | Copies packets from one mirrored source to one observing port. |
| N:1 mirroring | Copies packets from *N* mirrored sources to one observing port. |
| 1:N mirroring | Copies packets from one mirrored source to *N* observing ports. |
| M:N mirroring | Copies packets from *M* mirrored sources to *N* observing ports. |

When flow mirroring, port mirroring, and VLAN mirroring are configured simultaneously on a device to mirror packets to different observing ports, the priorities are as follows: flow mirroring > port mirroring > VLAN mirroring, and only one observing port can receive mirrored packets.
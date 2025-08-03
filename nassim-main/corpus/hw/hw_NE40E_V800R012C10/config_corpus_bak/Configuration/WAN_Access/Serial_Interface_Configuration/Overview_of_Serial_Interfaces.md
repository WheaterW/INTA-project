Overview of Serial Interfaces
=============================

Serial interfaces, as one type of the most commonly used WAN interfaces, are classified as synchronous serial interfaces or asynchronous serial interfaces.

Compared with asynchronous serial interfaces, synchronous serial interfaces are more commonly used. Unless otherwise specified in this document, serial interfaces refer to synchronous ones.

#### Supported Types of Serial Interfaces

The device supports synchronous serial interfaces formed using E1 and CPOS interfaces. The indexing modes of these interfaces are different.

various synchronous serial interfaces channelized from physical interfaces support link-layer protocol and MTU configuration. [Table 1](#EN-US_CONCEPT_0172363974__tab_dc_vrp_serial_cfg_000301) describes the indexing modes of different synchronous serial interfaces.

**Table 1** Indexing modes of synchronous serial interfaces
| Physical Interface | Indexing Mode |
| --- | --- |
| E1 interface | **serial** *controller-number*:*set-number* or **serial** *controller-number*:**0** |
| CPOS interface | **serial** *cpos-number*/*e1-number*:*set-number* or **serial** *cpos-number*/*e1-number*:**0** |



#### Supported Serial Interface Features

The serial interfaces on the device support the following features:

* Use ATM, HDLC, PPP or TDM as the link layer protocol.
* Support IP network layer protocols.
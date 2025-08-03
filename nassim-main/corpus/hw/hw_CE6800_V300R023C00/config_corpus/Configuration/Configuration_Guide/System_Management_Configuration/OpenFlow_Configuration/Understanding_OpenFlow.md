Understanding OpenFlow
======================

Understanding OpenFlow

#### OpenFlow System Architecture

OpenFlow separates the control and data planes, serves a standard communication protocol between them, and allows the data plane to implement flow-based forwarding. [Figure 1](#EN-US_CONCEPT_0000001563750121__fig_1) shows the OpenFlow system architecture, which consists of the controller, OpenFlow devices, and OpenFlow protocol.

**Figure 1** OpenFlow system architecture  
![](figure/en-us_image_0000001564109837.png)

**Controller**

A server residing at the OpenFlow control plane, which creates and maintains flow tables.

**OpenFlow Device**

There are two types of OpenFlow devices:

* Dedicated OpenFlow device: a standard OpenFlow device that supports only OpenFlow forwarding.
* OpenFlow-compatible device: a device supporting OpenFlow forwarding in addition to Layer 2 and Layer 3 data forwarding. Huawei CE series switches are OpenFlow-compatible switches.

**OpenFlow Agent**

This is an OpenFlow management component on the OpenFlow device. The OpenFlow agent sets up OpenFlow connections with the controller. It then reports the interface information of the OpenFlow device.


#### OpenFlow Working Mechanism

The controller controls and manages devices using the OpenFlow protocol. The controller and device establish an OpenFlow channel, through which they exchange information. If one device establishes OpenFlow connections with multiple controllers, the controllers notify the device of their roles through the OpenFlow channels.

**OpenFlow Channel Establishment and Maintenance**

The controller and device need to establish an OpenFlow channel before they can exchange information. After the channel is established, it needs to be maintained to ensure stability. The establishment and maintenance process of an OpenFlow channel is as follows:

1. After the OpenFlow connection parameters are configured on the controller and device, the controller and device establish a TCP connection.
2. The controller and device exchange HELLO packets carrying information such as the OpenFlow protocol version through the TCP connection to negotiate the OpenFlow channel parameters.
3. After the OpenFlow channel parameters are negotiated, the controller sends a FEATURES\_REQUEST packet to request the device's attributes. The device responds with a FEATURES\_REPLY packet carrying its attributes. The OpenFlow channel is then established.
4. The controller and device exchange ECHO packets to detect peer device status. ECHO packets include ECHO\_REQUEST and ECHO\_REPLY packets. The detection initiator periodically sends ECHO\_REQUEST packets, and the peer responds with ECHO\_REPLY packets.
   
   If the initiator does not receive any ECHO\_REPLY packet after sending five consecutive ECHO\_REQUEST packets, the initiator considers the peer device failed and closes the OpenFlow connection. If the initiator receives a packet (except ECHO\_REPLY) before closing the OpenFlow connection, it restarts the counter.

**Figure 2** OpenFlow channel establishment and maintenance  
![](figure/en-us_image_0000001563989997.png)

**Controller Role Notification**

A device can connect to one or more controllers through OpenFlow connections. Establishing OpenFlow connections to multiple controllers improves reliability and implements load balancing. If one controller is faulty or an OpenFlow connection fails, the device is still connected to the other controllers and works normally.

A device must set up an OpenFlow connection with every configured controller and maintain connectivity. After OpenFlow channels are set up, the controllers actively send ROLE\_REQUEST packets carrying controller roles to the device. The controller roles include EQUAL, MASTER, and SLAVE.

* When the ROLE\_REQUEST packet contains OFPCR\_ROLE\_EQUAL, the controller is determined as the EQUAL. The EQUAL controller has the highest operating permissions on the device and can receive synchronization information from the device. This controller can send the forwarding information database and Packet-out packets to the device. By default, the role of the controller is EQUAL when it sets up a connection with a device.
* When the ROLE\_REQUEST message contains OFPCR\_ROLE\_MASTER, the controller is determined as the MASTER. The MASTER has the same permissions as EQUAL. If one MASTER exists, the other controllers can only be EQUAL or SLAVE.
* When the ROLE\_REQUEST packet contains OFPCR\_ROLE\_SLAVE, the controller is determined as the SLAVE. In this case, the controller has only read permission. The device does not send synchronization information to the controller or receive forwarding information databases or Packet-out packets from the slave device. If the device receives such information from the slave device, it discards the information and returns an OFPT\_ERROR message.

A controller determines its own role, and the controllers elect the MASTER. The device does not intervene with the MASTER or EQUAL controller election, and is informed of the controller role based on the ROLE\_REQUEST packet. The role notification process for the controller is as follows:

1. After the channel is established, the controller proactively sends a ROLE\_REQUEST packet to the device. After receiving the packet, the device returns a ROLE\_REPLY packet to the corresponding controller.
2. If a slave controller is elected as the MASTER controller, this controller sends a ROLE\_REQUEST(MASTER) packet to notify the device of its role change. The device records the new MASTER controller and replies with a ROLE\_REPLY packet. At the same time, the device sends a ROLE\_STATUS packet to the previous MASTER controller, requesting it to change its role to SLAVE.

**Figure 3** Controller role notification process  
![](figure/en-us_image_0000001512670618.png)

**Transparent Transmission of Packets**

The controller and device encapsulate packets into the Packet-in and Packet-out packets and transparently transmit them.

Packet-in: The device forwards information to the controller through Packet-in packets.

Packet-out: The controller delivers information to the device through Packet-out packets.
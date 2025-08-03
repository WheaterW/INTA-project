Configuring the MTU for an Ethernet Interface
=============================================

MTU is the largest packet of data that can be transmitted on a network, expressed in bytes. MTU is determined by data link layer protocols, and MTU values vary with networks. A proper MTU is a prerequisite for normal communication between network devices.

#### Context

The size of each data packet is limited at the network layer. Whenever receiving an IP packet, the IP layer determines the next-hop interface for the packet and obtains the MTU configured on the interface. Then, the IP layer compares the MTU with the packet length. If the packet length is longer than the MTU, the IP layer fragments the packet into smaller packets, which are shorter than or equal to the MTU.

If unfragmentation is configured, some packets may be discarded during data transmission at the IP layer. To ensure that jumbo packets are not dropped during transmission, set an MTU on an interface to fragment these packets into smaller ones.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If the size of packets is much greater than the configured MTU value, the packets are broken into a great number of fragments. The packets may be discarded by quality of service (QoS) queues.
* If the configured MTU value is too large, packets may be transmitted at a low speed.
* After changing the MTU of an Ethernet interface, also change the MTU of the peer Ethernet interface to ensure that the MTUs of both interfaces are the same. If the MTUs are different, services may be interrupted.

Perform the following steps on each Router:


#### Procedure

* Set an IPv4 MTU for an Ethernet interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
     
     
     
     The specified Ethernet interface view is displayed.
  3. Run [**mtu**](cmdqueryname=mtu) *mtu*
     
     
     
     An IPv4 MTU is set for the Ethernet interface.
     
     The MTU is expressed in bytes. The MTU value range of an Ethernet interface varies depending on the device.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an IPv6 MTU for an Ethernet interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
     
     
     
     The specified Ethernet interface view is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled on the Ethernet interface.
  4. Run [**ipv6 mtu**](cmdqueryname=ipv6+mtu) *mtu*
     
     
     
     An IPv6 MTU is set for the Ethernet interface.
     
     The MTU is expressed in bytes. The MTU value range of an Ethernet interface varies depending on the device.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

The length of a QoS queue is limited. If the size of packets is much greater than the configured MTU value, the packets are broken into a great number of fragments. The packets may be discarded by the QoS queue. To address this problem, you can increase the length of the QoS queue. The queue scheduling mechanism First In First Out (FIFO) is used on an interface by default. You can change the FIFO queue length. For detailed configuration of QoS queues, see *Configuration Guide - QoS*.
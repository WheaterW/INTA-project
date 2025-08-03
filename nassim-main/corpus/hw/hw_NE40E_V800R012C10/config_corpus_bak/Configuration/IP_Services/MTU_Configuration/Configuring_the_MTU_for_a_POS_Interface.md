Configuring the MTU for a POS Interface
=======================================

The MTU is used to reassemble or fragment packets on a POS interface when packets are received or sent on the interface through the IP network protocol.

#### Context

A Router reassembles or fragments the received or sent packets based on the MTU.

The IP layer limits the length of each frame in a packet to be sent each time. Any time the IP layer receives an IP packet to be sent, it determines to which interface the packet should be delivered and obtains the MTU of the target interface. Then, the IP layer compares the MTU with the packet length. If the packet length is longer than the MTU, the IP layer fragments the packet. Each fragment is not longer than the MTU.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If the MTU is set too small and the size of packets is quite large, packets will be divided into too many fragments and be discarded by QoS queues.
* If the MTU is set too large, packet transmission will be slowed down.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After changing the MTU of an interface by running the [**mtu**](cmdqueryname=mtu) *mtu* command, restart the interface to validate the configuration by running the [**shutdown**](cmdqueryname=shutdown) and then [**undo shutdown**](cmdqueryname=undo+shutdown) commands.

Perform the following steps on the Routers:


#### Procedure

* Configure the IPv4 MTU.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
     
     
     
     The POS interface view is displayed.
  3. Run [**mtu**](cmdqueryname=mtu) *mtu*
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the IPv6 MTU.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
     
     
     
     The POS interface view is displayed.
  3. Run [**ipv6 mtu**](cmdqueryname=ipv6+mtu) *mtu*
     
     
     
     The IPv6 MTU is configured for the POS interface.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     After configuring the IPv6 MTU, run the [**ppp mru-negotiate**](cmdqueryname=ppp+mru-negotiate) **ipv6** command to start negotiation of the IPv6 MTU.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
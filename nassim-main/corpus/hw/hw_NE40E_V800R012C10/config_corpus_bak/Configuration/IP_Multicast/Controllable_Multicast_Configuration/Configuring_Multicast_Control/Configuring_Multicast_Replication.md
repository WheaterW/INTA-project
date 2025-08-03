Configuring Multicast Replication
=================================

This section describes how to configure multicast replication. The NE40E uses a configured multicast replication method to copy multicast packets to its downstream Layer 2 devices.

#### Context

You can configure all the multicast replication methods, which are listed in descending order of priority. Broadband access server (BAS) interfaces support multicast replication by:

1. Replication by interface + VLAN
2. Replication by session
3. Replication by multicast VLAN
4. Replication by interface

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before you enable multicast replication on a BAS interface, you must enable the Internet Group Management Protocol (IGMP) on the interface by running the command [**igmp enable**](cmdqueryname=igmp+enable).

This configuration process is supported only on the Admin-VS.



#### Procedure

* Configure multicast replication by interface+VLAN.
  
  
  
  If multiple IP over X (IPoX) users order the same program from the same VLAN on an interface and IGMP snooping is enabled on the NE40E's downstream Layer 2 device, configure multicast replication by interface+VLAN to reduce the NE40E's copy burden. After the configuration is complete, the NE40E copies only one multicast packet to this interface. The interface copies the packet to its directly connected Layer 2 device. The downstream Layer 2 device then copies the packet to the IPoX users.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number*
     
     
     
     The sub-interface view is displayed.
  3. Run [**bas**](cmdqueryname=bas)
     
     
     
     A BAS interface is created, and the BAS interface view is displayed.
  4. Run [**multicast copy by-vlan**](cmdqueryname=multicast+copy+by-vlan)
     
     
     
     Multicast replication by interface+VLAN is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Only Ethernet, GE, Eth-Trunk's sub-interfaces support multicast replication by interface+VLAN.
     + If you run the [**multicast copy by-vlan**](cmdqueryname=multicast+copy+by-vlan) or [**undo multicast copy by-vlan**](cmdqueryname=undo+multicast+copy+by-vlan) command on an interface, the IPoX users who have gone online from the interface automatically leave the multicast group. As a result, the users' services are interrupted. The users join the multicast group only after they reorder a program.
     + Multicast replication by interface+VLAN is mutually exclusive with IGMPv3, which can be configured using the [**igmp version 3**](cmdqueryname=igmp+version+3) command.
* Configure multicast replication by user session.
  
  
  
  If the Router's downstream Layer 2 device does not provide IGMP snooping for user identification, configure multicast replication by user session on the Router's interface connected to the downstream Layer 2 device. After the configuration is complete, the Router directly copies multicast packets to each user.
  
  Because the Router's downstream Layer 2 device cannot parse Point-to-Point Protocol over Ethernet (PPPoE) sessions, you must configure multicast replication by user session on the Router's interface for PPPoE users.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**bas**](cmdqueryname=bas)
     
     
     
     A BAS interface is created, and the BAS interface view is displayed.
  4. Run [**multicast copy by-session**](cmdqueryname=multicast+copy+by-session)
     
     
     
     Multicast replication by user session is configured.
* Configure multicast replication by user aggregation.
  
  
  
  To isolate multicast packets from other types of packets and ensure multicast packet security, configure multicast replication by user aggregation. After the configuration is complete, multicast packets are aggregated and transmitted over an aggregation VLAN to reduce bandwidth consumption.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**multicast user-aggregation**](cmdqueryname=multicast+user-aggregation) [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     Multicast replication by user aggregation is configured.
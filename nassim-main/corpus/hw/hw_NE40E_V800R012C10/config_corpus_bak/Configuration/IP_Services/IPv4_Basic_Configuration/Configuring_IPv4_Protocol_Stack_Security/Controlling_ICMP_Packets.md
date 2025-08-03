Controlling ICMP Packets
========================

By controlling the sending and receiving of ICMP packets, you can effectively defend against attacks by sending these packets.

#### Context

In the case of heavy traffic on a network, if hosts or ports frequently become unreachable, routers receive a large number of ICMP packets. As a result, the network is more heavily burdened, and router performance deteriorates. In addition, most attackers use ICMP packets to launch attacks, such as sending a large number of packets with the TTL value 1, packets carrying options, and ICMP packets whose destination addresses are broadcast addresses.

Perform the following configurations to reduce traffic burdens over the network and defend against ICMP packet attacks:


#### Procedure

* Control the sending and receiving of ICMP packets in the system view.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**undo icmp receive**](cmdqueryname=undo+icmp+receive) or [**undo icmp send**](cmdqueryname=undo+icmp+send)
     
     The system is disabled from receiving or sending ICMP packets.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To restore the default configuration and ensure that the [**display this**](cmdqueryname=display+this) command output does not contain the [**undo icmp receive**](cmdqueryname=undo+icmp+receive) or [**undo icmp send**](cmdqueryname=undo+icmp+send) command configuration, run the [**clear icmp receive**](cmdqueryname=clear+icmp+receive) or [**clear icmp send**](cmdqueryname=clear+icmp+send) command.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Control the source IP address of ICMP Port Unreachable or Time Exceeded messages in the loopback interface view.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
     
     The loopback interface view is displayed.
  3. Run [**ip icmp**](cmdqueryname=ip+icmp+ttl-exceeded+port-unreachable+source-address) { **ttl-exceeded** | **port-unreachable** } **source-address**
     
     The source IP address of ICMP Port Unreachable or Time Exceeded messages is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
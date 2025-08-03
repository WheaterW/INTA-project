Optimizing DCN Routes
=====================

To improve DCN performance, configure OSPF functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**dcn (interface view)**](cmdqueryname=dcn+%28interface+view%29) or [**dcn mode vlan**](cmdqueryname=dcn+mode+vlan)
   
   
   
   DCN is enabled on the interface or sub-interface 4094.
4. Perform one or more of the following operations to configure OSPF functions.
   
   
   * Set an interval for sending Hello packets.
     
     Run the [**dcn ospf timer hello**](cmdqueryname=dcn+ospf+timer+hello) *interval* command to set an interval for sending Hello packets.
   * Set an interval for retransmitting LSAs to a neighboring Router.
     
     Run the [**dcn ospf timer retransmit**](cmdqueryname=dcn+ospf+timer+retransmit) *interval* command to set an interval for retransmitting LSAs to a neighboring Router.
   * Set an LSA transmission delay on an interface.
     
     Run the [**dcn ospf trans-delay**](cmdqueryname=dcn+ospf+trans-delay) *interval* command to set an LSA transmission delay on an interface.
   * Set a dead interval for a neighboring Router.
     
     Run the [**dcn ospf timer dead**](cmdqueryname=dcn+ospf+timer+dead) *interval* command to set a dead interval for a neighboring Router.
     
     If an interface does not receive Hello packets from an OSPF neighbor within the specified interval, the interface considers the neighbor Down. This interval is called an OSPF neighbor dead interval.
   * Set an interval for sending polling packets on a non-broadcast multiple access (NBMA) network.
     
     Run the [**dcn ospf timer poll**](cmdqueryname=dcn+ospf+timer+poll) *interval* command to set an interval for sending polling packets on an NBMA interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
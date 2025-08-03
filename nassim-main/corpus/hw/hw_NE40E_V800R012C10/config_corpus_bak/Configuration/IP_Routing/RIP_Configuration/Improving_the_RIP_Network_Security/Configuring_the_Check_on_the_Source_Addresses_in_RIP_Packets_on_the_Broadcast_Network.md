Configuring the Check on the Source Addresses in RIP Packets on the Broadcast Network
=====================================================================================

By default, a RIP interface checks the source address in each received packet and accepts only those from the same network.

#### Context

By default, RIP interfaces check the source addresses in received packets, which improves network security. If the source address of a received RIP packet is on a network segment different from that of the local interface IP address, the local interface discards the packet.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**rip**](cmdqueryname=rip) [ *process-id*] command to create a RIP process and enter the RIP view.
3. Run the [**verify-source**](cmdqueryname=verify-source) command to configure the check on the source addresses in RIP packets on the broadcast network.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
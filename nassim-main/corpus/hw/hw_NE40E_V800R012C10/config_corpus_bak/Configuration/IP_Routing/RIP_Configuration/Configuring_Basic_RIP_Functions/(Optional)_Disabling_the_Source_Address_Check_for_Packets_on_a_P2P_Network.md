(Optional) Disabling the Source Address Check for Packets on a P2P Network
==========================================================================

On a P2P network, the IP addresses of the two ends of a link can belong to different networks. In this case, the two ends can accept packets from each other only if the source address check is disabled.

#### Context

By default, a RIP interface checks the source address in each received packet and accepts only those from the same network. When the IP addresses of the two ends of a P2P link belong to different networks, the two ends can establish a neighbor relationship only if the source address check is disabled.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**rip**](cmdqueryname=rip) [ *process-id*] command to create a RIP process and enter the RIP view.
3. Run the [**undo verify-source**](cmdqueryname=undo+verify-source) command to disable source address check for RIP packets.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
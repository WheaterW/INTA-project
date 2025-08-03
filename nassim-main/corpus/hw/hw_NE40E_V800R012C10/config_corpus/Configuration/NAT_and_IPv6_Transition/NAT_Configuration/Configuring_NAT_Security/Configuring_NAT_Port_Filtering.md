Configuring NAT Port Filtering
==============================

To maintain network security and prevent virus intrusion, deploy the port filtering function for NAT services. The function prevents a port from being converted into a filtered port after NAT. Without this function, packets fail to be forwarded.

#### Context

The centralized NAT deployment scenario is used as an example. The port filter function is configured on two network interfaces of the NAT device to filter out packets with destination port 1434 (Worm.NetKiller2003). When a packet from the public network side reaches the private network side, the NAT device checks the packet's destination port. If the port is within the filtered port range, the device discards the packet. After NAT services are deployed on the private network side, a filtered port on the NAT device may be used as the post-NAT source port of a packet sent from the private network side to the public network side. After receiving a return packet, the NAT device finds that the packet's destination port is within the filtered port range and discards the packet, impacting user services. To resolve this issue, deploy the port filtering function for NAT services to filter out the filtered ports on the NAT device. This prevents returned user packets from being discarded by the NAT device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ [**id**](cmdqueryname=id) *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**exclude-port**](cmdqueryname=exclude-port) { *start-port* [ [**to**](cmdqueryname=to) *end-port* ] } & <1â10>
   
   
   
   The NAT port filtering function is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
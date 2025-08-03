Associating an IP Address Pool with a DHCPv4 Server Group
=========================================================

Only remote IP address pools need to be associated with DHCPv4 server groups.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* **bas** **remote**
   
   
   
   The remote address pool view is displayed.
3. Run [**dhcp-server group**](cmdqueryname=dhcp-server+group) *group-name*
   
   
   
   The address pool is associated with a DHCPv4 server group.
4. (Optional) Run [**remote-ip lease manage**](cmdqueryname=remote-ip+lease+manage)
   
   
   
   The lease management function is enabled for the remote address pool.
   
   
   
   If some clients do not respond to ARP probe packets sent by the Router, ARP probe is disabled on access interfaces on the Router. In this case, if a client is powered off or goes offline unexpectedly, the Router cannot detect that the offline event, because the client does not send any Release packet. As a result, the IP address used by the user cannot be released from the remote address pool. To prevent this problem, enable the lease management function for the remote address pool.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If destination IP addresses of lease packets sent by a DHCP server to users are user IP addresses instead of gateway IP addresses, do not enable the lease management function for the remote address pool. Because the Router directly forwards these packets to users without updating the leases, users will go offline after the leases expire.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
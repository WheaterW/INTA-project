Configuring RUI in Exclusive Address Pool Mode
==============================================

In exclusive address pool mode, each RBP is bound to an address pool to control the advertisement and withdrawal of network segment routes of the address pool.

#### Context

In exclusive address pool mode, an address pool is configured for each physical interface and bound to an RBP.

Perform the following steps on the devices that back up each other:


#### Procedure

1. Configure address pools on the master and backup devices.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* [ **bas** { **local** | **remote** } **rui-slave** ]
      
      
      
      An address pool is configured, and its view is displayed.
      
      
      
      A local primary address pool and a local RUI-slave address pool must be configured on both the master and backup devices.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The Router allows a third device to function as a remote DHCP server to allocate addresses to users logging in to the master and backup devices. In this case, you need to configure a remote address pool on the master device and a remote RUI-slave address pool on the backup device. The address pools must be associated with the DHCP server group on the remote DHCP server.
   3. Run [**gateway**](cmdqueryname=gateway) *ip-address* { **mask-length** | **mask** }
      
      
      
      A gateway address is configured for each address pool.
      
      The gateway address and subnet mask are used to check whether an address is on the same subnet as the gateway. Therefore, you must configure the gateway address and mask before configuring address segments.
   4. Run [**section**](cmdqueryname=section) *section-number* *start-ip-address* [ *end-ip-address* ]
      
      
      
      An address segment is configured for each address pool.
      
      
      
      If both the master and backup devices have two address pools configured, the address pools on each device must use different address segments. In addition, the primary address pool on the master device and the secondary address pool on the backup device share the same address segment, so do the secondary address pool on the master device and the primary address pool on the backup device. This prevents address conflicts if an master/backup device switchover occurs in a load balancing scenario.
   5. (Optional) Run [**dhcp-server group**](cmdqueryname=dhcp-server+group) *group-name*
      
      
      
      A remote DHCP server group is associated with the specified address pool.
      
      
      
      The remote DHCP server group associated with the secondary address pool on the backup device must be mapped to the master device. In a load balancing scenario, the remote DHCP server group associated with the secondary address pool on the master device must also be mapped to the backup device.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Bind an address pool to the RBP.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run **[**remote-backup-profile**](cmdqueryname=remote-backup-profile)** **profile-name**
      
      
      
      The RBP view is displayed.
   3. (Optional) Run [**ip-pool**](cmdqueryname=ip-pool) [ [**pool-group**](cmdqueryname=pool-group) ] *source-name* **include** [ [**pool-group**](cmdqueryname=pool-group) ] *destination-name* [ **node** *node-id* ]
      
      
      
      Address pool name mapping in the RBP is configured.
      
      
      
      A source address pool can be mapped to multiple target address pools in descending order by *node-id*, which means that the mapping starts from the target address pool with the largest *node-id*.
      
      If a remote DHCP server takes precedence over a local address pool in address allocation, the secondary address pool must have a higher priority than the primary address pool. However, if a local address pool takes precedence over a remote DHCP server, the primary address pool must have a higher priority than the secondary address pool.
   4. Run [**ip-pool**](cmdqueryname=ip-pool) *pool-name*
      
      
      
      An address pool is configured.
      
      
      
      The name of the address pool is specified by *destination-name* in the preceding step.
   5. (Optional) Run [**frame-route metric**](cmdqueryname=frame-route+metric) *metric-num*
      
      
      
      The preference of a route used by the RADIUS server to deliver an IP address is configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This step applies only to PPP private line users.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
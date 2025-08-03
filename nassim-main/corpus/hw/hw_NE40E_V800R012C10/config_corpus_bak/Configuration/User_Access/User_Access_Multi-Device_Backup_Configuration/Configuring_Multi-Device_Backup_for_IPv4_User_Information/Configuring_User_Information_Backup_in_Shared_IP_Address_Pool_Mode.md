Configuring User Information Backup in Shared IP Address Pool Mode
==================================================================

In shared address pool mode, links need to be added, and the networking mode is flexible.

#### Context

If the exclusive address pool mode is used, a great number of address pools are needed. This wastes addresses. To resolve the preceding issue, a shared address pool needs to be deployed. When a shared address pool is deployed, the following requirements must be met:

* The address pool cannot be bound to a remote backup profile (RBP).
* Both the master and backup devices need to be configured with the route control function to advertise address pool subnet routes so that the address pool subnet routes advertised by the master device have a higher priority. This prevents load balancing between network-side devices.
* A protection tunnel (for example, an LSP) must be established between the master and backup devices. If a user's uplink fails, the user's downlink traffic will be switched to the protection tunnel.
* The primary and secondary address pools need to be bound to the RBS using the [**ip-pool**](cmdqueryname=ip-pool) *pool-name* command in the RBS view. This ensures that network-side traffic can be forwarded through the protection tunnel before host routes are generated.

Perform the following steps on the devices that back up each other:


#### Procedure

* Configure address pools on the master and backup devices.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* [ **bas** { **local** | **remote** } **rui-slave** ]
     
     
     
     An address pool is created, and its view is displayed.
     
     
     
     A primary address pool (by specifying **local**) and a secondary address pool (by specifying **rui-slave**(**local** **rui-slave**)) must be configured on both the master and backup devices.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The Router allows a third device to function as a remote DHCP server to allocate addresses to users logging in to the master and backup devices. In this case, you need to configure a remote address pool on the master device and a remote RUI-slave address pool on the backup device. The address pools must be associated with the DHCP server group on the remote DHCP server.
  3. Run [**gateway**](cmdqueryname=gateway) *ip-address* { **mask-length** | **mask** }
     
     
     
     The gateway address of the address pool is configured.
     
     
     
     The gateway address and subnet mask are used to verify if an address in the configured address segment resides on the same subnet as the gateway. Therefore, you must configure the gateway address and mask before configuring address segments.
  4. Run [**section**](cmdqueryname=section) *section-number* *start-ip-address* [ *end-ip-address* ]
     
     
     
     The address segment is configured for the address pool.
     
     
     
     If both the master and backup devices have two address pools configured, the address pools on each device must use different address segments. In addition, the primary address pool on the master device and the secondary address pool on the backup device share the same address segment, so do the secondary address pool on the master device and the primary address pool on the backup device. This prevents address conflicts if an master/backup device switchover occurs in a load balancing scenario.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) After the address pool type is set to **rui-slave** (by specifying **local** **rui-slave**):
     + You can perform the following steps to configure parameters related to the remote DHCP server.
     + If an RUI-slave address pool configured by specifying **local** **rui-slave** is bound to an RBS, the address pool automatically uses the peer IP address configured in the RBS as a DHCP server IP address.
     
     Before performing the following steps, run the [**dhcp-server group**](cmdqueryname=dhcp-server+group) *group-name* **remote-backup-service** *rbs-name* command in the system view to specify the name of a DHCP server group and the RBS to be associated with the DHCP server group.
* Configure a protection path in IP redirection mode for public network users.
  
  
  
  Before configuring a protection path in IP redirection mode, ensure that a direct link has been deployed between the devices that back up each other.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name* command to enter the RBS view.
  3. Run the [**protect**](cmdqueryname=protect) **redirect** **ip-nexthop** *ip-address* **interface** { **interface-name** | *interface-type* *interface-num* } command to configure a protection path in IP redirection mode for public network users, with the peer IP address and the local outbound interface specified.
  4. Run either of the following commands to bind the primary address pool or an address pool group to the RBS:
     
     
     + To bind the primary address pool to the RBS, run the [**ip-pool**](cmdqueryname=ip-pool) *pool-name* command.
     + To bind an address pool group to the RBS, run the [**ip-pool-group**](cmdqueryname=ip-pool-group) *pool-group-name* [ **metric** *metric-name* ] command.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a protection path in tunnel mode for public network users.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name* command to enter the RBS view.
  3. Run the [**protect**](cmdqueryname=protect) **tnl-policy** *policy-name* **peer-ip** *ip-address* [ **interface** *interface-type* *interface-number* ] command to configure a protection path for public network users as an LSP, MPLS TE tunnel, or GRE tunnel. The tunnel type is specified through the tunnel policy, and the outbound interface is optional.
  4. Run either of the following commands to bind the primary address pool or an address pool group to the RBS:
     
     
     + To bind the primary address pool to the RBS, run the [**ip-pool**](cmdqueryname=ip-pool) *pool-name* command.
     + To bind an address pool group to the RBS, run the [**ip-pool-group**](cmdqueryname=ip-pool-group) *pool-group-name* [ **metric** *metric-name* ] command.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a protection path for VPN users.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name* command to enter the RBS view.
  3. Run the [**protect**](cmdqueryname=protect) **ip-vpn-instance** *vpn-instance-name* **peer-ip** *ip-address* [ **interface** *interface-type* *interface-number* ] command to configure a protection tunnel for VPN users, with the VPN instance name specified. **peer-ip** specifies the IP address of the loopback interface bound to the VPN instance on the peer end. The tunnel type cannot be specified. Instead, it is automatically selected by the device. The outbound interface is optional.
  4. Run either of the following commands to bind the primary address pool or an address pool group to the RBS:
     
     
     + To bind the primary address pool to the RBS, run the [**ip-pool**](cmdqueryname=ip-pool) *pool-name* command.
     + To bind an address pool group to the RBS, run the [**ip-pool-group**](cmdqueryname=ip-pool-group) *pool-group-name* [ **metric** *metric-name* ] command.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a protection tunnel template for the public and private networks.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name* command to enter the RBS view.
  3. Either of the following methods can be used:
     
     
     + To configure a protection tunnel template in MPLS LSP mode, run the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) *ip-address* command.
     + To configure a protection tunnel template in SRv6 TE Policy mode, run the [**protect srv6 tunnel-policy**](cmdqueryname=protect+srv6+tunnel-policy) *policy-name* **endpoint** *ipv6-address* **color** *color-number* command after a tunnel policy is created using the [**tunnel-policy**](cmdqueryname=tunnel-policy) command.
  4. Run either of the following commands to bind the primary address pool or an address pool group to the RBS:
     
     
     + To bind the primary address pool to the RBS, run the [**ip-pool**](cmdqueryname=ip-pool) *pool-name* command.
     + To bind an address pool group to the RBS, run the [**ip-pool-group**](cmdqueryname=ip-pool-group) *pool-group-name* [ **metric** *metric-name* ] command.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A protection tunnel template can be configured concurrently for both a private network and a public network. After the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) command is run, a protection tunnel for a public network is directly created, and a protection tunnel for private networks is triggered by user login. This eliminates the need for configuring a protection tunnel for each private network, simplifying tunnel configuration.
  
  To specifically create a protection tunnel for a public network, run the [**protect**](cmdqueryname=protect) **tnl-policy** *policy-name* **peer-ip** *ip-address* [ **interface** *interface-type* *interface-number* ] command. To specifically create a protection tunnel for a private network, run the [**protect**](cmdqueryname=protect) **ip-vpn-instance** *vpn-instance-name* **peer-ip** *ip-address* [ **interface** *interface-type* *interface-number* ] command. If one protection path is deployed using the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) command and the other protection path is deployed specifically for a private or public network, the former protection path has a higher priority, and the corresponding configuration takes effect.
  
  If both the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) and [**protect srv6 tunnel-policy**](cmdqueryname=protect+srv6+tunnel-policy) commands are configured on the device, the latter command takes effect and has the highest priority.
  
  Before running the [**protect srv6 tunnel-policy**](cmdqueryname=protect+srv6+tunnel-policy) command, you need to run the [**tunnel-policy**](cmdqueryname=tunnel-policy) command on the network side to create a tunnel policy. For details, see the [SRv6 TE Policy configuration (static configuration)](../vrp/dc_vrp_srv6_cfg_all_0110.html) in the product documentation.
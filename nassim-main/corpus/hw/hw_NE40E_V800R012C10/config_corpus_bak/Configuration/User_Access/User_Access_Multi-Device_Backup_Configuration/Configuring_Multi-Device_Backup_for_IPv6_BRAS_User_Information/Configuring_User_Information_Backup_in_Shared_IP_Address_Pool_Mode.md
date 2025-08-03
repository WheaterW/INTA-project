Configuring User Information Backup in Shared IP Address Pool Mode
==================================================================

In shared address pool mode, links need to be added, and the networking mode is flexible.

#### Context

If the exclusive address pool mode is used, a great number of address pools are needed. This wastes addresses. To resolve the preceding issue, a shared address pool needs to be deployed. When a shared address pool is deployed, the following requirements must be met:

* The address pool cannot be bound to an RBP.
* Both the master and backup devices need to advertise their network segment routes of address pools and be configured with a routing policy to ensure that the route advertised by the master device has a higher priority. This prevents load balancing on network-side devices.
* A protection tunnel (for example, an LSP) must be established between the master and backup devices. If a user's uplink fails, the user's downlink traffic will be switched to the protection tunnel.
* The primary address pool and the secondary address pool are bound to the RBS by running the [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name* [ **metric** *metric-value* ] command in the RBS view. This ensures that network-side traffic can be forwarded through the protection tunnel before host routes are generated.

Perform the following steps on the devices that back up each other:


#### Procedure

* Configure an IPv6 address pool for the master/backup device.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6**](cmdqueryname=ipv6) [**prefix**](cmdqueryname=prefix) *prefix-name* [ **local** | **delegation** | **remote** ]
     
     
     
     The IPv6 prefix pool is created, and its view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the IPv6 prefix pool view.
  4. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas { local | delegation | remote }** **[ rui-slave ]**
     
     
     
     A local address pool is created, and its view is displayed.
     
     
     
     A primary address pool (by specifying **local** | **delegation** | **remote**) and a secondary address pool (by specifying **rui-slave**(**local** **rui-slave**)) must be configured on both the master and backup devices.
  5. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
     
     
     
     A prefix is configured for the address pool.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the IPv6 address pool view.
* Configure a protection tunnel template for the public and private networks.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
     
     
     
     The RBS view is displayed.
  3. Either of the following methods can be used:
     
     
     + To configure a protection tunnel template in MPLS LSP mode, run the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) *ip-address* command.
     + To configure a protection tunnel template in SRv6 TE Policy mode, run the [**protect srv6 tunnel-policy**](cmdqueryname=protect+srv6+tunnel-policy) *policy-name* **endpoint** *ipv6-address* **color** *color-number* command after a tunnel policy is created using the [**tunnel-policy**](cmdqueryname=tunnel-policy) command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A protection tunnel template can be configured concurrently for both a private network and a public network. After the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) or [**protect srv6 tunnel-policy**](cmdqueryname=protect+srv6+tunnel-policy) command is run, a protection tunnel for a public network is directly created, and a protection tunnel for a private network is triggered by user login. This eliminates the need for configuring a protection tunnel for each private network, simplifying tunnel configuration. If both the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) and [**protect srv6 tunnel-policy**](cmdqueryname=protect+srv6+tunnel-policy) commands are configured on the device, the latter command takes effect and has the highest priority.
     
     To specifically create a protection tunnel for a public network, run the [**protect**](cmdqueryname=protect) **tnl-policy** *policy-name* **peer-ip** *ip-address* [ **interface** *interface-type* *interface-number* ] command. To specifically create a protection tunnel for a private network, run the [**protect**](cmdqueryname=protect) **ip-vpn-instance** *vpn-instance-name* **peer-ip** *ip-address* [ **interface** *interface-type* *interface-number* ] command. If one protection path is deployed using the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) command and the other protection path is deployed specifically for a private or public network, the protection path deployed using the [**protect lsp-tunnel for-all-instance peer-ip**](cmdqueryname=protect+lsp-tunnel+for-all-instance+peer-ip) command has a higher priority, and the corresponding configuration takes effect. Manual tunnel configuration takes effect only for IPv4. IPv6 still uses simplified tunnels for forwarding.
  4. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name* [ **metric** *metric-value* ]
     
     
     
     The primary address pool is bound to the RBS.
  5. (Optional) Run [**dhcpv6-server destination**](cmdqueryname=dhcpv6-server+destination) *destination-ipv6-address* **source** *source-ipv6-address* [ **vpn-instance** *vpn-instance* ]
     
     
     
     Inter-chassis borrowing of IPv6 addresses is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
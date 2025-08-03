Configuring a Remote IPv6 Prefix Pool
=====================================

When the NE40E functions as a DHCPv6 relay agent, a remote IPv6 prefix pool must be configured to manage the prefixes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* **remote**
   
   
   
   A remote IPv6 prefix pool is created, and the IPv6 prefix pool view is displayed.
3. Run [**link-address**](cmdqueryname=link-address) *ipv6-address*/*prefix-length*
   
   
   
   The link-local address is configured.
   
   
   
   When the remote server allocates addresses or prefixes, link-local addresses must be configured on the relay.
4. (Optional) Run the [**lock**](cmdqueryname=lock) command to lock an IPv6 prefix pool.
   
   
   
   After this command is run, no prefix in the locked prefix pool can be assigned, preventing new users from going online using prefixes in the prefix pool.
   
   This method is typically used when a prefix pool cannot be deleted because its prefixes are in use by online users. You can lock the prefix pool first to stop it from assigning prefixes. After all users go offline, the prefixes in the prefix pool are all released, and the prefix pool can then be deleted.
5. (Optional) Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to bind a VPN instance to the prefix pool.
6. Run [**remote-ip lease manage**](cmdqueryname=remote-ip+lease+manage)
   
   
   
   The lease management function is enabled for the remote IPv6 prefix pool.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
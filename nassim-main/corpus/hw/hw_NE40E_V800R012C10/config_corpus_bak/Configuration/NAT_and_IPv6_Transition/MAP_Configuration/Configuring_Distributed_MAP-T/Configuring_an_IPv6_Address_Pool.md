Configuring an IPv6 Address Pool
================================

In a distributed MAP-T scenario, a prefix pool, a DMR prefix, and an FMR flag bit need to be configured in an IPv6 delegation address pool. An IPv6 prefix pool can be configured in either delegation or remote mode. Configuring an IPv6 remote address pool includes binding a prefix pool to the address pool and configuring route advertisement information for the address pool.

#### Procedure

* Configure an IPv6 delegation address pool.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas delegation**
     
     
     
     An IPv6 delegation address pool is created, and its view is displayed.
  3. Run [**option-s46 dmr-prefix**](cmdqueryname=option-s46+dmr-prefix) *dmr-prefix-name*
     
     
     
     A DMR prefix name is bound to the IPv6 address pool. The HUAWEI NE40E-M2 series encapsulates the IPv6 prefix as Option 91 information (OPTION\_S46\_DMR) into the DHCPv6 Response message sent to MAP-T users.
  4. (Optional) Run [**option-s46 fmr-flag disable**](cmdqueryname=option-s46+fmr-flag+disable)
     
     
     
     The F-flag bit is set to 0 in DHCPv6 OPTION\_S46\_RULE (option 89).
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an IPv6 remote address pool.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only PPPoE users can go online using IPv6 remote address pools.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run the following commands to configure a DHCPv6 server group:
     
     
     1. Run [**dhcpv6-server group**](cmdqueryname=dhcpv6-server+group) *group-name*
        
        A DHCPv6 server group is created, and its view is displayed.
     2. Run [**dhcpv6-server**](cmdqueryname=dhcpv6-server) { **destination** *ipv6-address* [ **vpn-instance** *vpn-instance* ] | **interface** *interface-type**interface-number* } [ **weight** *weight-value* ]
        
        An IPv6 address or outbound interface is configured for the DHCPv6 server.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas remote**
     
     
     
     An IPv6 remote address pool is created, and its view is displayed.
  5. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
     
     
     
     An IPv6 prefix pool is bound to the IPv6 address pool.
  6. Run [**export host-route**](cmdqueryname=export+host-route)
     
     
     
     Routes in the address pool are advertised.
  7. Run [**dhcpv6-server group**](cmdqueryname=dhcpv6-server+group) *group-name*
     
     
     
     The remote address pool is associated with the created DHCPv6 server group.
     
     
     
     Associating an IPv6 address pool with a DHCPv6 server group is required only when the IPv6 remote address pool is used.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  9. Run [**access map-t support pool-type remote user-type pppoe**](cmdqueryname=access+map-t+support+pool-type+remote+user-type+pppoe)
     
     
     
     PPPoE MAP-T users are enabled to go online from a remote address pool.
     
     
     
     In a MAP-T scenario, run this command in the system view to enable the DHCPv6 server to assign MAP prefixes and rules to PPPoE users.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
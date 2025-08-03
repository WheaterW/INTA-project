Binding an IPv6 Delegation Address Pool to a Domain
===================================================

After an IPv6 delegation address pool is bound to a domain, users in the domain can be assigned prefixes from the address pool.

#### Prerequisites

An IPv6 delegation address pool has been configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   A domain is created, and the AAA domain view is displayed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
   
   
   
   An IPv6 delegation address pool is bound to the domain.
6. (Optional) Run [**ipv6-warning-threshold**](cmdqueryname=ipv6-warning-threshold) { *upper-limit-value* | **lower-limit** *lower-limit-value* }
   
   
   
   A threshold for the usage of IPv6 addresses and prefixes is configured.
7. (Optional) Run [**prefix-assign-mode unshared**](cmdqueryname=prefix-assign-mode+unshared)
   
   
   
   The IPv6 prefix allocation mode is set to unshared. IPv6 users do not share the same IPv6 prefix.
8. (Optional) Configure different users of a home connected to the network through a hub to communicate with each other directly rather than through a BRAS.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You must run the [**dhcpv6-unshare-only**](cmdqueryname=dhcpv6-unshare-only) command in the IPv6 prefix pool view before performing this step.
   
   1. Run [**ipv6-address assign**](cmdqueryname=ipv6-address+assign) { **circuit-id** | **remote-id** } \*
      
      The device is configured to assign IPv6 addresses to users based on the Option 18 or Option 37 attribute.
   2. Run [**ipv6 nd ra link-prefix**](cmdqueryname=ipv6+nd+ra+link-prefix)
      
      The device is configured to send RA packets carrying the first 64 bits of the addresses assigned to IPv6 users as on-link prefixes.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
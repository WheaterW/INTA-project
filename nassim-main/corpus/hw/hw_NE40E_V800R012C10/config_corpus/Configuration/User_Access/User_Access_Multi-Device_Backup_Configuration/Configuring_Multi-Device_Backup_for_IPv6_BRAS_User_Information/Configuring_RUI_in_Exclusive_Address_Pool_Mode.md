Configuring RUI in Exclusive Address Pool Mode
==============================================

In exclusive address pool mode, each RBP is bound to an address pool to control the advertisement and withdrawal of network segment routes of the address pool.

#### Context

In exclusive address pool mode, an address pool is configured for each physical interface and bound to an RBP.

Perform the following steps on the devices that back up each other:


#### Procedure

* RADIUS-delivered address pool
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas local**
     
     
     
     A local IPv6 address pool is created and its view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**ipv6**](cmdqueryname=ipv6) [**prefix**](cmdqueryname=prefix) *prefix-name*
     
     
     
     The IPv6 prefix pool view is displayed and prefixes are configured in the IPv6 prefix pool.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
     
     
     
     The RBP view is displayed.
  7. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *source-pool-name* **include** *destination-pool-name* [ **node** *node-id* ]
     
     
     
     The address pool mapping is configured.
     
     
     
     *source-pool-name* specifies the name of the address pool delivered by the RADIUS server, and *destination-pool-name* specifies the local address pool configured in Step 2.
  8. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
     
     
     
     An address pool is configured.
     
     
     
     The name of the IPv6 address pool is specified by *destination-pool-name* in the preceding step.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Locally-configured address pool
  
  
  + Divide domains based on links and bind each domain to an address pool.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6**](cmdqueryname=ipv6) [**prefix**](cmdqueryname=prefix) *prefix-name* **local**
     
     
     
     A local prefix pool is configured.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the IPv6 prefix pool view.
  4. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas local**
     
     
     
     A local address pool is created and its view is displayed.
  5. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
     
     
     
     A prefix is configured for the address pool.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the IPv6 address pool view.
  7. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  8. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The AAA domain view is displayed.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  10. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
      
      
      
      The address pool is bound to the domain.
  11. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the AAA domain view.
  12. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the AAA view.
  13. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
  14. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
      
      
      
      An address pool is configured.
  15. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  + Map a source IPv6 address pool to a destination address pool.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas local**
     
     
     
     A local address pool is created.
  3. Run [**prefix**](cmdqueryname=prefix) *prefix-name*
     
     
     
     A prefix is configured for the address pool.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the address pool view.
  5. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  6. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The AAA domain view is displayed.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  8. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
     
     
     
     An address pool is bound to a domain.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the AAA domain view.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the AAA view.
  11. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
  12. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *source-pool-name* **include** *destination-pool-name* [ **node** *node-id* ]
      
      
      
      The address pool mapping is configured.
  13. Run [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name*
      
      
      
      An address pool is configured.
      
      The name of the address pool is specified by *destination-pool-name* in the preceding step.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
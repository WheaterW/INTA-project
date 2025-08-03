Configuring an Address Pool Group
=================================

An address pool group is a set of address pools sharing specified attributes. An address pool group simplifies configuration in some situations.

#### Context

An address pool group can be created if either of the following conditions is met:

* Multiple domains share some address pools.
* A RADIUS server is able to deliver address pool names.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool-group**](cmdqueryname=ip+pool-group) *group-name* **bas**
   
   
   
   An address pool group is created, and the address pool group view is displayed.
3. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
   
   
   
   An address pool group is bound to a VPN instance.
   
   The address pool group and its address pools must be bound to the same VPN instance.
   
   The address pool group in a domain and the domain must be bound to the same VPN instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. (Optional) Run [**ip-attribute public**](cmdqueryname=ip-attribute+public)
   
   
   
   The public network attribute is configured for an IP address pool or an IP address pool group. After the configuration is complete, the IP address pool or the IP address pool group is configured as a public IP address pool or pool group whose usage status is calculated.
   
   
   
   To use the [**ip-attribute public**](cmdqueryname=ip-attribute+public) command, you must also run the [**ip-pool usage-status threshold**](cmdqueryname=ip-pool+usage-status+threshold) command to configure the upper and lower thresholds for public IP address pool usage in a domain, so that the pool usage status to be sent to the RADIUS server can be calculated.
   
   The [**ip-attribute public**](cmdqueryname=ip-attribute+public) command takes effect only on local address pools.
6. Run [**ip-pool**](cmdqueryname=ip-pool) *pool-name*
   
   
   
   An address pool is added to an address pool group.
7. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. (Optional) Run [**warning-exhaust**](cmdqueryname=warning-exhaust)
   
   
   
   The address exhaustion alarm function is enabled for the address pool group.
   
   
   
   After this command is run, the system generates an address exhaustion alarm when IP addresses in the address pool group are exhausted, prompting the administrator to plan the IP addresses. When IP addresses in the address pool group are exhausted, users cannot go online.
   
   When IP address usage of the address pool group falls below 90%, the address exhaustion alarm is cleared.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

You can run the [**ip-pool-group**](cmdqueryname=ip-pool-group) *group-name* [ **move-to** *new-position* ] command in AAA domain view to bind an address pool group to a domain.
Configuring an MBGP Peer
========================

Valid routing information can be provided for the Reverse Path Forwarding (RPF) check only after a Multicast Border Gateway Protocol (MBGP) connection is enabled in the multicast address family view.

#### Usage Scenario

The RPF check is performed on multicast packets based on the following routes:

* Multicast static routes
* Unicast routes
* MBGP routes

Valid routing information can be provided for the RPF check only after an MBGP connection is enabled in the multicast address family view.


#### Pre-configuration Tasks

Before configuring basic MBGP functions, configure basic multicast functions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The IP address and autonomous system (AS) number of a remote peer are specified.
4. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **connect-interface** { *interface-type* *interface-number* | *ipv4-source-address* }
   
   
   
   The local interface and the source address used to set up a BGP connection are specified.
   
   
   
   If the BGP connection is set up through a Loopback interface or a sub-interface, this command must be configured.
5. (Optional) Run [**peer**](cmdqueryname=peer) { *ip-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops of an External Border Gateway Protocol (EBGP) connection is set.
   
   
   
   The command is valid only for EBGP peers.
   
   If the EBGP connection is set up through a Loopback interface, this command must be configured.
6. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
7. Run [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**enable**](cmdqueryname=enable)
   
   
   
   MBGP is enabled for a BGP peer or peer group, which then becomes an MBGP peer or peer group.
   
   
   
   * *group-name*: specifies the name of a BGP peer group.
   * *peer-address*: specifies the IP address of a remote BGP peer.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After the configuration is complete, verify the configuration.

Run the [**display bgp multicast peer**](cmdqueryname=display+bgp+multicast+peer) [ *peer-address* ] [ **verbose** ] command to check information about a specified or all MBGP peers.
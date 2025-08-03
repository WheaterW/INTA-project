Configuring MBGP RRs
====================

MBGP RRs resolve the problem of full-mesh connections between multiple IBGP peers, which reduces network costs.

#### Usage Scenario

Full-mesh connections need to be established between IBGP peers in an AS to ensure the connectivity between the IBGP peers. When there are many IBGP peers, it is costly to establish a fully-meshed network. An RR can be used to solve the problem.


#### Pre-configuration Tasks

Before configuring MBGP RRs, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

An RR takes effect only for IBGP peers. Before configuring an MBGP RR, establish an IBGP peer relationship between the RR and each of its clients.

This configuration is optional.

Perform the following steps on the Router to be configured as an MBGP RR:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } **reflect-client**
   
   
   
   The device is configured as an RR and its peer or peer group is configured as a client.
   
   
   
   * *group-name*: specifies the name of an MBGP peer group.
   * *peer-address*: specifies the IP address of a remote MBGP peer.
5. (Optional) Run [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* }
   
   
   
   A cluster ID is configured for the RR.
   
   
   
   * *cluster-id-value*: specifies a cluster ID in the decimal format.
   * *cluster-id-ipv4*: specifies a cluster ID in the format of an IPv4 address.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After the configuration is complete, verify the configuration.

* Run the [**display bgp multicast routing-table**](cmdqueryname=display+bgp+multicast+routing-table) command to check routes in the MBGP routing table.
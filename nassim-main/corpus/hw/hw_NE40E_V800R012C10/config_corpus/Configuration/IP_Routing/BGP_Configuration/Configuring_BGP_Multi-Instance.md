Configuring BGP Multi-Instance
==============================

You can configure BGP multi-instance to achieve separate route management and maintenance.

#### Usage Scenario

By default, all BGP routes are stored in the BGP base instance, and separate route management and maintenance are impossible. To address this problem, BGP multi-instance is introduced. A device can simultaneously run the BGP base instance and BGP multi-instance, which are independent of each other and can have either the same AS number or different AS numbers. You can deploy different address families for the BGP base instance and BGP multi-instance as required to implement separate route management and maintenance.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enable the VPN instance IPv4 address family and enter its view.
4. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance IPv4 address family.
5. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the VPN instance IPv4 address family.
6. Run the [**quit**](cmdqueryname=quit) command to enter the VPN instance view.
7. Run the [**quit**](cmdqueryname=quit) command to enter the system view.
8. Run the [**bgp**](cmdqueryname=bgp+instance) *as-number* **instance** *instance-name* command to enter the BGP multi-instance view.
9. (Optional) Run the **ipv4-family vpn-instance** *vpn-instance-name* command to enter the BGP multi-instance VPN instance IPv4 address family view.
10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* [**as-number**](cmdqueryname=as-number) *as-number* command to specify the IP address of a peer and the number of the AS where the peer resides.
    
    
    
    The IP address of the peer can be one of the following types:
    
    * IP address of the peer's interface that is directly connected to the local device
    * IP address of a sub-interface on the peer's interface that is directly connected to the local device
    * IP address of a reachable loopback interface on the peer
11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
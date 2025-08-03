Configuring BGP MVPN Peer Relationships
=======================================

Configuring BGP MVPN Peer Relationships

#### Context

In an IPv4 Layer 3 multicast over VXLAN scenario, all PEs functioning as VXLAN gateways must establish a BGP MVPN peer relationship between one another.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Specify a peer PE as a BGP peer.
   
   
   ```
   [peer](cmdqueryname=peer) ipv4-address as-number as-number
   ```
4. (Optional) Specify the source interface and source address used to establish a TCP connection with the BGP peer.
   
   
   ```
   [peer](cmdqueryname=peer) ipv4-address connect-interface interface-type interface-number [ ipv4-source-address ]
   ```
   
   If loopback interfaces are used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command on both ends to ensure proper connectivity. If this command is run on only one end, the BGP connection may fail to be established.
   
   If a physical interface is configured with multiple IP addresses, *ipv4-source-address* must be specified in the command.
5. (Optional) Set the maximum number of hops allowed over an EBGP connection.
   
   
   ```
   [peer](cmdqueryname=peer) ipv4-address [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
   ```
   
   By default, the value of *hop-count* is 255. In inter-AS NG MVPN scenarios, EBGP peer relationships must be established first. In most cases, EBGP peers are directly connected through a physical link. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed over the TCP connection.
   
   If loopback interfaces are used to establish an EBGP connection, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command, where the value of *hop-count* must be greater than or equal to 2. Otherwise, the EBGP peer relationship cannot be established.
6. Enter the BGP-MVPN address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family) mvpn
   ```
7. Specify the peer device as a BGP MVPN peer.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name } enable
   ```
8. (Optional) Disable the device from checking whether local A-D routes exist upon receiving C-multicast routes from its BGP MVPN peers.
   
   
   ```
   [c-multicast ad-route-ignore](cmdqueryname=c-multicast+ad-route-ignore)
   ```
   
   
   
   By default, the device checks whether local A-D routes exist when validating C-multicast routes received from its BGP MVPN peers.
   
   If different RD values are configured for the VPN instance IPv4 address families on the M-LAG active-active gateways of an inter-AS VXLAN network, one of the gateways considers received C-multicast routes invalid because the RD value carried in the C-multicast routes is different from that in a local A-D route. As a result, the M-LAG active-active function cannot take effect. To prevent this problem, perform this step on the two active-active gateways.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

Configure the following BGP functions in the BGP-MVPN address family view as required. For details, see [BGP Configuration](vrp_bgp_cfg_0001.html).

1. [Configure a BGP peer group](vrp_bgp_cfg_0031.html).
2. [Configure a BGP RR](vrp_bgp_cfg_0073.html).
3. [Set a BGP Update timer](vrp_bgp_cfg_0090.html).
4. [Configure Next\_Hop-related functions](vrp_bgp_cfg_0027.html). Among these functions, the BGP-MVPN address family view supports only the function that allows the device to use its own address as the next-hop address of routes when advertising them.
5. [Configure BGP community attributes](vrp_bgp_cfg_0081.html). Among these attributes, the BGP-MVPN address family view only supports the configuration that allows the device to advertise standard community attributes to its peers or peer groups.
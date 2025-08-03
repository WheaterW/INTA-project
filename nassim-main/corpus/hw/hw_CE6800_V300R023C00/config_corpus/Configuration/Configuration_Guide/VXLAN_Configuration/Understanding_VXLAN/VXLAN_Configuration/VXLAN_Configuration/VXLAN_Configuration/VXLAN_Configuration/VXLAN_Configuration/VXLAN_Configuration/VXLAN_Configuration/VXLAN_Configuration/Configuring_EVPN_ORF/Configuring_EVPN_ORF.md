Configuring EVPN ORF
====================

Configuring EVPN ORF

#### Context

The growing number of services run over an EVPN has triggered a proliferation of new users. As a result, BGP-EVPN peers on an EVPN are sending vast quantities of EVPN routes to each other. Even if the remote peer does not have an RT-matching EVPN instance, the local PE still sends EVPN routes to it. To reduce the pressure on the network, each PE needs to receive only desired routes. However, configuring a separate export route-policy for each user drives up O&M costs significantly. To address this issue, configure EVPN outbound route filtering (ORF) on the network.

After EVPN ORF is configured, each PE on the EVPN sends the IRT and original AS number of locally desired routes to the other PEs that function as EVPN peers or BGP EVPN RRs. Upon receipt of such information, which is sent through ORF routes, the peers construct export route-policies based on these routes. This ensures that the local PE receives only the desired routes, thereby reducing pressure on the PE.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-VPN-target address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family) vpn-target
   ```
4. Enable the function of exchanging ORF routes with a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+enable) { group-name | ipv4-address | ipv6-address }  enable
   ```
5. (Optional) Enable the RR function on the current device and configure the peer or peer group as the RR client.
   
   
   ```
   [peer](cmdqueryname=peer) { group-name | ipv4-address | ipv6-address } reflect-client
   ```
   
   On an EVPN where an RR is deployed, you also need to perform this step in the BGP-VPN-target address family view of the RR to enable the RR function for the address family.
6. Exit the BGP-VPN-target address family view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Enter the BGP-EVPN address family view.
   
   
   ```
   [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
   ```
8. Enable EVPN ORF.
   
   
   ```
   [vpn-orf enable](cmdqueryname=vpn-orf+enable)
   ```
9. (Optional) Disable EVPN ORF for a specified BGP EVPN peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+vpn-orf+disable) { group-name | ipv4-address | ipv6-address } vpn-orf disable
   ```
   
   
   
   On a network where both EVPN and L3VPN services are deployed, if a PE runs an earlier version and does not support EVPN ORF, this PE cannot exchange EVPN routes with the RRs after BGP-VPN-target peer relationships are established and EVPN ORF is enabled on other PEs and RRs. As a result, EVPN services cannot run properly. To ensure that EVPN services can run properly, run the [**peer vpn-orf disable**](cmdqueryname=peer+vpn-orf+disable) command. This command disables the RR from filtering IRT-related routes for the PE so that the PE can send and receive EVPN routes as expected.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display bgp vpn-target routing-table**](cmdqueryname=display+bgp+vpn-target+routing-table) command. The command output shows information about routes in the BGP-VPN-target address family.
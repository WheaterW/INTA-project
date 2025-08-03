Configuring BGP G-Shut
======================

After EBGP and IBGP sessions between ASBRs and BGP devices are shut down during maintenance, the ASBRs and BGP devices are temporarily unreachable to each other during BGP convergence. To minimize traffic loss during session closure and re-establishment, you can configure the g-shut function to gracefully shut down one or more BGP sessions.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable and activate BGP g-shut globally or for a specified peer as required.
   
   
   * Enable and activate BGP g-shut globally.
     1. Enable g-shut globally.
        ```
        [graceful-shutdown all-peer](cmdqueryname=graceful-shutdown+all-peer)
        ```
     2. Activate g-shut globally.
        ```
        [graceful-shutdown manual-activate](cmdqueryname=graceful-shutdown+manual-activate)
        ```
   
   
   * Enable and activate BGP g-shut for a peer.
     1. Enable g-shut for a peer or peer group.
        ```
        [peer](cmdqueryname=peer+graceful-shutdown+local-preference+as-prepend) { peerIpv4Addr | peerIpv6Addr | groupName } graceful-shutdown [ local-preference local-preference-value | as-prepend as-prepend-value ]
        ```
     2. Activate g-shut for a peer or peer group.
        ```
        [peer](cmdqueryname=peer+graceful-shutdown+manual-activate) { peerIpv4Addr | peerIpv6Addr | groupName } graceful-shutdown manual-activate
        ```
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        To enable and activate g-shut for peers in the BGP-VPN instance view, BGP-VPN instance IPv4 address family view, or BGP-VPN instance IPv6 address family view, enter the corresponding view before performing this step.
        
        If a peer group has been configured with g-shut but peer A in it does not need to inherit g-shut from the peer group, run the [**peer**](cmdqueryname=peer)  { *peerIpv4Addr* | *peerIpv6Addr* } **graceful-shutdown disable** command. To prevent this peer from inheriting the g-shut activation status from the peer group, run the [**peer**](cmdqueryname=peer) { *peerIpv4Addr* | *peerIpv6Addr* } **graceful-shutdown manual-activate disable** command.
4. (Optional) Configure the device to advertise the g-shut community attribute of the address family level.
   
   
   ```
   [advertise-community-gshut](cmdqueryname=advertise-community-gshut+ibgp+ebgp) { ibgp | ebgp }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure the device to advertise the g-shut community attribute in an address family view, enter the address family view before performing this step. Currently, the following address families are supported: BGP-IPv4 unicast address family view, BGP-IPv6 unicast address family view, BGP-EVPN address family view, BGP-VPN instance IPv4 address family view, and BGP-VPN instance IPv6 address family view.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
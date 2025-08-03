Configuring BGP G-Shut
======================

After EBGP and IBGP sessions between BGP devices are shut down during maintenance, the BGP devices are temporarily unreachable to each other during BGP convergence. To minimize traffic loss during session closure and re-establishment, you can configure the g-shut function to gracefully shut down one or more BGP sessions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Enable and activate BGP g-shut globally or for a specified peer as required.
   
   
   * Enable and activate BGP g-shut globally.
     1. Run the [**graceful-shutdown all-peer**](cmdqueryname=graceful-shutdown+all-peer) command to enable the g-shut function globally.
     2. Run the [**graceful-shutdown manual-activate**](cmdqueryname=graceful-shutdown+manual-activate) command to activate the g-shut function globally.
   * Enable and activate BGP g-shut for a peer.
     1. Run the [**peer**](cmdqueryname=peer+graceful-shutdown) { *peerIpv4Addr* | *groupName* } [**graceful-shutdown**](cmdqueryname=peer+graceful-shutdown) [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ] command to enable the g-shut function for a peer or peer group.
     2. Run the [**peer**](cmdqueryname=peer+graceful-shutdown+manual-activate) { *peerIpv4Addr* | *groupName* } [**graceful-shutdown manual-activate**](cmdqueryname=peer+graceful-shutdown+manual-activate) command to activate the g-shut function for a peer or peer group.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If a peer group has been configured with g-shut but peer A in it does not need to inherit g-shut from the peer group, run the [**peer**](cmdqueryname=peer+graceful-shutdown) *peerIpv4Addr* [**graceful-shutdown**](cmdqueryname=peer+graceful-shutdown) **disable** command. To prevent this peer from inheriting the g-shut activation status from the peer group, run the [**peer**](cmdqueryname=peer+graceful-shutdown+manual-activate) *peerIpv4Addr* [**graceful-shutdown manual-activate**](cmdqueryname=peer+graceful-shutdown+manual-activate) **disable** command.
4. (Optional) Run [**advertise-community-gshut**](cmdqueryname=advertise-community-gshut+ibgp+ebgp) [ **ibgp** | **ebgp** ]
   
   
   
   The device is configured to advertise the g-shut community attribute of the address family level.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) **verbose** command to check the status of BGP g-shut.
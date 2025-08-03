Configuring MSDP Peers
======================

Configuring MSDP Peers

#### Context

Depending on the scenario, you can use different methods when configuring MSDP peers to implement inter-domain multicast. [Table 1](#EN-US_TASK_0000001130783712__table786011435) shows how to configure MSDP peers. Method 3 is recommended for inter-AS MSDP peers.

**Table 1** Methods for configuring MSDP peers
| Configuration | Action | Application Scenario | Configuration description |
| --- | --- | --- | --- |
| Method 1 | Configure BGP to advertise routes, specify MSDP peers as next hops, and configure advertised BGP routes to be preferentially selected by multicast devices. | Inter-AS MSDP peer relationship | You can choose whether to configure a description for the MSDP peer on either end or both ends. The description contains a maximum of 80 characters. |
| Method 2 | Specify devices as static RPF peers of each other. | Inter-AS MSDP peer relationship | When you specify multiple static RPF peers for a device, use either of the following configuration methods:   * If source RP-based filtering is configured for SA messages on both ends: After receiving SA messages from multiple active static RPF peers, the local device filters them based on their respective filtering policies and only accepts those that pass. * If neither ends are configured to filter SA messages based on the source RP address: All SA messages received from active static RPF peers will be accepted.   NOTE:  Incorrect static RPF configurations may cause SA message looping. As such, exercise caution when configuring static RPF peers.  You can choose whether to configure a description for the MSDP peer on either end or both ends. The description contains a maximum of 80 characters. |
| Method 3 | Add all MSDP peers to the same mesh group. | Inter-AS MSDP peer relationship  Intra-AS MSDP peer relationship | Members of the same mesh group use the same mesh group name.  Each MSDP peer can only join one mesh group. If an MSDP peer is configured to join different mesh groups multiple times, the latest configuration takes effect.  You can choose whether to configure a description for the MSDP peer on either end or both ends. The description contains a maximum of 80 characters. |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the multicast function.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
   ```
3. Enable MSDP and enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
4. Configure an MSDP peer relationship.
   
   
   * Configure BGP to advertise routes with the MSDP peer as the next hop.
     ```
     [peer](cmdqueryname=peer) peer-address connect-interface interface-type interface-number
     [peer](cmdqueryname=peer) peer-address [description](cmdqueryname=description) text
     ```
   * Specify devices as static RPF peers of each other.
     ```
     [peer](cmdqueryname=peer) peer-address connect-interface interface-type interface-number
     [peer](cmdqueryname=peer) peer-address [description](cmdqueryname=description) text
     [static-rpf-peer](cmdqueryname=static-rpf-peer) peer-address [ rp-policy ip-prefix-name ]
     ```
   * Add all MSDP peers to the same mesh group.
     ```
     [peer](cmdqueryname=peer) peer-address connect-interface interface-type interface-number
     [peer](cmdqueryname=peer) peer-address [description](cmdqueryname=description) text
     [peer](cmdqueryname=peer) peer-address [mesh-group](cmdqueryname=mesh-group) name
     ```
5. (Optional) Disable the session with the remote MSDP peer.
   
   
   ```
   [shutdown](cmdqueryname=shutdown) peer-address
   ```
   
   SA messages are no longer exchanged between MSDP peers after the session with the remote MSDP peer is disabled, but the configuration is still retained. To re-establish a TCP connection with the remote MSDP peer, run the [**undo shutdown**](cmdqueryname=undo+shutdown) *peer-address* command.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
(Optional) Configuring LDP to Automatically Trigger Requests in DoD Mode
========================================================================

A remote LDP session must be configured before LDP is configured to automatically send requests in downstream-on-demand (DoD) mode

#### Context

To improve the stability of a large network with a great number of remote LDP peers and low-end DSLAMs deployed at the network edge, you need to minimize resource consumption. To achieve this, run the [**remote-ip auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request) or [**remote-peer auto-dod-request**](cmdqueryname=remote-peer+auto-dod-request) command to configure the function of triggering a request to a downstream node for Label Mapping messages associated with a specified or all remote LDP peers in DoD mode.

To disable an LSR from automatically sending a request to a downstream node for a Label Mapping message associated with a specified LSR ID in DoD mode, you can run the [**remote-ip auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request+block) **block** command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* A remote LDP session must have been configured before the [**remote-peer auto-dod-request**](cmdqueryname=remote-peer+auto-dod-request) or [**remote-ip auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request) command is run.
* Inter-area LDP extension must have been configured by using the [**longest-match**](cmdqueryname=longest-match) command before the [**remote-peer auto-dod-request**](cmdqueryname=remote-peer+auto-dod-request) or [**remote-ip auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request) command is run.
* A DoD session must have been established with the downstream node by using the [**mpls ldp advertisement**](cmdqueryname=mpls+ldp+advertisement+dod) **dod** command before the [**remote-peer auto-dod-request**](cmdqueryname=remote-peer+auto-dod-request) or [**remote-ip auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request) command is run.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Perform either or both of the following operations to configure the automatic triggering of a request to a downstream node for Label Mapping messages of a specified or all remote LDP peers in DoD mode.
   
   
   * To enable the device to automatically send DoD requests for Label Mapping messages to all downstream remote LDP peers, run the [**remote-peer auto-dod-request**](cmdqueryname=remote-peer+auto-dod-request) command.
   * To enable the device to automatically send DoD requests for Label Mapping messages to a specified downstream remote LDP peer, perform the following procedures:
     1. Run the [**quit**](cmdqueryname=quit) command to enter the system view.
     2. Run the [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name* command to create a remote MPLS LDP peer and enter the remote MPLS LDP peer view.
     3. Run the [**remote-ip**](cmdqueryname=remote-ip) *ip-address* command to specify the IP address of the remote MPLS LDP peer.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + This IP address must be the LSR ID that the remote LDP peer uses to establish the current remote session.
        + Modifying or deleting the configured IP address of a remote peer leads to the deletion of a remote LDP session.
     4. Run the [**remote-ip
        auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request) command to configure LDP to automatically send DoD requests for Label Mapping messages to a specified downstream remote LDP peer.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        To disable the function of the [**remote-peer auto-dod-request**](cmdqueryname=remote-peer+auto-dod-request) command, run the [**remote-ip auto-dod-request**](cmdqueryname=remote-ip+auto-dod-request+block) **block** command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
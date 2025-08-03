Configuring PW Status Negotiation
=================================

In independent PW redundancy mode, the master/backup status of the local PE is determined by the signaling status sent from the remote PE.

#### Context

In an independent PW redundancy scenario where a CE asymmetrically accesses PEs, the master/backup status of the local PE is determined by the signaling status sent from the remote PE, and the master/backup status of the ACs is determined by the E-Trunk status.


#### Procedure

1. Configure Eth-Trunk interfaces.
   
   
   
   Perform the following steps on the CE and the PEs to which the CE is dual-homed.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
      
      
      
      An Eth-Trunk interface is created.
   3. (Optional) Run [**portswitch**](cmdqueryname=portswitch)
      
      
      
      The Eth-Trunk interface is switched from the Layer 3 mode to the Layer 2 mode.
      
      
      
      This command is needed only on CEs. The Eth-Trunk sub-interfaces on PEs are the AC interfaces for service PWs.
   4. Run [**mode lacp-static**](cmdqueryname=mode+lacp-static)
      
      
      
      The Eth-Trunk interface is configured to work in static LACP mode.
   5. (Optional) Run [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> } | **all** }
      
      
      
      The interface is configured to allow packets with specified tags to pass through.
      
      
      
      This command is needed only on CEs, and the specified VLANs must be configured on the CEs.
   6. Run [**trunkport**](cmdqueryname=trunkport) *interface-type* { *interface-number1* [ **to***interface-number2* ] } &<1-64> [ **mode** { **active** | **passive** } ]
      
      
      
      A member interface is added.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure an E-Trunk.
   
   
   
   Perform the following steps on the PEs to which the CE is dual-homed.
   
   
   
   1. Run [**lacp e-trunk system-id**](cmdqueryname=lacp+e-trunk+system-id) *mac-address*
      
      
      
      An E-Trunk LACP system ID is configured.
      
      
      
      *mac-address* is in the format of H-H-H and cannot be all 0s or all Fs.
      
      The LACP system IDs of the master and backup devices in the E-Trunk must be the same.
   2. Run [**lacp e-trunk priority**](cmdqueryname=lacp+e-trunk+priority) *priority*
      
      
      
      The LACP priority is configured for the E-Trunk.
      
      
      
      The LACP priorities of the master and backup devices in an E-Trunk must be the same.
   3. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      An E-Trunk is created.
      
      
      
      *e-trunk-id* is an integer ranging from 1 to 16.
   4. Run [**security-key**](cmdqueryname=security-key) { **simple** *simple-key* | **cipher** *cipher-key* }
      
      
      
      An E-Trunk encryption password is configured.
      
      
      
      The encrypted passwords configured on the master and backup devices of an E-Trunk must be the same.
      
      
      
      For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
   5. Run [**priority**](cmdqueryname=priority) *priority*
      
      
      
      A priority is configured for the E-Trunk.
   6. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
      
      
      
      The local and peer IP addresses are configured.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
      
      
      
      The Eth-Trunk interface view is displayed.
   9. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The Eth-Trunk interface is added to the E-Trunk.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Bind BFD to the E-Trunk.
   
   
   
   Perform the following steps on the PEs to which the CE is dual-homed.
   
   
   
   1. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind peer-ip** *peer-ip* [ **interface** *interface-type interface-number* ] [ **source-ip** *source-ip* ]
      
      
      
      A BFD session is created.
      
      
      
      *bfd-name* specifies a BFD session name. The value is a string of 1 to 15 characters.
      
      **interface** *interface-type interface-number* specifies the Layer 3 outbound interface on which a BFD session is created.
      
      The IP addresses of the local and remote ends of a BFD session must be the same as those of the E-Trunk.
   2. Run [**discriminator local**](cmdqueryname=discriminator+local) *discr-value*
      
      
      
      A local discriminator is configured.
   3. Run [**discriminator remote**](cmdqueryname=discriminator+remote) *discr-value*
      
      
      
      A remote discriminator is configured.
      
      
      
      *discr-value* specifies a BFD session discriminator. The value is an integer ranging from 1 to 8191.
      
      The local discriminator on one end must be the same as the remote discriminator on the other end. Otherwise, the BFD session cannot be established. In addition, the local and remote discriminators cannot be modified after being configured.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The E-Trunk view is displayed.
   7. Run [**e-trunk track bfd-session**](cmdqueryname=e-trunk+track+bfd-session) **session-name** *bfd-session-name*
      
      
      
      The BFD session is bound to the E-Trunk.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
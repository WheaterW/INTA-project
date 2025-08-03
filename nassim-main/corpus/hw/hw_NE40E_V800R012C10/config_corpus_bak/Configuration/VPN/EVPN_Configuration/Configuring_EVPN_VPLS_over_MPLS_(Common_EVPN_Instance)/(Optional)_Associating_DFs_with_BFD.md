(Optional) Associating DFs with BFD
===================================

If a CE is dual-homed to PEs, you can associate the DF with BFD. If an access link fails, this configuration accelerates primary/backup DF switching.

#### Context

In a CE dual-homing scenario, to speed up primary/backup DF switching if an access link fails, you can create a BFD session between the two PEs, specify an access-side Eth-Trunk or PW VE interface as the interface to be monitored by the BFD session, and then associate the interface with the BFD session. After the configurations are complete, if the access link connected to the PE on which the primary DF resides fails, BFD can rapidly detect the fault and transmit the fault status to the other PE through the BFD session. This allows the backup DF to quickly become the primary DF.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally, and the global BFD view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**bfd**](cmdqueryname=bfd) *bfd-session-name* **bind peer-ip** *pe-ip-address* **track-interface** **interface** *interface-type* *interface-number*
   
   
   
   The binding between a BFD session and a peer IP address is created, and the BFD session view is displayed. *pe-ip-address* indicates the IP address of the remote PE, and *interface-type* *interface-number* indicates the type and number of the Eth-Trunk or PW VE interface on the access side.
5. Run the following commands to configure BFD session discriminators:
   
   
   1. To set the local discriminator, run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command.
   2. To set the remote discriminator, run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command.
   
   The local discriminator at one end must be the remote discriminator at the other end.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**interface**](cmdqueryname=interface) { **eth-trunk** *trunk-id* | **pw-ve** *interface-number* }
   
   
   
   The Eth-Trunk interface view or PW VE interface view is displayed.
8. Run [**es track bfd**](cmdqueryname=es+track+bfd) *bfd-session-name*
   
   
   
   The interface is associated with the BFD session.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
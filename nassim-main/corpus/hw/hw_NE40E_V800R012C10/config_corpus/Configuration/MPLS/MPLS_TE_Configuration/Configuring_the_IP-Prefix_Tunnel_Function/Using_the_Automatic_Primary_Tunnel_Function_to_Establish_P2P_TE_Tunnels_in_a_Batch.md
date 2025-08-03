Using the Automatic Primary Tunnel Function to Establish P2P TE Tunnels in a Batch
==================================================================================

The automatic primary tunnel function can be used to establish P2P TE tunnels in a batch.

#### Context

The automatic primary tunnel function uses a specified IP prefix list in which destination IP addresses are defined so that tunnels to the destination IP addresses can be established in a batch. The automatic primary tunnel function can also use a specified tunnel template that defines public attributes before creating tunnels in a batch.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls te auto-primary-tunnel**](cmdqueryname=mpls+te+auto-primary-tunnel) **ip-prefix** *ip-prefix* [ **p2p-template** *template-name* ]
   
   
   
   The automatic primary tunnel function is configured.
3. (Optional) Set the hold time for tunnels.
   1. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      The MPLS view is displayed.
   2. Run [**mpls te timer auto-primary-tunnel**](cmdqueryname=mpls+te+timer+auto-primary-tunnel) **delay-delete** *time-value*
      
      
      
      The hold time for tunnels is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

If errors occur in services transmitted on a TE tunnel and the services cannot be restored, run the reset mpls te auto-primary-tunnel command in the user view to reestablish the TE tunnel to restore the services.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After this command is run, all LSPs in the specified tunnel are torn down and reestablished. If some LSPs are transmitting traffic, the operation causes a traffic interruption. Exercise caution when using this command.
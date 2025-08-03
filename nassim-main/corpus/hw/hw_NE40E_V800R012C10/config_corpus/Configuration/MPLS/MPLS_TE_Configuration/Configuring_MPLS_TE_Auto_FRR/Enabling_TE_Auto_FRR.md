Enabling TE Auto FRR
====================

TE Auto FRR must be enabled on the PLR of the bypass tunnel before the function is configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) [ **self-adapting** ]
   
   
   
   TE Auto FRR is enabled globally.
   
   
   
   To enable an automatic bypass tunnel to dynamically select node protection or link protection based on network conditions, specify **self-adapting**.
   
   If the **self-adapting** parameter is not specified, the current automatic bypass tunnel selects node protection by default.
4. (Optional) Configure TE Auto FRR on an interface.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the outbound interface on the primary tunnel.
   3. Run the [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) { **block** | **default** | **link** | **node** | **self-adapting** } command to configure TE Auto FRR on the interface.
      
      
      
      After Auto FRR is enabled globally, all MPLS TE-enabled interfaces on the device are automatically configured with [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) **default**. To disable Auto FRR on some interfaces, run the [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) **block** command on these interfaces. After the [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) **block** command is run on an interface, the interface does not have the Auto FRR capability, regardless of whether Auto FRR is enabled or re-enabled globally.
      
      To enable an automatic bypass tunnel to dynamically select node protection or link protection based on network conditions, specify **self-adapting**.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * If the [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) **default** command is run, the Auto FRR capability status of an interface is the same as the global Auto FRR capability status.
      * After node protection is enabled, if a bypass tunnel for node protection fails to be created because the topology does not meet requirements, the penultimate hop of the primary tunnel attempts to create link protection, and other nodes do not degrade to create link protection.
      * If **self-adapting** is not specified and node protection is enabled, the penultimate hop of the primary tunnel attempts to create link protection when a bypass tunnel fails to be created because the topology does not meet requirements. Other nodes do not degrade to create link protection.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
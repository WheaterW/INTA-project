Binding an Eth-Trunk Interface to an ICCP Redundancy Group
==========================================================

Binding_an_Eth-Trunk_Interface_to_an_ICCP_Redundancy_Group

#### Context

mLACP transmits LACP configuration and status information in an ICCP redundancy group through an ICCP channel to negotiate link aggregation. An Eth-Trunk interface can be added to an ICCP redundancy group after being configured to work in static LACP mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   The Eth-Trunk interface view is displayed.
3. Run [**mode lacp-static**](cmdqueryname=mode+lacp-static)
   
   
   
   The Eth-Trunk interface is configured to work in static LACP mode. Only Eth-Trunk interfaces in static LACP mode can be added to an ICCP redundancy group.
4. Run **[**mlacp iccp-group**](cmdqueryname=mlacp+iccp-group)** **iccp-group-value**
   
   
   
   The Eth-Trunk interface is bound to an ICCP redundancy group.
5. (Optional) Run **[**mlacp port-priority**](cmdqueryname=mlacp+port-priority)** *priority*
   
   
   
   An mLACP port priority is configured for the Eth-Trunk interface bound to the ICCP redundancy group.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the user view.
8. (Optional) Run **[**reset mlacp port-priority eth-trunk**](cmdqueryname=reset+mlacp+port-priority+eth-trunk)** **eth-trunk-id**
   
   
   
   The running mLACP port priority is restored to the configured value.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   mLACP may use the port priority requested by the peer end as the running port priority. In this case, the port priority configured using the [**mlacp port-priority**](cmdqueryname=mlacp+port-priority) command does not take effect. To restore the configured priority, you can run the **[**reset mlacp port-priority eth-trunk**](cmdqueryname=reset+mlacp+port-priority+eth-trunk)** **eth-trunk-id** command.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
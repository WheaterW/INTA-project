Configuring a Channelized Sub-interface
=======================================

This section describes how to configure a channelized sub-interface.

#### Context

To prevent services from affecting each other, a mechanism to isolate different types of services is needed. Different service flows are forwarded through VLAN channelized sub-interfaces with different encapsulation modes, and each channelized sub-interface implements independent HQoS scheduling to isolate services of different types.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subinterface-number*
   
   
   
   The view of a specified sub-interface is displayed.
3. Configure the sub-interface as required.
   
   If the sub-interface is an Ethernet one:
   * Run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlanid* command to set the encapsulation mode of the sub-interface to dot1q.
   * Run the [**encapsulation qinq-termination**](cmdqueryname=encapsulation+qinq-termination) and [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vlanid* [**ce-vid**](cmdqueryname=ce-vid) *ce-vlanid* commands to set the encapsulation mode of the sub-interface to QinQ termination.
   
   If the sub-interface is a POS one, run the [**fr dlci**](cmdqueryname=fr+dlci) *dlci-value* command to set its encapsulation mode to POS FR. This command depends on the [**link-protocol fr**](cmdqueryname=link-protocol+fr) command configuration on the POS main interface.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The channelized sub-interface license does not need to be activated on GE interfaces.
6. Run [**active port-mode-channel**](cmdqueryname=active+port-mode-channel)
   
   
   
   The license for channelized sub-interfaces is activated.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subinterface-number*
   
   
   
   The view of a specified sub-interface is displayed.
9. Run [**mode channel enable**](cmdqueryname=mode+channel+enable)
   
   
   
   Channelization is enabled for the sub-interface.
10. (Optional) Run [**mode channel bandwidth**](cmdqueryname=mode+channel+bandwidth) *bwvalue*
    
    
    
    The bandwidth is configured for the channelized sub-interface.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
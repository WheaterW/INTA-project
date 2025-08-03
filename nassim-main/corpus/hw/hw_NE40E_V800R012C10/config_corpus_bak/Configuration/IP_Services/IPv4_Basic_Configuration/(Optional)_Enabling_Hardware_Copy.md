(Optional) Enabling Hardware Copy
=================================

The hardware copy function allows a device to forward the protocol packets to be broadcast through hardware instead of sending them to the CPU, achieving fast forwarding.

#### Usage Scenario

If a lot of VLANs are configured on a super VLANIF interface, a dot1q VLAN tag termination sub-interface, or a QinQ VLAN tag termination sub-interface, the protocol packets to be forwarded will be broadcast to all the configured VLANs, which burdens the CPU. The hardware copy function allows the protocol packets to be broadcast through hardware, which reduces CPU performance consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Enable hardware copy either globally or on an interface. 
   
   
   * To enable hardware copy globally in the system view, run [**broadcast-copy fast enable**](cmdqueryname=broadcast-copy+fast+enable)
   * To enable hardware copy on a dot1q VLAN tag termination sub-interface or a QinQ VLAN tag termination sub-interface, run the following commands:
     1. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*.*subinterface-number*
        
        The sub-interface view is displayed.
     2. Run either of the following commands:
        + To configure the sub-interface as a dot1q VLAN tag termination sub-interface, run the [**encapsulation dot1q-termination**](cmdqueryname=encapsulation+dot1q-termination) command.
        + To configure the sub-interface as a QinQ VLAN tag termination sub-interface, run the [**encapsulation qinq-termination**](cmdqueryname=encapsulation+qinq-termination) command.
     3. Run [**broadcast-copy fast enable**](cmdqueryname=broadcast-copy+fast+enable)
        
        The hardware copy function is enabled.
   * To enable hardware copy on a super VLANIF interface, run the following commands:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The interface view is displayed.
     2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
        
        The VLAN view is displayed.
     3. Run [**aggregate-vlan**](cmdqueryname=aggregate-vlan)
        
        The VLAN is configured as a super VLAN.
     4. Run [**interface vlanif**](cmdqueryname=interface+vlanif) *vlanif-id*
        
        The VLANIF interface view is displayed.
     5. Run [**broadcast-copy fast enable**](cmdqueryname=broadcast-copy+fast+enable)
        
        The hardware copy function is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
(Optional) Configuring Bandwidth for a VLANIF Interface
=======================================================

After configuring bandwidth for VLANIF interfaces, you can use the NMS to query the bandwidth. This facilitates traffic monitoring.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vlanif** *vlan-id*
   
   
   
   The VLANIF interface view is displayed.
   
   
   
   The VLAN ID specified in this command must be the ID of an existing VLAN.
3. Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
   
   
   
   Bandwidth is configured for the VLANIF interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
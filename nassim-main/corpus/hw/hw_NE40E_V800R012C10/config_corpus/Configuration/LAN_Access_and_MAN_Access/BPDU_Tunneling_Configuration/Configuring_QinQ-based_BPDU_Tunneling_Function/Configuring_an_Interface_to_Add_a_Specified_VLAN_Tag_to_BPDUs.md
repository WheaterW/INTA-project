Configuring an Interface to Add a Specified VLAN Tag to BPDUs
=============================================================

If multiple user networks are connected to the same interface of a PE, configure the interfaces of CEs to add specified VLAN IDs to bridge protocol data units (BPDUs) before sending them to the PE. The VLAN IDs identify the user networks to which the BPDUs belong.

#### Context

Perform the following steps on CEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A VLAN is created, and its view is displayed.
   
   
   
   The VLAN ID ranges from 1 to 4094. To create multiple VLANs, repeat this step.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface connected to a PE is displayed.
5. Run [**port trunk allow-pass**](cmdqueryname=port+trunk+allow-pass) **vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }
   
   
   
   The VLAN ID that the CE allows to pass is configured.
6. Run [**stp bpdu vlan**](cmdqueryname=stp+bpdu+vlan) *vlan-id*
   
   
   
   The interface is configured to add the specified VLAN ID to BPDUs that will be sent to the PE.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the specified VLAN ID is the same as that carried in BPDUs received by the interface.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
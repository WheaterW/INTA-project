Adding an Interface to a Specified VLAN
=======================================

Each interface on a provider edge (PE) is connected to one user network, and user networks belong to different local area networks (LANs). BPDUs sent from user networks to PEs are untagged. The PEs, however, need to identify the LANs to which the BPDUs belong. In this situation, you need to add the PE interfaces to specified virtual local area networks (VLANs).

#### Context

Perform the following steps on PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A VLAN is created, and the VLAN view is displayed.
   
   
   
   The VLAN ID ranges from 1 to 4094. If the VLAN to be created exists, the command displays the VLAN view.
3. Run [**port**](cmdqueryname=port) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10>
   
   
   
   The interface on the PE that is connected to a customer edge (CE) is added to the created VLAN.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To add an interface on the PE that is connected to a CE to a specified VLAN in untagged mode, you can also run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
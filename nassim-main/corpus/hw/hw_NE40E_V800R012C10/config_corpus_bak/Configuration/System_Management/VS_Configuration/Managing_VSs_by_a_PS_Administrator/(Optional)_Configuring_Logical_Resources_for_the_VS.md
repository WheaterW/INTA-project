(Optional) Configuring Logical Resources for the VS
===================================================

A Physical System (PS) administrator can allocate logical resources to Virtual Systems through two methods.

#### Context

PS administrator can assign a logical resource to a VS each time, or use a resource template to assign multiple logical resources to a VS in a batch.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration task applies only to the admin VS.



#### Procedure

* Assign a logical resource to a VS each time.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**admin**](cmdqueryname=admin)
     
     
     
     The admin view is displayed.
  3. Run [**virtual-system**](cmdqueryname=virtual-system) *vs-name*
     
     
     
     The VS view is displayed.
  4. Run [**port-mode**](cmdqueryname=port-mode) **port-mode** [ **resource-template** *template-name* ]
     
     
     
     A port mode is configured for the VS.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You cannot delete the port mode that has been configured for a VS.
  5. In the virtual system view, run [**resource**](cmdqueryname=resource) { **m4route** | **m6route** | **u4route** | **u6route** | **vpn-instance** } **upper-limit** *resource-limit*
     
     
     
     Logical resources are assigned to the VS.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Assign multiple logical resources to a VS in a batch.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**admin**](cmdqueryname=admin)
     
     
     
     The admin view is displayed.
  3. Run [**virtual-system**](cmdqueryname=virtual-system) *vs-name*
     
     
     
     The VS view is displayed.
  4. Run [**port-mode**](cmdqueryname=port-mode) **port** [ **resource-template** *template-name* ]
     
     
     
     A port mode is configured for the VS.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You cannot delete the port mode that has been configured for a VS.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the VS view and enter the admin view.
  6. Run [**resource-template**](cmdqueryname=resource-template) *template-name*
     
     
     
     A resource template is created or modified and the resource template view is displayed.
  7. In the resource template view, run [**resource**](cmdqueryname=resource) { **m4route** | **m6route** | **u4route** | **u6route** | **vpn-instance** } **upper-limit** *resource-limit*
     
     
     
     Resource items are added to the resource template, and the item specification is specified.
  8. Run [**assign resource-template**](cmdqueryname=assign+resource-template) *template-name*
     
     
     
     The resource template is assigned to the VS.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
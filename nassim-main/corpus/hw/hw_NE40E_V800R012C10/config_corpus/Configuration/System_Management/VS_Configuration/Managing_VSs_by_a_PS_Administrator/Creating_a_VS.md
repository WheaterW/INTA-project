Creating a VS
=============

A Physical System (PS) administrator can create Virtual Systems (VSs) on the PS, but cannot create, or delete the Admin-VS. The Admin-VS is the default VS on a PS and manages the entire PS. The Admin-VS is automatically created when a PS is being started. All the unassigned resources on a PS belong to the Admin-VS by default. A VS is started as soon as it is created.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**admin**](cmdqueryname=admin)
   
   
   
   The admin view is displayed.
3. Run [**virtual-system**](cmdqueryname=virtual-system) *vs-name*
   
   
   
   A VS is created and started.
4. Run [**port-mode**](cmdqueryname=port-mode) **port-mode** [ **resource-template** *template-name* ]
   
   
   
   A port mode is configured for the VS.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You cannot delete the port mode that has been configured for a VS.
5. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   The description of a VS is displayed.
   
   The network administrator can configure a description for the VS to describe the service type or usage.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the VS creation process, the NetStream function becomes unavailable in two minutes.
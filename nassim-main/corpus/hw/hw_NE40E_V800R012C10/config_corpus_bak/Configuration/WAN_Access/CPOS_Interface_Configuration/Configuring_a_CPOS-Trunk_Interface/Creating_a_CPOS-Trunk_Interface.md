Creating a CPOS-Trunk Interface
===============================

This section describes how to create a CPOS-Trunk interface and add a CPOS member interface to the CPOS-Trunk interface.

#### Context

In scenarios where automatic protection switching (APS) is configured to protect services, CPOS interfaces must be added to a CPOS-Trunk interface so that services can be carried on a Trunk-Serial interface channelized from the CPOS-Trunk interface.


#### Procedure

1. Create a CPOS-Trunk interface.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface cpos-trunk**](cmdqueryname=interface+cpos-trunk) *trunk-id* command to create a CPOS-Trunk interface. If the CPOS-Trunk interface already exists, this command displays the CPOS-Trunk interface view.
2. Add a specified CPOS interface to the CPOS-Trunk interface.
   1. Run the [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number* command to enter the view of the specified CPOS interface.
   2. Run the [**cpos-trunk**](cmdqueryname=cpos-trunk) *trunk-id* command to add the CPOS interface to the CPOS-Trunk interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before adding a CPOS interface to a CPOS-Trunk interface, run the [**aps group**](cmdqueryname=aps+group) command on the CPOS interface to add it to an LMSP group and then configure the CPOS interface as a working or protection interface. For details about how to configure LMSP, see [LMSP Configuration](../ne/dc_ne_lmsp_cfg_router.html).
   
   After adding a CPOS interface to a CPOS-Trunk interface, note the following:
   * If you run the [**shutdown**](cmdqueryname=shutdown) command on the CPOS-Trunk interface, the physical status of both the CPOS-Trunk interface and its member interface becomes **Administratively DOWN**, and the status of the member interface is automatically displayed as **shutdown** in the configuration file.
   * If you run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on the CPOS-Trunk interface, the status of its member interface is automatically displayed as **undo shutdown** in the configuration file.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
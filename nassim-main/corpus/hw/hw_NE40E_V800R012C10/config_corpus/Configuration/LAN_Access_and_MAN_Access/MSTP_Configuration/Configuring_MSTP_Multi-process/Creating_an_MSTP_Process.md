Creating an MSTP Process
========================

A process ID uniquely identifies a Multiple Spanning Tree Protocol (MSTP) multi-process. After an MSTP device binds its ports to different processes, the MSTP device performs the MSTP calculation based on processes, and only relevant ports in each process take part in MSTP calculation.

#### Context

Do as follows on the devices connected to access rings:
#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp process**](cmdqueryname=stp+process) *process-id*
   
   
   
   An MSTP process is created, and its view is displayed.
3. Run [**stp mode**](cmdqueryname=stp+mode) **mstp**
   
   
   
   A working mode is configured for the MSTP process.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After a device starts, there is a default MSTP process with the ID 0. MSTP configurations in the system view and interface view belong to this process. The default working mode of this process is MSTP.
   * To add an interface to an MSTP process with the ID of non-zero, run the [**stp process**](cmdqueryname=stp+process) command and then the [**stp binding process**](cmdqueryname=stp+binding+process) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
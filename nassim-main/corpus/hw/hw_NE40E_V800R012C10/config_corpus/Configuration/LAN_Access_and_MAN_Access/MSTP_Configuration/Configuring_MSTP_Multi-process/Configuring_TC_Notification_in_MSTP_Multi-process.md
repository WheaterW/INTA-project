Configuring TC Notification in MSTP Multi-process
=================================================

After the Topology Change (TC) notification function is configured for Multiple Spanning Tree Protocol (MSTP) multi-process, the current MSTP process can notify the Multiple Spanning Tree Instances (MSTIs) in other specified MSTP processes to refresh MAC address entries and ARP entries after receiving a TC-BPDU. Nonstop services are ensured.

#### Context

Do as follows on the devices connected to access rings:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp process**](cmdqueryname=stp+process) *process-id*
   
   
   
   The view of the created MSTP process is displayed.
3. Run [**stp tc-notify process 0**](cmdqueryname=stp+tc-notify+process+0)
   
   
   
   TC notification is enabled in the MSTP process.
   
   
   
   After the [**stp tc-notify process 0**](cmdqueryname=stp+tc-notify+process+0) command is run, the current MSTP process notifies the MSTIs in MSTP process 0 to update MAC entries and ARP entries after receiving a TC-BPDU. This prevents services from being interrupted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
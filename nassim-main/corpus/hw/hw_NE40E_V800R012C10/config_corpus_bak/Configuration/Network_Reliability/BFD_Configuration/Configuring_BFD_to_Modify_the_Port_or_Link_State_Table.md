Configuring BFD to Modify the Port or Link State Table
======================================================

This section describes how to enable BFD to modify the port or link state table to speed up link fault detection. This function applies only to single-hop BFD sessions.

#### Usage Scenario

If BFD is enabled to modify the port or link state table, BFD modifies related entries in the port or link state table upon detecting an interface or link down event. This function allows the underlying layer to detect the fault based on the change in the port or link state table.

In BFD-based link protection scenarios such as BFD for FRR, you are advised to configure BFD to modify the port or link state table upon detection of a fault in a BFD session so that a fast link switchover can be performed.


#### Pre-configuration Tasks

Before configuring BFD to modify the PST or link state table (LST), complete the following task:

* [Configure single-hop BFD](dc_vrp_bfd_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**process-pst**](cmdqueryname=process-pst)
   
   
   
   BFD is allowed to modify the port or link state table upon detection of a fault.
   
   
   
   After the **process-pst** command is run, the BFD session is associated with the port or link state table of the interface to which the BFD session is bound. After the BFD session detects a link down event, BFD sets the port or link state table of the interface bound to the BFD session to down. Then, the system switches traffic to a working link accordingly.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
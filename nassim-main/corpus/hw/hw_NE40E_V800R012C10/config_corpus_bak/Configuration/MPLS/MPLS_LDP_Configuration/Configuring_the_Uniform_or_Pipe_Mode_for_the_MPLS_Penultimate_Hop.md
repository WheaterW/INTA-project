Configuring the Uniform or Pipe Mode for the MPLS Penultimate Hop
=================================================================

This section describes the process of configuring the uniform/pipe mode for the MPLS penultimate hop.

#### Pre-configuration Tasks

Before configuring the uniform or pipe mode for the MPLS penultimate hop, complete the following tasks:

* Configure the physical parameters and link attributes of interfaces to ensure that they work properly.
* Establish an MPLS TE tunnel between PEs when MPLS TE networking is used. For details, see "MPLS TE Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - MPLS*.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Perform the following configuration on MPLS LSP or MPLS TE penultimate hop:



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls lsp exp-mode**](cmdqueryname=mpls+lsp+exp-mode) { **pipe** | **uniform** }
   
   
   
   A global MPLS DiffServ mode is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The mode configured using this command takes effect only on new LSPs. To have the mode take effect on existing LSPs, you need to run the [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp) command to reestablish the LSPs.
   * The command is run only on the penultimate hop to determine whether to copy the EXP value of an outer label to the EXP value of an inner label.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
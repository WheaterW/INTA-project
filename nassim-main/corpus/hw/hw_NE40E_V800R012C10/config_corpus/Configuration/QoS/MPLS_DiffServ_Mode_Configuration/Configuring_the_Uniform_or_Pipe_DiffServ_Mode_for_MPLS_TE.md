Configuring the Uniform or Pipe DiffServ Mode for MPLS TE
=========================================================

This section describes the process of configuring the uniform or pipe DiffServ mode for MPLS TE.

#### Usage Scenario

To implement service class-based queue scheduling for MPLS TE services on the public network, configure the uniform or pipe mode for MPLS TE.

#### Pre-configuration Tasks

Before configuring the uniform or pipe mode for MPLS TE, complete the following tasks:

* Configure physical parameters and link attributes for each interface to ensure that the interfaces work properly.
* Configure an MPLS TE tunnel between two PEs. For details, see "MPLS TE Configuration" in HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - MPLS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before configuring the uniform or pipe mode for MPLS TE, check that MPLS TE is up.

Perform the following configuration on the user-side tunnel interface of the ingress PE. The configuration takes effect only for the ingress PE. The penultimate node uses the uniform mode by default.

For details about how to change the DiffServ mode on the penultimate node, see [Configuring the Uniform or Pipe Mode for the MPLS Penultimate Hop](../vrp/dc_vrp_ldp-p2p_cfg_0093.html).




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The view of the user-side tunnel interface is displayed.
3. Run [**diffserv-mode**](cmdqueryname=diffserv-mode) { **pipe** *service-class* *color* | **uniform** }
   
   
   
   A DiffServ mode is configured for MPLS TE.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
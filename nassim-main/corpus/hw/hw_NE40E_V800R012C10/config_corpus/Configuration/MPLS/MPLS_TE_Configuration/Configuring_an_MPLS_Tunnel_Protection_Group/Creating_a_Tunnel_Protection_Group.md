Creating a Tunnel Protection Group
==================================

A configured protection tunnel can be bound to a working tunnel to form a tunnel protection group. If the working tunnel fails, traffic switches to the protection tunnel, which improves tunnel reliability.

#### Context

A tunnel protection group can be configured on the ingress to protect a working tunnel. The switchback delay time and a switchback mode can also be configured. If the revertive mode is used, the wait to restore (WTR) time can be set.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface view is displayed.
3. Run [**mpls te protection tunnel**](cmdqueryname=mpls+te+protection+tunnel) *tunnel-id* [ [ **holdoff** *holdoff-time* ] | [ **mode** { **non-revertive** | **revertive** [ **wtr** *wtr-time* ] } ] ] \*
   
   
   
   The working tunnel is added to a protection group.
   
   
   
   The following parameters can be configured in this step:
   
   * *tunnel-id* specifies the ID of a protection tunnel.
   * *holdoff-time* specifies the period between the time when a signal failure occurs and the time when the protection switching algorithm is initiated upon notification of the signal fault. *holdoff-time* specifies a multiplier of 100 milliseconds.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Hold-off time = 100 milliseconds x *holdoff-time*
   * In non-revertive mode, traffic does not switch back to a working tunnel even after the working tunnel recovers.
   * In revertive mode, traffic switches back to a working tunnel after the working tunnel recovers.
   * The WTR time is the time elapses before traffic switching is performed. The *wtr-time* parameter specifies a multiplier of 30 seconds.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     WTR time = 30 seconds x *wtr-time*
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Configure a detection mechanism.

#### Follow-up Procedure

You can also perform the preceding steps to modify a protection group.

An MPLS TE tunnel protection group must be detected by MPLS OAM or MPLS-TP OAM to rapidly trigger protection switching if a fault occurs.

After an MPLS TE tunnel protection group is created, properly select an MPLS OAM mechanism:

* If both the working and protection tunnels are static bidirectional associated LSPs, [configure MPLS OAM for bidirectional associated LSPs](dc_vrp_mplsoam_cfg_0004.html).
* If both the working and protection tunnels are static bidirectional co-routed LSPs, [configure MPLS OAM for bidirectional co-routed LSPs](dc_vrp_mplsoam_cfg_0008.html).
* If OAM is deleted before APS is deleted, APS incorrectly considers that OAM has detected a link fault, affecting protection switching. To resolve this issue, re-configure OAM.

After an MPLS TE tunnel protection group is created, if MPLS-TP OAM is used to detect faults and both the working and protection tunnels are static bidirectional co-routed CR-LSPs, [configure MPLS-TP OAM for bidirectional co-routed LSPs](dc_vrp_mpls-tp_oam_cfg_0004.html).
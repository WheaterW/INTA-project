(Optional) Configuring the Protection Switching Trigger Mechanism
=================================================================

This section describes how to configure the protection switching trigger mechanism for a tunnel protection group to forcibly switch traffic to the working or protection tunnel. Alternatively, you can perform a traffic switchover manually.

#### Context

Read [switching rules](dc_vrp_te-p2p_cfg_0162.html#EN-US_CONCEPT_0172368234__tab_dc_vrp_te-p2p_cfg_016201) before configuring the protection switching trigger mechanism.

Perform the following steps on the ingress of the tunnel protection group as needed:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface view is displayed.
3. Select one of the following protection switching trigger methods as required:
   
   
   * To forcibly switch traffic from the working tunnel to the protection tunnel, run [**mpls te protect-switch**](cmdqueryname=mpls+te+protect-switch) **force**
   * To prevent traffic on the working tunnel from switching to the protection tunnel, run [**mpls te protect-switch**](cmdqueryname=mpls+te+protect-switch) **lock**
   * To switch traffic to the protection tunnel, run [**mpls te protect-switch**](cmdqueryname=mpls+te+protect-switch) **manual**
   * To cancel the configuration of the protection switching trigger mechanism, run [**mpls te protect-switch**](cmdqueryname=mpls+te+protect-switch) **clear**![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The preceding commands can take effect immediately after being run, without the [**commit**](cmdqueryname=commit) command executed.
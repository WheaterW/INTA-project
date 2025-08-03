Configuring Bit-Error-Triggered RSVP-TE Tunnel Switching
========================================================

This section describes how to configure bit-error-triggered Resource Reservation Protocol-Traffic Engineering (RSVP-TE) tunnel switching.

#### Usage Scenario

Bit errors caused by optical fiber aging or optical signal jitter may exist on carrier networks. These bit errors may result in the interruption of services with high quality requirements. If a network uses an RSVP-TE tunnel with traffic engineering (TE) hot standby protection to carry services, you can configure bit-error-triggered RSVP-TE tunnel switching to protect services against bit errors.

Then, if a bit error event occurs on a link along the TE tunnel, TE hot-standby switching is triggered to minimize the impact of the bit error event on services.


#### Pre-configuration Tasks

Before configuring bit-error-triggered RSVP-TE tunnel switching, complete the following tasks:

* Configure two unidirectional RSVP-TE tunnels in opposite directions.
  
  ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  Before establishing a unidirectional RSVP-TE tunnel, you must run the [**label advertise**](cmdqueryname=label+advertise) **non-null** command to enable the egress of the unidirectional tunnel to allocate a non-null label to the penultimate hop. Otherwise, bit-error-triggered RSVP-TE tunnel switching cannot take effect.
* Configure CR-LSP hot standby for the forward and reverse RSVP-TE tunnels. For configuration details, see [Configuring CR-LSP Backup](dc_vrp_te-p2p_cfg_0057.html).
* Enable Bidirectional Forwarding Detection (BFD) globally on the nodes along the primary and backup CR-LSPs of each unidirectional RSVP-TE tunnel.
* [Configure static BFD for CR-LSP](dc_vrp_te-p2p_cfg_0121.html) or [dynamic BFD for CR-LSP](dc_vrp_te-p2p_cfg_0144.html).

#### Procedure

1. Enabling Bit Error Detection on Interfaces Along the RSVP-TE Tunnel
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface along the TE tunnel is displayed.
   3. Run [**trap-threshold crc-error packet-error-ratio**](cmdqueryname=trap-threshold+crc-error+packet-error-ratio) **alarm-threshold** *coef-value pow-value* [ **resume-threshold** *rsm-coef-value rsm-pow-value* ] **trigger-lsp**
      
      
      
      Bit error detection is enabled on the interface, and the BER threshold for triggering the bit error alarm is set.
      
      
      
      To associate bit error alarm with RSVP-TE tunnel switching, specify **trigger-lsp**.
      
      The **alarm-threshold** value equals *alarm-coe* multiplied by 10-*alarm-pow*. If the BER detected by a trunk member interface exceeds the **alarm-threshold** value, the trunk member interface reports an alarm indicating that a bit error event has occurred.
      
      The **resume-threshold** value equals *resume-coe* multiplied by 10-*resume-pow*. If the BER detected by a trunk member interface falls below the **resume-threshold** value, the trunk member interface reports an alarm indicating that the bit error event is over.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The **resume-threshold** value cannot be greater than the **alarm-threshold** value.
      * If you do not specify the **resume-threshold** value, the system automatically uses tenth of the **alarm-threshold** value as the **resume-threshold** value.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Enabling Bit-Error-Triggered RSVP-TE Tunnel Switching
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. (Optional) Enable bit error detection compatibility globally.
      
      
      1. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
      2. Run the [**mpls te**](cmdqueryname=mpls+te) command to enable MPLS TE.
      3. Run the [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te) command to enable RSVP-TE.
      4. Run the [**mpls rsvp-te bit-error-detection compatible**](cmdqueryname=mpls+rsvp-te+bit-error-detection+compatible) command to enable bit error detection compatibility globally. In a scenario where a Huawei device communicates with a non-Huawei device and bit error detection is enabled for the RSVP-TE tunnels, if the non-Huawei device incorrectly parses the non-standard vendor private object in the Path message, the LSPs cannot be established. To enable bit error detection compatibility, run this command. In this case, the Path message sent by the Huawei device carries the vendor private object defined in the standard to ensure that the Huawei device can communicate with non-Huawei devices properly.
      5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
      
      
      
      The tunnel interface view is displayed.
   4. Run [**mpls te bit-error-detection**](cmdqueryname=mpls+te+bit-error-detection) [ **mode** { **unidirectional** | **bidirectional** } ]
      
      
      
      Bit-error-triggered tunnel switching is enabled for the current tunnel.
      
      
      
      This function supports two switching modes: **unidirectional** and **bidirectional**.
      
      * **unidirectional**: In this mode, a bit error event triggers only the current tunnel to perform protection or revertive switching.
      * **bidirectional**: In this mode, a bit error event triggers both the current tunnel and its reverse tunnel to perform protection or revertive switching.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In real-world applications, RSVP-TE tunnels are usually deployed bidirectionally. The primary CR-LSPs of a pair of RSVP-TE tunnels in opposite directions are on the same path. If an RSVP-TE tunnel performs a primary/backup CR-LSP switchover, its reverse tunnel should also perform a primary/backup CR-LSP switchover to minimize the impact of bit errors on services.
   5. Run [**mpls te reverse-lsp**](cmdqueryname=mpls+te+reverse-lsp) **protocol** **rsvp-te** **ingress-lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id*
      
      
      
      The dynamic reverse LSP for the current tunnel is specified.
      
      Bit-error-triggered RSVP-TE tunnel switching implements bidirectional switching with the help of dynamic reverse LSPs.
   6. (Optional) Run [**mpls te bit-error-detection threshold**](cmdqueryname=mpls+te+bit-error-detection+threshold) **switch** *switch-coe* *switch-pow* **resume** *resume-coe* *resume-pow*
      
      
      
      The thresholds for bit-error-triggered protection switching and revertive switching are set.
      
      
      
      The *switch-coe* parameter specifies the coefficient of the protection switching threshold, and the *switch-pow* parameter specifies the power of the protection switching threshold. The formula for calculating the threshold for bit-error-triggered protection switching is as follows:
      
      Protection switching threshold = *switch-coe* Ã 10-*switch-pow*
      
      Similarly, the *resume-coe* parameter specifies the coefficient of the revertive switching threshold, and the *resume-pow* parameter specifies the power of the revertive switching threshold. The formula for calculating the threshold for bit-error-triggered revertive switching is similar to the formula for calculating the threshold for bit-error-triggered protection switching.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The revertive switching threshold cannot be greater than the protection switching threshold.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
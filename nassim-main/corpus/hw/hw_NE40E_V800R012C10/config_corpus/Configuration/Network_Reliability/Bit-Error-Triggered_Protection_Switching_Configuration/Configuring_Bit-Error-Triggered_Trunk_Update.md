Configuring Bit-Error-Triggered Trunk Update
============================================

To cope with bit errors detected on trunk member interfaces, configure bit-error-triggered trunk update.

#### Usage Scenario

If bit errors are generated or cleared on a trunk member interface, bit-error-triggered trunk update triggers the trunk interface to delete or re-add the member interface from or to the forwarding plane. If bit errors occur on all trunk member interfaces or the number of member interfaces without bit errors is lower than the lower threshold for the trunk interface's Up links, bit-error-triggered protection switching involves the following modes:

* Trunk-bit-error-triggered section switching: The trunk interface goes Down, triggering an upper-layer application associated with the trunk interface to perform a service switchover.
* Trunk-bit-error-triggered IGP route switching: The trunk interface ignores the bit errors on the member interfaces and remains Up. However, the link quality level of the trunk interface becomes Low, triggering an IGP to increase the cost of the trunk interface's link. IGP routes then do not preferentially select the link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If bit errors occur on the trunk interfaces on both the primary and secondary links, trunk-bit-error-triggered section switching may interrupt services. Therefore, trunk-bit-error-triggered IGP route switching is recommended.



#### Pre-configuration Tasks

Before configuring bit-error-triggered trunk update, complete the following tasks:

* [Configure an Eth-Trunk interface in manual load balancing mode](dc_vrp_ethtrunk_cfg_0006.html)[, configure an IP-Trunk interface,](dc_vrp_hdlc_ip-trunk_cfg_0008.html) or [configure an Eth-Trunk interface in static LACP mode](dc_vrp_ethtrunk_cfg_0013.html).
* Enable BFD globally.

If trunk-bit-error-triggered IGP route switching is configured, complete either of the following tasks based on a used IGP:

* [Configure basic IPv4 IS-IS functions.](dc_vrp_isis_cfg_1000.html)
* [Configure basic OSPF functions.](dc_vrp_ospf_cfg_0003.html)

#### Procedure

1. Enable bit error detection on each trunk member interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The trunk member interface view is displayed.
   3. Enable bit error detection, and configure bit error alarm thresholds on the interface.
      
      
      * If trunk-bit-error-triggered section switching is configured, run the [**trap-threshold crc-error packet-error-ratio**](cmdqueryname=trap-threshold+crc-error+packet-error-ratio) **alarm-threshold** *coef-value* *pow-value* [ **resume-threshold** *rsm-coef-value* *rsm-pow-value* ] [ **trigger-lsp** | **trigger-section** ] command to enable bit error detection on the interface and set BER thresholds for triggering bit error alarms.
        
        To enable bit-error-triggered trunk update to take effect, you must specify the switching type, either **trigger-lsp** or **trigger-section**.
      * If trunk-bit-error-triggered IGP route switching is configured, run the [**link-quality**](cmdqueryname=link-quality) **low** **bit-error-threshold** **error-ratio** *trigger-coefficient* *trigger-power* **resume-ratio** *recovery-coefficient* *recovery-power* command to enable bit error detection on the interface and set BER thresholds for determining link quality.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Enable bit error detection on a trunk interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run either of the following commands:
      
      
      * Run the [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id* command to enter the view of an Eth-Trunk interface.
      * Run the [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id* command to enter the view of an IP-Trunk interface.
   3. Run [**bit-error-detection**](cmdqueryname=bit-error-detection)
      
      
      
      Bit error detection is enabled on the trunk interface.
   4. (Optional) If trunk-bit-error-triggered IGP route switching is configured, perform the following operations depending on a used IGP:
      
      
      
      If IS-IS is used:
      
      1. Run the [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ] command to enable the IS-IS function on the interface.
      2. Run the [**isis link-quality**](cmdqueryname=isis+link-quality) **low** **incr-cost** { *cost* | **max-reachable** } command to enable the IS-IS interface to automatically adjust the link cost based on link quality.
      
      If OSPF is used:
      
      1. Run the [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id* command to enable the OSPF function on the interface.
      2. Run the [**ospf link-quality low incr-cost**](cmdqueryname=ospf+link-quality+low+incr-cost) { *cost* | **max-reachable** } command to enable the OSPF interface to automatically adjust the link cost based on link quality.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
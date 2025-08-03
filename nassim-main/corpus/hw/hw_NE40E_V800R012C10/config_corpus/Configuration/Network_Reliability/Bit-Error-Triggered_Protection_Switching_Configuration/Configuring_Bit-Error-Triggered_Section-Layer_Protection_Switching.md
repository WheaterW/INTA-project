Configuring Bit-Error-Triggered Section-Layer Protection Switching
==================================================================

This section describes how to configure bit-error-triggered section switching.

#### Usage Scenario

Bit errors caused by optical fiber aging or optical signal jitter may exist on carrier networks. These bit errors may result in the interruption of services with high quality requirements. In a scenario in which services travel along an LDP LSP and LDP auto fast reroute (FRR) is configured for the LDP LSP, you can configure bit-error-triggered LDP LSP switching to protect services against bit errors.

To do so, you only need to enable bit error detection on interfaces along the primary and backup paths of the LDP LSP and set the switching type of each interface as trigger-section. If an interface encounters a bit error event after you configure bit-error-triggered LDP LSP switching, the interface changes its status to Down and triggers route convergence, which in turn triggers LDP LSP switching.


#### Pre-configuration Tasks

Before configuring bit-error-triggered section switching, complete the following tasks:

* Enable BFD globally.
* [Configure LDP auto FRR](../vrp/dc_vrp_ldp-p2p_cfg_0049.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The views of the interfaces along the primary and backup paths of the LDP LSP are displayed.
3. Run [**trap-threshold crc-error packet-error-ratio**](cmdqueryname=trap-threshold+crc-error+packet-error-ratio) **alarm-threshold** *coef-value pow-value* [ **resume-threshold** *rsm-coef-value* *rsm-pow-value* ] [[**trigger-lsp**](cmdqueryname=trigger-lsp) | **trigger-section**]
   
   
   
   Bit error detection is enabled, and the thresholds for triggering bit error event alarms are set.
   
   
   
   To enable bit-error-triggered LDP LSP switching to take effect, you must specify **trigger-section**.
   
   To enable bit-error-triggered trunk update to take effect, you must specify the switching type, either **trigger-lsp** or **trigger-section**.
   
   The **alarm-threshold** value equals *alarm-coe* multiplied by 10-*alarm-pow*. If the BER detected by a trunk member interface exceeds the **alarm-threshold** value, the trunk member interface reports an alarm indicating that a bit error event has occurred.
   
   The **resume-threshold** value equals *resume-coe* multiplied by 10-*resume-pow*. If the BER detected by a trunk member interface falls below the **resume-threshold** value, the trunk member interface reports an alarm indicating that the bit error event is over.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The **resume-threshold** value cannot be greater than the **alarm-threshold** value.
   * If you do not specify the **resume-threshold** value, the system automatically uses tenth of the **alarm-threshold** value as the **resume-threshold** value.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After an interface along the primary or backup paths of an LDP LSP encounters a bit error event, run the following commands to check the configurations:

* Run the [**display interface**](cmdqueryname=display+interface) *interface-type* *interface-number* command. The command output shows that the link protocol status of the interface that has encountered the bit error event is **DOWN(bit-error-detection down)**.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command. The command output shows LDP LSP configurations.
* Before a bit error event occurs, run the [**tracert lsp**](cmdqueryname=tracert+lsp) **ip** *destination-address* *mask-length* command. The command output shows that the LDP LSP uses the primary path to transmit services.
* After a bit error event occurs, run the [**tracert lsp**](cmdqueryname=tracert+lsp) **ip** *destination-address* *mask-length* command. The command output shows that the LDP LSP uses the backup path to transmit services.
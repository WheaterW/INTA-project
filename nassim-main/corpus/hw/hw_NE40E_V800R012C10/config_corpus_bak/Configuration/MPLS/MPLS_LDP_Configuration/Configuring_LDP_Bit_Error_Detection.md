Configuring LDP Bit Error Detection
===================================

LDP bit error detection enables a device to detect bit errors on LDP LSPs and trigger VPN service switchovers, which improves service reliability.

#### Usage Scenario

When LDP LSPs are established to transmit services with high quality requirements, bit errors on LSPs may cause service interruptions. To detect bit errors, run the corresponding command for LDP LSPs. If a node on an LSP detects bit errors, LDP notifies the VPN services of the bit error rate and triggers a service switchover, which guarantees service quality.


#### Pre-configuration Tasks

Before configuring LDP bit error detection, complete the following task:

* [Configure LDP LSPs.](dc_vrp_ldp-p2p_cfg_0015.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bit-error-detection level**](cmdqueryname=bit-error-detection+level+threshold+switch+resume) *level-number* **threshold** **switch** *switch-coe* *switch-pow* **resume** *resume-coe* *resume-pow*
   
   
   
   A level is set for LDP bit error rate thresholds.
   
   
   
   A maximum of three levels can be set for bit error rate thresholds. The parameter description is as follows:
   
   | Parameter | Description | Value |
   | --- | --- | --- |
   | *level-number* | Specifies the level value for LDP bit error rate thresholds. | The value is an integer ranging from 1 to 3. |
   | **switch** *switch-coe* *switch-pow* | Specifies an LDP bit error rate threshold for triggering a service switchover. Switchover threshold = *switch-coe* Ã 10-*switch-pow* The *switch-coe* parameter specifies the protection switchover coefficient, and the *switch-pow* parameter specifies the protection switchover power. | The *switch-coe* value is an integer ranging from 1 to 9.  The *switch-pow* value is an integer ranging from 1 to 7. |
   | **resume** *resume-coe* *resume-pow* | Specifies an LDP bit error rate threshold for triggering a service switchback. Switchback threshold = *resume-coe* Ã 10-*resume-pow* The *resume-coe* parameter specifies the protection switchback coefficient, and the *resume-pow* parameter specifies the protection switchback power.  NOTE:  The switchback threshold must be smaller than or equal to the switchover threshold. | The *resume-coe* value is an integer ranging from 1 to 9.  The *resume-pow* value is an integer ranging from 1 to 7. |
3. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
4. Run [**bit-error-detection**](cmdqueryname=bit-error-detection+level) **level** *level-number*
   
   
   
   LDP bit error detection is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configuration, you can run the following command to verify the configuration.

* Run the [**display mpls ldp adjacency**](cmdqueryname=display+mpls+ldp+adjacency+interface+remote+peer+verbose) [ **interface** *interface-type* *interface-number* | **remote** ][ **peer** *peer-id* ] **verbose** command to check the bit error rate of LDP.
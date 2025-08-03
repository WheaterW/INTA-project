Configuring Mutual Protection Between an LDP VC and a CCC VC
============================================================

This section describes how to configure mutual protection between an LDP VC and a CCC VC. If a CCC VC (or LDP VC) functioning as the primary path fails, traffic is switched to the LDP VC (CCC VC) functioning as the backup path, improving reliability.

#### Usage Scenario

Widespread L2VPN adoption has raised reliability requirements for L2VPNs, especially for L2VPNs that carry real-time services such as VoIP and IPTV.

To improve service reliability, you can configure an LDP VC to protect a CCC VC. If the CCC VC functioning as the primary path fails, traffic can be switched to the LDP VC functioning as the backup path.

Similarly, you can also configure a CCC VC to protect an LDP VC. If the LDP VC functioning as the primary path fails, traffic can be switched to the CCC VC functioning as the backup path.

Mutual protection between an LDP VC and a CCC VC applies to the following scenarios:

* Dual-homing 2PE scenario: On the network shown in [Figure 1](#EN-US_TASK_0172369844__fig_dc_vrp_vpws_cfg_607201), CE1 is dual-homed to PE1 and PE2 through an Eth-Trunk, and AC1 is selected as the active AC. CE2 is dual-homed to PE1 and PE2 through another Eth-Trunk, and AC3 is selected as the active AC. PW1 VC1 is deployed between PE1 and PE2 to protect AC3. If AC3 fails, CE1 can access CE2 through PW1 VC1 and AC4. PW2 VC1 is deployed between PE1 and PE2 to protect AC1. If AC1 fails, CE2 can access CE1 through PW2 VC1 and AC2. Therefore, CE1 and CE2 both use AC1 and AC3 for primary links and AC2 and AC4 for backup links. If the primary link fails, service data can be transmitted over the backup link.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If a CE and PEs support low-speed interfaces, the CE can be dual-homed to PEs through a CPOS-Trunk interface.
  
  
  **Figure 1** Mutual protection between an LDP VC and a CCC VC (dual-homing 2PE scenario)  
  ![](images/fig_dc_vrp_vpws_cfg_607201.png)
* Dual-homing 3PE scenario: On the network shown in [Figure 2](#EN-US_TASK_0172369844__fig_dc_vrp_vpws_cfg_607202), CE1 is dual-homed to PE1 and PE2 through an Eth-Trunk. AC1 serves as the primary path, and AC2 the backup path. CE2 is dual-homed to PE2 and PE3 through another Eth-Trunk. AC3 serves as the primary path, and AC4 the backup path. The independent PW redundancy mode is configured on PE1, with PW1 VC1 being the primary PW and PW2 VC1 the secondary PW. The independent PW redundancy mode is also configured on PE3, with PW2 VC2 being the primary PW and PW3 VC1 being the secondary PW. For AC1, there are two paths to CE2: PW1 VC1 (primary) and PW2 VC1 (backup). For AC2, there are two paths to CE2: AC3 (primary) and PW3 VC2 (backup). If the primary path fails, service data can be transmitted over the backup path.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If a CE and PEs support low-speed interfaces, the CE can be dual-homed to PEs through a CPOS-Trunk interface.
  
  
  **Figure 2** LDP VC protecting CCC VC (dual-homing 3PE scenario)  
  ![](images/fig_dc_vrp_vpws_cfg_607202.png)

**Table 1** Mutual protection between an LDP VC and a CCC VC
| Scenario | Key Configurations |
| --- | --- |
| Dual-homing 2PE scenario | LDP VC protecting CCC VC  * Configure a primary PW (CCC VC) on PE1. * Configure a secondary (bypass) PW on PE1 to protect the CCC VC.  CCC VC protecting LDP VC  * Configure a primary PW (LDP VC) on PE1. * Configure a secondary PW (CCC VC) on PE1 to protect the primary PW (LDP VC). |
| Dual-homing 3PE scenario | LDP VC protecting CCC VC  * Configure a primary PW (CCC VC) on PE2. * Configure a secondary (bypass) PW on PE1 to protect the CCC VC. * Configure PW redundancy on PE1 and PE3.  CCC VC protecting LDP VC  * Configure a primary PW on PE1. * Configure a secondary PW (CCC VC) on PE2 to protect the primary PW (LDP VC). * Configure PW redundancy on PE1 and PE3. |

#### Pre-configuration Tasks

Before configuring mutual protection between an LDP VC and a CCC VC, complete the following tasks:

* Configure PW status negotiation. You can configure E-Trunk or VRRP to determine the primary/secondary status of PWs.
* Configure static routing or an IGP for the PEs and Ps on the MPLS backbone network to implement IP connectivity.
* Configure basic MPLS functions on the PEs and Ps of the MPLS backbone network.
* Establish tunnels between PEs based on tunnel policies. If no tunnel policy is configured, LDP tunnels are established by default.



#### Procedure

1. Configure MPLS L2VPN.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to configure MPLS L2VPN.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
2. Create a CCC VC.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ] command to enter the AC interface view.
   2. Run the [**mpls ccc**](cmdqueryname=mpls+ccc) [ **instance-name** *instance-name* ] **out-interface** *interface-type* *interface-number* [ [ **ip-interworking** | **ip-layer2** | **raw** | **tagged** ] | [ **access-port** ] ] \* command to create a primary CCC VC.
   3. (Optional) Run the [**mpls ccc**](cmdqueryname=mpls+ccc) **out-interface** *interface-type* *interface-number* [ [ **ip-interworking** | **ip-layer2** | **raw** | **tagged** ] | [ **access-port** ] | [ **secondary** ] ] \* command to create a secondary CCC VC.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you specify the **secondary** keyword, a secondary CCC VC is created. If this keyword is not specified, the created CCC will be a primary VC.
3. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking** ] | **access-port** | [ **secondary** | **bypass** ] | **ignore-standby-state** ] \* command to create a PW.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you specify the **secondary** or **bypass** keyword, a backup VC is created. If this keyword is not specified, a primary VC is created.
4. (Optional) Run the [**mpls l2vpn pw ignore-ac-state**](cmdqueryname=mpls+l2vpn+pw+ignore-ac-state) [ **secondary** | **bypass** ] command for the PW to ignore the impact of AC status changes on PW service status.
   
   
   
   If you want an LDP-based bypass PW to ignore AC status changes, specify the **bypass** keyword.
   
   If you want an LDP-based secondary PW to ignore AC status changes, also specify the **secondary** keyword.
   
   In reliability scenarios where an LDP VC protects a local CCC VC, if an AC interface goes down, the PW status changes to down accordingly. When the AC interface recovers, the PW needs to be re-established. If a primary/secondary PW switchover is performed in this case, traffic is switched back to the primary PW only after PW status negotiation is complete. As a result, the switchback performance is poor. To improve switchback performance, run the [**mpls l2vpn pw ignore-ac-state**](cmdqueryname=mpls+l2vpn+pw+ignore-ac-state) command. After this command is run, the PW remains up after the AC interface goes down. After the AC interface recovers, the PW does not need to be re-established, enhancing switchback performance.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring mutual protection between an LDP VC and a CCC VC, verify the configuration.

* Run the [**display mpls l2vpn vpws**](cmdqueryname=display+mpls+l2vpn+vpws) [ **interface** *interface-type interface-number* [ **verbose** ] ] command to check VPWS PW information.
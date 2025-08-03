(Optional) Configuring a Secondary VPWS Connection
==================================================

This section describes how to configure a secondary VPWS connection for VLL FRR, so that L2VPN traffic can be quickly switched to the backup path if the primary path fails. After the primary path recovers, the L2VPN traffic can be switched back to it according to the corresponding revertive switching policy.

#### Context

A secondary VPWS connection is mainly used in the following networking modes:

* CEs symmetrically dual-homed to PEs
  
  Two communication paths exist between the CEs on the two ends of the VC. One is the primary PW path, and the other is the secondary PW path.
* CEs asymmetrically connecting to PEs
  
  **Figure 1** CEs asymmetrically connecting to PEs  
  ![](images/fig_dc_vrp_vpws_cfg_500201.png)  
  
  On the network shown in [Figure 1](#EN-US_TASK_0172369803__fig_dc_vrp_vpws_cfg_500201), a pair of primary and secondary PWs need to be configured on PE1. Only one PW needs to be configured on PE2 and another on PE3. Therefore, PE2 and PE3 do not determine whether their PW is a primary or secondary one.
  
  The CE on one end of the VC accesses a higher-reliability PE over a single reliable link. The CE on the other end is dual-homed to lower-reliability PEs. The two CEs can communicate over two paths. The higher-reliability path serves as the primary path, and the lower-reliability path serves as the backup path.
  
  In a scenario where CEs asymmetrically connect to PEs, configure both primary and secondary PWs. The primary and secondary PWs must be of the same type.
  
  In addition, the interface used by the singled-homed CE to connect to the corresponding PE requires both primary and secondary IP addresses. If the primary path is available, the CE uses the primary IP address to communicate with the remote CE. If a fault occurs on the primary path, this CE uses the secondary IP address to communicate with the remote CE.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the IP addresses of AC interfaces used to connect to CEs at both ends of a PW are on different network segments, the AC type must be PPP. In this case, the [**ppp peer hostroute-suppress**](cmdqueryname=ppp+peer+hostroute-suppress) command cannot be used.
  
  On a network where CEs asymmetrically connect to PEs, the secondary PW does not transmit data when the primary and backup paths both work properly. If the secondary PW AC interface borrows the IP address of the primary PW AC interface, the following situations arise:
  
  + Non-revertive switching cannot be configured.
  + The local CE has two equal-cost direct routes to the remote CE, with both routes having the same destination address and same next hop. The route that passes through the secondary PW is actually an invalid route.
  + If CEs exchange routing information using routing protocols, you need to change the cost or metric of the backup path AC interface to be greater than that of the primary path AC interface. In this case, the local CE may fail to communicate with the remote CE, but can communicate with other user devices on the remote end.
  + If CEs use static routes to exchange routing information, ensure that the preference of the backup route is lower than that of the primary route (a larger value indicates a lower preference). To do so, run the [**ip route-static**](cmdqueryname=ip+route-static) *dest-ip-address* *mask* *out-interface* **preference** *preference-value* command.
  
  Perform the following steps on the PE to which a CE is single-homed:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The AC interface view is displayed.
5. Run one of the following commands to create a secondary VPWS connection according to the interface type:
   
   
   * Ethernet interface:
     
     [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **access-port** | [ **control-word** | **no-control-word** ] | **ignore-standby-state** | [ **raw** | **tagged** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **secondary** ]\*
   * PPP/HDLC interface:
     
     [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **access-port** | [ **control-word** | **no-control-word** ] | **ignore-standby-state** | [ **raw** | **tagged** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **secondary** ]\*
   * ATM interface:
     
     [**mpls l2vc**](cmdqueryname=mpls+l2vc){ *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | [ **seq-number** ] | **no-control-word** ] | **max-atm-cells** *cells-value* | **atm-pack-overtime** *atm-pack-overtime* | **transmit-atm-cells** *transmit-atm-cell-value* | **ignore-standby-state** | **secondary** ] \*
   * TDM interface:
     
     [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation-number** *number* ] | [ **tdm-sequence-number** ] | [ **rtp-header** ] | **ignore-standby-state** | **secondary** ] \*
   
   
   
   When configuring a secondary VPWS PW, ensure that the parameter settings for the primary, secondary, and bypass PWs are consistent. Parameter setting inconsistencies may result in the secondary or bypass PW failing to take over traffic if the primary PW fails.
   
   In the scenario where CEs asymmetrically connect to PEs, note the following:
   
   * Only the PE to which a CE is single-homed requires the configuration of both the primary and secondary PWs. The PEs to which a CE is dual-homed require only the configuration of the primary PW.
   * The control word configurations for the primary and secondary PWs must be the same. Otherwise, a large number of packets will be lost after a primary/secondary PW switchover.
   * If CEs connect to PEs over PPP/HDLC links:
     
     + PEs can only have heterogeneous interworking configured.
     + The interface connecting CE1 to PE1 can be configured with both primary and secondary IP addresses. The primary PW forwards packets to the primary IP address, and the secondary PW forwards packets to the secondary IP address.
     + CEs can advertise routes to each other using OSPF. OSPF, however, cannot advertise routes destined for the secondary IP address.
6. (Optional) Run [**undo interface-parameter-type vccv**](cmdqueryname=undo+interface-parameter-type+vccv)
   
   
   
   The function to delete the VCCV byte (an interface parameter) from the Label Mapping message is enabled.
   
   
   
   Run this command if LDP VPWS is configured for a device running VRP V800R005 or later and this device communicates with another device running VRP V300R001 or any branch version of VRP V300R001.
7. (Optional) Run [**mpls l2vpn service-name**](cmdqueryname=mpls+l2vpn+service-name) *service-name*
   
   
   
   An L2VPN service name is specified. The L2VPN service can then be maintained through an NMS based on the specified name.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
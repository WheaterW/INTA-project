Configuring VPWS Heterogeneous Interworking
===========================================

If AC types at the two ends of a VPWS PW are different, configure VPWS heterogeneous interworking for the two CEs to communicate.

#### Context

Determine which configuration procedure to use based on the following guidelines:

* If the two CEs use non-Ethernet link types, perform Steps 1 to 8 and Step 11.
* If one of the two CEs uses the Ethernet or VLAN link type, performing Steps 9 to 11 is also required on the local PE.
  
  If the PE has not learned the MAC address of the local CE (neither dynamically learned nor statically configured) and the broadcast mode is not enabled, the PE will discard all the IP packets received from the remote PE. To prevent this situation, configure the IP or MAC address of the local CE on the local PE, and configure an interface IP address of the remote CE on the remote PE.

Perform the following configurations on the endpoint PEs of a PW.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is configured.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The AC interface view is displayed.
5. Run the following command to create a VPWS connection according to the interface type:
   
   
   * Ethernet/PPP/HDLC interface:
     
     [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
   * Set the **ip-interworking** parameter for heterogeneous interworking between Huawei devices.
   * Set the **ip-layer2** parameter for heterogeneous interworking between Huawei and non-Huawei devices.
6. (Optional) Run [**undo interface-parameter-type vccv**](cmdqueryname=undo+interface-parameter-type+vccv)
   
   
   
   The function to delete the VCCV byte from the Label Mapping message is enabled.
   
   
   
   Run this command if LDP VPWS is configured for a device running VRP V800R005 or later and this device communicates with another device running VRP V300R001 or any branch version of VRP V300R001.
7. (Optional) Run [**mpls l2vpn service-name**](cmdqueryname=mpls+l2vpn+service-name) *service-name*
   
   
   
   An L2VPN service name is specified. The L2VPN service can then be maintained through an NMS based on the specified name.
8. (Optional) Run [**local-ce mac**](cmdqueryname=local-ce+mac) *mac-address* or [**local-ce ip**](cmdqueryname=local-ce+ip) *ip-address*
   
   
   
   An Ethernet interface MAC address or IP address is configured for each local CE.
   
   
   
   * If the Ethernet interface MAC addresses of local CEs are configured, the PE uses the configured MAC addresses as the destination MAC addresses when sending IP packets to local CEs.
   * If the Ethernet interface IP addresses of local CEs are configured, if the PE can find neither statically configured nor dynamically learned MAC addresses of local CEs, the PE uses the configured IP addresses as the destination IP addresses to send ARP Request packets to local CEs.
9. (Optional) Run [**local-ce mac broadcast**](cmdqueryname=local-ce+mac+broadcast)
   
   
   
   The PE is configured to use a broadcast address as the destination MAC address to send packets to local CEs.
   
   
   
   If neither command in the preceding step is run, perform this step for the PE to use a broadcast address as the destination MAC address to send packets to local CEs.
10. (Optional) Run [**remote-ce ip**](cmdqueryname=remote-ce+ip) *ip-address*
    
    
    
    The IP address of the remote CE relayed by the specified interface is configured.
    
    
    
    In VPWS heterogeneous interworking, if multiple PWs are established on sub-interfaces of the PE, configure this command on each sub-interface to specify the IP address of the remote CE relayed by each sub-interface. This configuration is necessary for P2MP communication between CEs.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

If the VLAN ID of a CE interface connected to the PE changes or a CE uses another interface to connect to the PE, run the [**reset local-ce mac**](cmdqueryname=reset+local-ce+mac) [ *interface-type* *interface-number* ] command in the user view to clear MAC address and VLAN ID information, so that the PE can re-learn interface information about the CE.
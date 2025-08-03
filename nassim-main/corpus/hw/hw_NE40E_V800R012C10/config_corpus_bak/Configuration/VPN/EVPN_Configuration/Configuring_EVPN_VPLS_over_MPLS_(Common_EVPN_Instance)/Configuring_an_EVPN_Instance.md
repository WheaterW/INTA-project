Configuring an EVPN Instance
============================

You can configure EVPN instances on PEs to manage EVPN routes.

#### Context

EVPN instances are used to isolate EVPN routes from public routes and isolate the routes of EVPN instances from each other.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name*
   
   
   
   An EVPN instance is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the EVPN instance.
   
   Similar to a hostname or an interface description, an EVPN instance description helps you memorize the EVPN instance.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the EVPN instance.
   
   
   
   An EVPN instance takes effect only after an RD is configured for it. The RDs of different EVPN instances on a PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you need to create a large number of EVPN instances and plan a large number of RDs, you can run the **evpn route-distinguisher auto** *rd-ip* command in the system view to enable automatic RD allocation, thereby avoiding RD conflicts. The *rd-ip* parameter specifies an IPv4 address, enabling a device to allocate RDs in the format of *X.X.X.X*:*index* to all EVPN instances that are not allocated RDs. *X.X.X.X* indicates a user-defined RD-IP value, and *index* is a 2-byte value automatically allocated by the system in the range from 1 to 65535.
5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   One or multiple VPN targets are configured for the EVPN instance.
   
   VPN targets are BGP extended community attributes used to control the acceptance and advertisement of EVPN routes. A maximum of eight import VPN targets and eight export VPN targets can be configured each time the [**vpn-target**](cmdqueryname=vpn-target) command is run. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command multiple times.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An RT of an Ethernet segment route is generated using the middle six bytes of an ESI. For example, if the ESI is 0011.1001.1001.1001.1002, the Ethernet segment route uses 11.1001.1001.10 as its RT.
6. (Optional) Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **export**
   
   
   
   The EVPN instance is configured to filter MAC advertisement routes to be advertised.
   
   To precisely control EVPN routes, an export route-policy must be configured. An export route-policy filters routes before they are sent to other PEs.
7. (Optional) Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **import**
   
   
   
   The EVPN instance is configured to filter received MAC advertisement routes.
   
   To precisely control EVPN routes, an import route-policy must be configured. An import route-policy filters routes that are received from other PEs.
8. (Optional) Run [**mac limit**](cmdqueryname=mac+limit) *number* [ **simply-alert** | **mac-unchanged** ]
   
   
   
   The maximum number of MAC addresses allowed in the EVPN instance is set.
   
   A device consumes more system resources as it learns more MAC addresses, meaning that the device may fail to operate when busy processing services. To limit the maximum number of MAC addresses allowed in an EVPN instance and thereby improve device security and reliability, run the [**mac limit**](cmdqueryname=mac+limit) command. After this configuration, if the number of MAC addresses exceeds the preset value, an alarm is triggered to prompt you to check the validity of existing MAC addresses.
   
   After the maximum number of MAC addresses allowed by an EVPN instance is configured, you can run the [**mac threshold-alarm**](cmdqueryname=mac+threshold-alarm) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* command to configure alarm thresholds for MAC addresses allowed by the EVPN instance. The alarm generation and clearance help a device detect threshold-crossing events of MAC addresses.
9. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   The EVPN instance is associated with a tunnel policy.
   
   This configuration enables PEs to use TE tunnels to transmit data packets.
10. (Optional) Run [**isolate spoken**](cmdqueryname=isolate+spoken)
    
    
    
    The forwarding isolation function is enabled for the EVPN instance.
    
    
    
    When users with the same service are bound to the same EVPN instance, you can configure the forwarding isolation function for the EVPN instance to prevent mutual access between them.
11. (Optional) Run [**control-word enable**](cmdqueryname=control-word+enable)
    
    
    
    The control word function is enabled for the EVPN instance.
    
    In load balancing mode, out-of-order packets may be generated when the device performs in-depth parsing on MPLS packets. In this case, you can enable the control word function in the EVPN instances on both ends to reassemble MPLS packets.
12. (Optional) Run [**reserve-interface fast-switch enable**](cmdqueryname=reserve-interface+fast-switch+enable)
    
    
    
    The reserve-interface fast switching function is enabled.
    
    When the active interface board fails, you can perform this step to enable reserve-interface fast switching, so that broadcast traffic can be quickly switched to the standby interface board.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
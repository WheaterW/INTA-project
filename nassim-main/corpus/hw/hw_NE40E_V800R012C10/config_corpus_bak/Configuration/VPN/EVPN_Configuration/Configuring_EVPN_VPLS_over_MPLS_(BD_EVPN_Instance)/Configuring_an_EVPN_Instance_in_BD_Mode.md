Configuring an EVPN Instance in BD Mode
=======================================

To implement service access based on a BD and manage EVPN routes, configure BD EVPN instances on PEs.

#### Context

EVPN instances are used to isolate EVPN routes from public routes and isolate the routes of EVPN instances from each other.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
   
   
   
   A BD EVPN instance is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the EVPN instance.
   
   Similar to a hostname or an interface description, an EVPN instance description helps you memorize the EVPN instance.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the EVPN instance.
   
   
   
   An EVPN instance takes effect only after an RD is configured for it. The RDs of different EVPN instances on a PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you need to create a large number of EVPN instances and plan a large number of RDs, you can run the **evpn route-distinguisher auto** *rd-ip* command in the system view to enable automatic RD allocation, thereby avoiding RD conflicts. The *rd-ip* parameter specifies an IPv4 address, enabling a device to allocate RDs in the format of *X.X.X.X*:*index* to all EVPN instances that are not allocated RDs. *X.X.X.X* indicates a user-defined RD-IP value, and *index* is a 2-byte value automatically allocated by the system in the range from 1 to 65535.
5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   One or multiple VPN targets are set for the EVPN instance.
   
   
   
   VPN targets are BGP extended community attributes used to control the acceptance and advertisement of EVPN routes. A maximum of eight import VPN targets and eight export VPN targets can be configured each time the [**vpn-target**](cmdqueryname=vpn-target) command is run. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command multiple times.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An RT of an Ethernet segment route is generated using the middle 6 bytes of an ESI. For example, if the ESI is 0011.1001.1001.1001.1002, the Ethernet segment route uses 11.1001.1001.10 as its RT.
6. (Optional) Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **export**
   
   
   
   The EVPN instance is configured to filter MAC advertisement routes to be advertised.
   
   To precisely control EVPN routes, an export route-policy must be configured. An export route-policy filters routes that are to be advertised to other PEs.
7. (Optional) Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **import**
   
   
   
   The EVPN instance is configured to filter received MAC advertisement routes.
   
   To precisely control EVPN routes, an import route-policy must be configured. An import route-policy filters routes that are received from other PEs.
8. (Optional) Run [**mac limit**](cmdqueryname=mac+limit) *number* [ **simply-alert** | **mac-unchanged** ]
   
   
   
   The maximum number of MAC addresses allowed in the EVPN instance is set.
   
   
   
   A device consumes more system resources as it learns more MAC addresses, meaning that the device may fail to operate when busy processing services. To limit the maximum number of MAC addresses allowed in an EVPN instance and thereby improve device security and reliability, run the [**mac limit**](cmdqueryname=mac+limit) command. After this configuration, if the number of MAC addresses exceeds the preset value, an alarm is triggered to prompt you to check the validity of existing MAC addresses.
   
   After the maximum number of MAC addresses allowed by an EVPN instance is configured, you can run the [**mac threshold-alarm**](cmdqueryname=mac+threshold-alarm) **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* command to configure an alarm threshold for MAC addresses allowed by the EVPN instance. The alarm generation and clearance help a device detect threshold-crossing events of MAC addresses.
9. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   The EVPN instance is associated with a tunnel policy.
   
   This configuration enables PEs to use TE or SR tunnels to transmit data packets.
10. (Optional) Run [**bypass-vxlan**](cmdqueryname=bypass-vxlan) **disable**
    
    
    
    The inter-chassis VXLAN function is disabled for the instance.
    
    
    
    After the [**bypass-vxlan enable**](cmdqueryname=bypass-vxlan+enable) command is run globally, only EVPN VXLAN functions can be deployed on the device. If you want to configure EVPN MPLS functions for some BD EVPN instances, perform this step.
11. (Optional) Run [**control-word enable**](cmdqueryname=control-word+enable)
    
    
    
    The control word function is enabled for the EVPN instance.
    
    In load balancing mode, out-of-order packets may be generated when the device performs in-depth parsing on MPLS packets. In this case, you can enable the control word function in the EVPN instances on both ends to reassemble MPLS packets.
12. (Optional) Run [**mac-route no-advertise**](cmdqueryname=mac-route+no-advertise)
    
    
    
    The device is disabled from sending local MAC routes to its EVPN peer.
    
    
    
    In scenarios that do not involve Layer 2 traffic forwarding, perform this step to disable local MAC routes from being advertised to the EVPN peer. This configuration prevents the EVPN peer from receiving MAC routes, thereby conserving device resources.
13. (Optional) Run [**local mac-only-route no-generate**](cmdqueryname=local+mac-only-route+no-generate)
    
    
    
    The device is disabled from generating EVPN MAC routes when the local MAC address exists in both a MAC address entry and an ARP/ND entry.
    
    
    
    If a MAC address entry and an ARP/ND entry on the device both contain the local MAC address, the device generates both an EVPN MAC/IP route and an EVPN MAC route by default. To optimize memory utilization, perform this step so that the device generates only EVPN MAC/IP routes. To ensure normal Layer 2 traffic forwarding, also run the [**mac-ip route generate-mac**](cmdqueryname=mac-ip+route+generate-mac) command on the peer device to enable the function to generate MAC entries based on MAC/IP routes.
14. (Optional) Run [**mac-ip route generate-mac**](cmdqueryname=mac-ip+route+generate-mac)
    
    
    
    The function to generate MAC address entries based on MAC/IP routes is enabled.
    
    If the peer device is configured not to advertise MAC routes (using the **mac-route no-advertise** command) or not to generate MAC routes (using the [**local mac-only-route no-generate**](cmdqueryname=local+mac-only-route+no-generate) command), the local device cannot generate MAC entries by default. To ensure normal Layer 2 traffic forwarding, perform this step on the local device to enable the function to generate MAC entries based on MAC/IP routes.
15. (Optional) Run [**mac-keep disable**](cmdqueryname=mac-keep+disable)
    
    
    
    The device is disabled from retaining MAC routes.
    
    In the MAC route withdrawal process, the device retains original MAC routes for a period of time by default after receiving MAC Withdraw messages. This function is used in fault recovery and switchback scenarios to prevent MAC route flapping. In the following scenarios, however, you need to perform this step on the remote PE to disable the remote PE from retaining MAC addresses:
    
    * Interworking between traditional VPLS and EVPN VPLS
    * Dual-homing access to EVPN through Eth-Trunk interfaces (LACP)
    * No upstream traffic from a CE to two PEs when the CE is dual-homed to the two PEs
    
    In the preceding scenario, when the fault is rectified and services are switched back, the device on the backup path clears the MAC address, whereas the remote PE maintains the MAC address by default. As a result, traffic is still diverted to the device on the backup path, causing traffic loss.
16. (Optional) Run [**timer revert delay**](cmdqueryname=timer+revert+delay) *delay-value*
    
    
    
    A switchback delay is set.
    
    
    
    In dual-homing scenarios, if a fault on the access-side link of the active PE or the active PE is rectified, the active PE generates MAC routes and advertises these routes to the remote PE through a BGP EVPN peer relationship. After receiving the MAC routes and generating forwarding entries, the remote PE switches traffic from the path destined for the standby PE to the path destined for the active PE. In this case, a few packets may be lost on the active PE because some forwarding entries are not generated. To prevent this problem, run the **timer revert delay** *delay-value* command on the remote PE to configure a proper switchback delay. After receiving MAC routes, the remote PE delays generating forwarding entries. Specifically, the remote PE generates forwarding entries only after the forwarding entries on the active PE become stable. After the delay timer expires, the remote PE generates new forwarding entries and sends traffic to the active PE, preventing packet loss.
17. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
Configuring the Peer-Link
=========================

Configuring the Peer-Link

#### Context

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ, the device provides the physical peer-link solution and virtual peer-link solution. The peer-link of the former is an Eth-Trunk that directly connects two M-LAG member devices, and the peer-link of the latter is a static bypass VXLAN tunnel between two M-LAG member devices.

For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE6885-LL (low latency mode), the device provides the physical peer-link solution in which an Eth-Trunk that directly connects two M-LAG member devices is used as the peer-link.

The peer-link is used to achieve the following:

* Transmit DFS group protocol packets.
* Transmit synchronization packets used for synchronizing MAC address entries and ARP entries between M-LAG master and backup devices.
* Forward inter-device traffic sent from non-M-LAG member interfaces or traffic received from an M-LAG member interface when downstream devices are single-homed to the M-LAG due to a fault.

![](../public_sys-resources/note_3.0-en-us.png) 

If the **peer** *ip-address* parameter for DAD has been configured, run the **[**display dfs-group heartbeat**](cmdqueryname=display+dfs-group+heartbeat)** command to check the heartbeat status. Configure the peer-link only when the heartbeat status is OK to prevent interfaces on one M-LAG member device from entering the error-down state incorrectly.



#### Procedure

* **Physical peer-link solution**
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the Eth-Trunk interface view.
     ```
     [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
     ```
  3. Add member interfaces to the Eth-Trunk interface.
     ```
     [trunkport](cmdqueryname=trunkport) interface-type { interface-number1 [ to interface-number2 ] } &<1-16>
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to configure at least two member interfaces for a peer-link interface.
  4. Configure the Eth-Trunk interface to work in static LACP mode.
     ```
     [mode](cmdqueryname=mode) [lacp-static](cmdqueryname=lacp-static)
     ```
     
     By default, an Eth-Trunk interface works in manual load balancing mode. To improve M-LAG reliability, you are advised to configure the Eth-Trunk interface to work in static LACP mode.
  5. Configure STP or VBST.
     + If the M-LAG is configured in root bridge mode, disable STP on the interface.
       ```
       [undo stp enable](cmdqueryname=undo+stp+enable)
       ```
     + If the M-LAG is configured in V-STP mode, enable STP on the interface.
       ```
       [stp enable](cmdqueryname=stp+enable)
       ```
     + If the M-LAG is configured in V-VBST mode, enable VBST on the interface.
       ```
       [stp enable](cmdqueryname=stp+enable)
       ```![](../public_sys-resources/note_3.0-en-us.png) 
     + In an M-LAG configured in root bridge mode, because the M-LAG master and backup devices need to be simulated into one root bridge, you need to disable STP on peer-link interfaces to ensure that the directly connected interfaces are not blocked.
     + In an M-LAG configured in V-STP mode, because the M-LAG master and backup devices need to exchange packets through the peer-link to perform STP virtualization calculation, you need to enable STP on peer-link interfaces. The STP configurations on the peer-link interfaces of the two devices must be the same.
     + In an M-LAG configured in V-VBST mode, because the M-LAG master and backup devices need to exchange packets through the peer-link to perform STP virtualization calculation, you need to enable VBST on peer-link interfaces.
  6. Configure the Eth-Trunk interface as the peer-link interface.
     ```
     [peer-link](cmdqueryname=peer-link) peer-linkid
     ```
     
     By default, an Eth-Trunk interface does not function as a peer-link interface.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + An interface configured as a peer-link interface is added to all VLANs by default. However, if a VLAN is bound to a BD, the peer-link interface is not added to the VLAN.
     + An interface configured as a peer-link interface cannot be configured with any other service.
     + If network-side VLANIF interfaces are configured on M-LAG member devices and establish a DAD link, perform [step 7](#EN-US_TASK_0000001512689654__li3280175251918) to remove peer-link interfaces from the VLANs corresponding to the VLANIF interfaces. Otherwise, DAD may fail.
     + If the **peer** *ip-address* parameter has been configured for DAD, you are advised to configure an Eth-Trunk interface in the up state as a peer-link interface. If you configure an Eth-Trunk interface in the down state as a peer-link interface, the peer-link interface is down. In this case, if the DAD heartbeat status is normal, interfaces on one M-LAG member device will enter the error-down state.
     + Each M-LAG member device has independent services, and MAC addresses learned in VLANs of these services do not need to be synchronized. In addition, M-LAG member devices independently maintain MAC addresses used to establish a VXLAN tunnel between them and do not synchronize the MAC addresses to each other. MAC address synchronization in this scenario causes MAC address flapping, resulting in loss of traffic forwarded through a peer-link interface when the physical peer-link solution is used. To prevent this problem, run the [**port vlan exclude**](cmdqueryname=port+vlan+exclude) command on the Eth-Trunk interface that functions as the peer-link interface to remove the Eth-Trunk interface from a VLAN. M-LAG synchronization then is not performed for the VLAN.
  7. (Optional) Configure the VLANs from which packets are not allowed to pass through the peer-link interface.
     ```
     [port vlan exclude](cmdqueryname=port+vlan+exclude) { { vlan-id1 [ to vlan-id2 ] } &<1-10> }
     ```
     
     By default, packets from all VLANs are allowed to pass through a peer-link interface.
  8. Exit the Eth-Trunk interface view.
     ```
     [quit](cmdqueryname=quit)
     ```
  9. (Optional) Configure a VLAN to contain only the peer-link interface.
     1. Create a VLAN and enter the VLAN view. If the VLAN has been created, the VLAN view is displayed.
        ```
        [vlan](cmdqueryname=vlan) vlan-id
        ```
        ![](../public_sys-resources/note_3.0-en-us.png) 
        
        Based on service requirements, you can also run the **vlan range** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command in the system view to create a temporary VLAN range and enter the VLAN range view.
     2. Configure the VLAN to contain only the peer-link interface so that packets from the VLAN can be forwarded only on the peer-link interface.
        ```
        [m-lag peer-link reserved](cmdqueryname=m-lag+peer-link+reserved)
        ```
        
        By default, a VLAN can contain a peer-link interface and other Layer 2 interfaces.
        
        ![](../public_sys-resources/note_3.0-en-us.png) 
        
        In a multicast over VXLAN scenario, as long as the receiver and multicast source are dual-homed to the two member devices in the same M-LAG, the VLANIF interface corresponding to the VLAN configured with the [**m-lag peer-link reserved**](cmdqueryname=m-lag+peer-link+reserved) command cannot be used to establish a bypass VXLAN tunnel, regardless of whether the receiver and multicast source are in the same VLAN. Otherwise, the receiver will receive redundant multicast traffic.
  10. Commit the configuration.
      ```
      commit
      ```
* **Virtual peer-link solution** (supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ)
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the NVE interface view.
     ```
     interface nve nve-number
     ```
  3. Create a static bypass VXLAN tunnel and specify the source and peer IP addresses.
     ```
     pip-source src-ip peer peer-ip bypass
     ```
     
     By default, no static bypass VXLAN tunnel is created between M-LAG member devices. An IPv4 or IPv6 tunnel can be configured. IPv4 and IPv6 tunnels are mutually exclusive. That is, only one IPv4 or IPv6 tunnel can be configured at a time.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + The virtual peer-link solution does not support pure Layer 2 scenarios. The bypass VXLAN tunnel requires reachable Layer 3 routes. Therefore, ensure that there are reachable Layer 3 routes between the source and peer IP addresses.
     + It is recommended that loopback interface addresses be used as the source and destination IP/IPv6 addresses for establishing a bypass VXLAN tunnel. If a Layer 3 interface address is used, the interface address can only be used by the bypass VXLAN tunnel and cannot be used to forward network-side service traffic.
  4. Exit the NVE interface view.
     ```
     quit
     ```
  5. Enter the Eth-Trunk interface view.
     ```
     [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The Eth-Trunk interface cannot be configured with any member interface. Otherwise, it cannot be configured as a virtual peer-link interface.
  6. Configure STP or VBST.
     + If the M-LAG is configured in root bridge mode, disable STP on the interface.
       ```
       [undo stp enable](cmdqueryname=undo+stp+enable)
       ```
     + If the M-LAG is configured in V-STP mode, enable STP on the interface.
       ```
       [stp enable](cmdqueryname=stp+enable)
       ```
     + If the M-LAG is configured in V-VBST mode, enable VBST on the interface.
       ```
       [stp enable](cmdqueryname=stp+enable)
       ```![](../public_sys-resources/note_3.0-en-us.png) 
     + In an M-LAG configured in root bridge mode, because the M-LAG master and backup devices need to be simulated into one root bridge, you need to disable STP on peer-link interfaces to ensure that the directly connected interfaces are not blocked.
     + In an M-LAG configured in V-STP mode, because the M-LAG master and backup devices need to exchange packets through the peer-link to perform STP virtualization calculation, you need to enable STP on peer-link interfaces. The STP configurations on the peer-link interfaces of the two devices must be the same.
     + In an M-LAG configured in V-VBST mode, because the M-LAG master and backup devices need to exchange packets through the peer-link to perform STP virtualization calculation, you need to enable VBST on peer-link interfaces.
  7. Configure the Eth-Trunk interface as the virtual peer-link interface.
     ```
     [peer-link](cmdqueryname=peer-link) peer-linkid virtual-link
     ```
     
     By default, an Eth-Trunk interface does not function as a peer-link interface.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + An interface configured as a peer-link interface is added to all VLANs by default. However, if a VLAN is bound to a BD, the peer-link interface is not added to the VLAN.
     + An interface configured as a peer-link interface cannot be configured with any other service.
     + If network-side VLANIF interfaces are configured on M-LAG member devices and establish a DAD link, perform [step 8](#EN-US_TASK_0000001512689654__li16612118309) to remove peer-link interfaces from the VLANs corresponding to the VLANIF interfaces. Otherwise, DAD may fail.
     + In the virtual peer-link solution, the up/down status of the virtual peer-link interface is the same as the up/down status of the bypass VXLAN tunnel.
     + If the **peer** *ip-address* parameter has been configured for DAD, you are advised to configure a virtual peer-link interface when the bypass VXLAN tunnel is up. If you configure a virtual peer-link interface when the bypass VXLAN tunnel is down, the virtual peer-link interface is also down. In this case, if the DAD heartbeat status is normal, interfaces on one M-LAG member device will enter the error-down state.
     + The **peer-link** *peer-linkid* **virtual-link** and **mode lacp-static** commands are mutually exclusive on an interface.
     + The **peer-link** *peer-linkid* **virtual-link** and **mode lacp-dynamic** commands are mutually exclusive on an interface.
     + The **peer-link** *peer-linkid* **virtual-link** and **trunkport** commands are mutually exclusive on an interface.
     + The **peer-link** *peer-linkid* **virtual-link** and **shutdown** commands are mutually exclusive on an interface.
     + The **peer-link** *peer-linkid* **virtual-link** command and the [**mld snooping enable**](cmdqueryname=mld+snooping+enable) command in the system view are mutually exclusive.
     + Each M-LAG member device has independent services, and MAC addresses learned in VLANs of these services do not need to be synchronized. In addition, M-LAG member devices independently maintain MAC addresses used to establish a VXLAN tunnel between them and do not synchronize the MAC addresses to each other. MAC address synchronization in this scenario causes MAC address flapping, resulting in loss of traffic forwarded through the virtual peer-link interface. To prevent this problem, use either of the following methods:
       - Run the [**port vlan exclude**](cmdqueryname=port+vlan+exclude) command on the Eth-Trunk interface that functions as the virtual peer-link interface to remove the Eth-Trunk interface from a VLAN. M-LAG synchronization then is not performed for the VLAN.
       - Run the [**reserved for vxlan bypass**](cmdqueryname=reserved+for+vxlan+bypass) command on the VLANIF interface corresponding to the virtual peer-link interface to configure the IP address of the VLANIF interface to be used only by the bypass VXLAN tunnel. M-LAG synchronization then is not performed for the VLAN.
  8. (Optional) Configure the VLANs from which packets are not allowed to pass through the peer-link interface.
     ```
     [port vlan exclude](cmdqueryname=port+vlan+exclude) { { vlan-id1 [ to vlan-id2 ] } &<1-10> }
     ```
     
     By default, packets from all VLANs are allowed to pass through a peer-link interface.
  9. Exit the Eth-Trunk interface view.
     ```
     [quit](cmdqueryname=quit)
     ```
  10. Enter the NVE interface view.
      ```
      interface nve nve-number
      ```
  11. Configure reserved VNIs. The 4096 VNIs starting from the VNI specified by the *vni-id* parameter are reserved for the virtual peer-link solution.
      ```
      vni vni-id reserved for m-lag
      ```
      
      By default, no reserved VNI is configured for the virtual peer-link solution.
      
      ![](../public_sys-resources/note_3.0-en-us.png) 
      + In the virtual peer-link solution, reserved VNIs must be configured. Otherwise, the M-LAG cannot be set up.
      + The reserved VNIs on the two M-LAG member devices must be the same.
      + In the virtual peer-link solution, VLAN traffic between M-LAG member devices needs to be forwarded through the virtual peer-link. VLAN IDs need to be converted into VNIs so that the VLAN traffic is forwarded through a bypass VXLAN tunnel. In this case, 4096 VNIs need to be reserved. VNIs 1 to 4094 are reserved for mapping from VLAN IDs to VNIs, and VNIs 4095 and 4096 are reserved for the M-LAG mechanism.
  12. Exit the NVE interface view.
      ```
      quit
      ```
  13. (Optional) Configure a VLAN to contain only the peer-link interface.
      1. Create a VLAN and enter the VLAN view. If the VLAN has been created, the VLAN view is displayed.
         ```
         [vlan](cmdqueryname=vlan) vlan-id
         ```
         ![](../public_sys-resources/note_3.0-en-us.png) 
         
         Based on service requirements, you can also run the **vlan range** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command in the system view to create a temporary VLAN range and enter the VLAN range view.
      2. Configure the VLAN to contain only the peer-link interface so that packets from the VLAN can be forwarded only on the peer-link interface.
         ```
         [m-lag peer-link reserved](cmdqueryname=m-lag+peer-link+reserved)
         ```
         
         By default, a VLAN can contain a peer-link interface and other Layer 2 interfaces.
         
         ![](../public_sys-resources/note_3.0-en-us.png) 
         
         In a multicast over VXLAN scenario, as long as the receiver and multicast source are dual-homed to the two member devices in the same M-LAG, the VLANIF interface corresponding to the VLAN configured with the [**m-lag peer-link reserved**](cmdqueryname=m-lag+peer-link+reserved) command cannot be used to establish a bypass VXLAN tunnel, regardless of whether the receiver and multicast source are in the same VLAN. Otherwise, the receiver will receive redundant multicast traffic.
  14. Commit the configuration.
      ```
      commit
      ```
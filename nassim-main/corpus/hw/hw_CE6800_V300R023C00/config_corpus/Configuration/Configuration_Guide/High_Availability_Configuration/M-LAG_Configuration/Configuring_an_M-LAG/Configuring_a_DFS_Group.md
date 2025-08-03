Configuring a DFS Group
=======================

Configuring a DFS Group

#### Context

The two M-LAG member devices in a DFS group exchange negotiation packets to determine their master and backup roles based on their DFS group priorities and system MAC addresses, where the device with a higher DFS group priority functions as the M-LAG master device. If the two devices have the same DFS group priority, the device with a smaller system MAC address functions as the M-LAG master device. M-LAG member devices use the DFS group protocol to synchronize information such as the interface status and entries. To improve network security and prevent hackers from performing network attacks aimed at disclosing network information, you need to configure authentication for DFS group synchronization packets.

For the CE6820H, CE6820H-K, and CE6820S: VXLAN-related configurations are not supported.

For the CE6885-LL (low latency mode): VXLAN and IPv6-related configurations are not supported.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a DFS group and enter its view.
   
   
   ```
   [dfs-group](cmdqueryname=dfs-group) dfs-group-id
   ```
3. (Optional) Configure the DFS group priority.
   
   
   ```
   [priority](cmdqueryname=priority) priorityvalue
   ```
   
   
   
   By default, the DFS group priority is 100.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the two M-LAG member devices have the same DFS group priority and system MAC address, they both function as M-LAG master devices. In this case, you are advised to configure different DFS group priorities for M-LAG member devices.
4. Configure the authentication mode and password for DFS group synchronization packets.
   
   
   ```
   [authentication-mode](cmdqueryname=authentication-mode) hmac-sha256 password pwdtext
   ```
   
   
   
   By default, the authentication mode of DFS group synchronization packets is not configured.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The authentication mode and password must be configured, and the devices in an M-LAG must use the same authentication password.
   
   After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used in the **[**authentication-mode**](cmdqueryname=authentication-mode)** command.
5. (Optional) Configure the delay in switching the M-LAG LACP system ID.
   
   
   ```
   [set lacp system-id switch-delay](cmdqueryname=set+lacp+system-id+switch-delay) { switch-delay-time | immediately }
   ```
   
   
   
   If **immediately** is specified, the M-LAG LACP system ID is switched immediately. If *switch-delay-time* is set to 0, the M-LAG LACP system ID is not switched.
   
   By default, the M-LAG LACP system ID is not switched.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * When DFS group pairing is successful, the master device synchronizes its M-LAG LACP system ID to the backup device, and the M-LAG member interface on the backup device uses the synchronized M-LAG LACP system ID to perform LACP negotiation. However, if DFS group pairing fails or the M-LAG splits and the device does not join the M-LAG again within the time specified by *switch-delay-time*, the M-LAG backup device changes the synchronized M-LAG LACP system ID to its own M-LAG LACP system ID. If the device joins the M-LAG again within the time specified by *switch-delay-time*, the M-LAG LACP system ID is not switched.
   * After a master/backup switchover of M-LAG devices, the M-LAG LACP system ID is not switched.
6. (Optional) Configure an IP address bound to the TCP channel for transmitting M-LAG protocol synchronization packets. Run either of the following commands. The commands cannot be configured together.
   
   
   * Configure an IPv4 address and a TCP port number bound to the TCP channel for transmitting M-LAG protocol synchronization packets.
     ```
     peer-link source ip ipv4-address1 [ vpn-instance vpnname ] peer ipv4-address2 tcp-port portnum
     ```
   * Configure an IPv6 address and a TCP port number bound to the TCP channel for transmitting M-LAG protocol synchronization packets.
     ```
     peer-link source ipv6 ipv6-address1 [ vpn-instance vpnname ] peer ipv6-address2 tcp-port portnum
     ```
   
   By default, no TCP channel is configured for transmitting M-LAG protocol synchronization packets. To improve M-LAG synchronization reliability when a device is dual-homed to an Ethernet, VXLAN, or IP network through an M-LAG, you need to bind the IP addresses and TCP port numbers of the Layer 3 interfaces on the two M-LAG devices to a TCP channel. This TCP channel is used only for ARP and ND entry synchronization between M-LAG devices.
7. (Optional) Configure the type of packets for electing the M-LAG master and backup member interfaces in an M-LAG in active/standby mode.
   
   
   ```
   [m-lag active-standby election](cmdqueryname=m-lag+active-standby+election) { arp | nd | igmp | dhcp | mld }
   ```
   
   By default, the type of packets for electing the M-LAG master and backup member interfaces in an M-LAG in active/standby mode is not configured.
   
   For the CE6885-LL (low latency mode): The **nd** and **mld** packet types cannot be configured.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * If the M-LAG works in active/standby mode, this step is mandatory.
   * An M-LAG in active/standby mode elects the M-LAG master and backup member interfaces based on protocol packets received from a server connected to the M-LAG. ARP, ND, IGMP, MLD, and DHCP packets are supported. You can configure the type of packets for electing the M-LAG master and backup member interfaces based on actual requirements. At least one packet type must be configured. To ensure that IGMP/DHCP/MLD packets can be sent to the CPU, you need to enable IGMP snooping in a VLAN or BD so that M-LAG master and backup member interface election can be performed through IGMP packets. Alternatively, you need to enable DHCP globally so that M-LAG master and backup member interface election can be performed through DHCP packets. You can also enable MLD snooping in a VLAN or BD so that M-LAG master and backup member interface election can be performed through MLD packets. In addition, when an M-LAG device functions as a Layer 2 transparent transmission device or Layer 2 gateway, ARP/ND packets are not sent to the CPU, and M-LAG master and backup member interface election cannot be performed through packets for electing the M-LAG master member interface. In this case, you need to enable Layer 2 proxy ARP in a VLAN and enable ARP broadcast suppression or NS multicast suppression in a BD so that ARP/ND packets can be used for M-LAG master and backup member interface election.
   * The two devices in an M-LAG must be configured with the same type of packets for electing the M-LAG master and backup member interfaces.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
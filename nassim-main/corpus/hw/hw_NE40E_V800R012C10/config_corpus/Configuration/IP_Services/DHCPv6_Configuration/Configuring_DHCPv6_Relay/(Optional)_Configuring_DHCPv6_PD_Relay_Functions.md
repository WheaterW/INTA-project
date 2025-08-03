(Optional) Configuring DHCPv6 PD Relay Functions
================================================

A DHCPv6 relay agent can be configured to advertise DHCPv6 PD routes, limit the maximum number of access DHCPv6 clients, and check the physical information of DHCPv6 messages.

#### Context

In DHCPv6 (IA\_PD) scenarios, a DHCPv6 relay agent generates a PD route based on the DHCPv6 PD prefix assigned by the DHCPv6 server to a DHCPv6 client. By default, this PD route applies only to the relay agent and is not advertised. Other devices cannot obtain the routes destined for the CPE and its attached user terminals. As a result, the user terminals cannot access the network. To resolve this issue, perform either of the following operations:

* Configure a summary route with a DHCPv6 PD prefix and use a routing protocol to advertise the route to other devices. This method is recommended because it does not require other devices to learn many routes, so it has little impact on the core network.
* Run the [**dhcpv6 export pd-route**](cmdqueryname=dhcpv6+export+pd-route) command to enable a DHCPv6 relay agent to advertise a generated PD route to other devices using a routing protocol.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 export pd-route**](cmdqueryname=dhcpv6+export+pd-route)
   
   
   
   The DHCPv6 relay agent is enabled to automatically advertise DHCPv6 PD routes.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After a device is enabled to advertise DHCPv6 PD routes, these routes can be advertised only after they are imported to the routing table of a dynamic routing protocol. Configure the device to import external routes based on the running routing protocol. For details, see [Configuring RIP to Import External Routes](dc_vrp_rip_cfg_0026.html), [Configuring OSPF to Import External Routes](dc_vrp_route-policy_cfg_0039.html), and [Configuring IS-IS to Import External Routes](dc_vrp_route-policy_cfg_0040.html).
3. Run [**dhcpv6 relay pd-route auto-save**](cmdqueryname=dhcpv6+relay+pd-route+auto-save) *file-name*
   
   
   
   The DHCPv6 relay agent is enabled to automatically save PD routes.
   
   
   
   PD routes are lost after a relay agent restarts, preventing users from accessing the network. You can run this command to enable the relay agent to automatically save PD routes to a file, from which the relay agent can restore the PD routes after restarting.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An encrypted file integrity check code is added to the backup file to prevent tampering. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the PD routes from the backup file. If the verification is successful, the data is restored; otherwise, it is discarded and a log is recorded.
   
   * If you manually modify the content of the backup file, run the [**dhcpv6 relay database authentication-mode no-check**](cmdqueryname=dhcpv6+relay+database+authentication-mode+no-check) command to set the file integrity authentication mode to no-check before the restart.
   * The root keys for decrypting and encrypting the file integrity check code must be the same. Otherwise, the decryption fails. The root key on each device is unique to that device. If you use a backup file generated on another device to restore data, run the [**dhcpv6 relay database authentication-mode no-check**](cmdqueryname=dhcpv6+relay+database+authentication-mode+no-check) command to set the file integrity authentication mode to no-check before the restart.
   * For compatibility with earlier versions, data can be restored based on an earlier version of a file that does not carry the file integrity check code after a restart. To forcibly check whether data is tampered with based on an earlier version of a file, run the [**dhcpv6 relay database authentication-mode force-check**](cmdqueryname=dhcpv6+relay+database+authentication-mode+force-check) command to set the file integrity authentication mode to force-check before a restart.
4. Run [**dhcpv6 relay pd-route auto-save maximum**](cmdqueryname=dhcpv6+relay+pd-route+auto-save+maximum) *number*
   
   
   
   The maximum number of entries in the PD route user table to be written into a file is configured.
5. Run [**dhcpv6 relay pd-route auto-save write-delay**](cmdqueryname=dhcpv6+relay+pd-route+auto-save+write-delay) *delaytime*
   
   
   
   A delay for writing the PD route user table into a file during automatic file saving is configured.
6. Run [**set dhcpv6 relay pd-route write immediately**](cmdqueryname=set+dhcpv6+relay+pd-route+write+immediately)
   
   
   
   The function of immediately writing the PD route user table into a file is configured.
7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of a DHCPv6 relay interface is displayed.
8. Run [**dhcpv6 relay access-limit**](cmdqueryname=dhcpv6+relay+access-limit)
   
   
   
   The maximum number of DHCPv6 clients that are allowed to access the DHCPv6 relay interface is configured.
   
   After the maximum number is reached, new DHCPv6 clients are not allowed to access the DHCPv6 relay interface.
   
   
   
   * The [**dhcpv6 relay access-limit**](cmdqueryname=dhcpv6+relay+access-limit) *limit-number* command configures the maximum number of access DHCPv6 clients on a DHCPv6 relay interface.
   * The [**dhcpv6 relay access-limit**](cmdqueryname=dhcpv6+relay+access-limit) *limit-number* **vlan** *vlan-id* [ *end-vlan-id* ] command configures the maximum number of access DHCPv6 clients in a specified VLAN on a DHCPv6 relay interface. If both *vlanid* and *end-vlan-id* are configured to specify a VLAN range, the maximum number of access DHCPv6 clients applies to all the VLANs in this range. Each relay interface supports 16 VLAN ranges. For example, if the [**dhcpv6 relay access-limit 1 vlan 1 100**](cmdqueryname=dhcpv6+relay+access-limit+1+vlan+1+100) command is run on GE 0/1/1.1, one DHCPv6 client is allowed to go online through VLANs in the range 1â100.
     
     If both *vlanid* and *end-vlan-id* are configured to specify a VLAN range, the maximum number of access DHCPv6 clients applies to all the VLANs in this range. Each relay interface supports 16 VLAN ranges. For example, if the [**dhcpv6 relay access-limit 1 vlan 1 100**](cmdqueryname=dhcpv6+relay+access-limit+1+vlan+1+100) command is run on GE 0/1/1.1, one DHCPv6 client is allowed to go online through VLANs in the range 1â100.
   * The [**dhcpv6 relay access-limit**](cmdqueryname=dhcpv6+relay+access-limit) *limit-number* **pevlan** *pevlan-id* { **cevlan** *cevlan-id* [ *end-cevlan-id* ] | **any** } command configures the maximum number of DHCPv6 clients that send double-tagged packets to go online through a DHCPv6 relay interface.
     
     Each relay interface supports 16 VLAN ranges. If you configure **any** for **cevlan**, the maximum number of DHCPv6 clients whose packets carry the outer VLAN ID specified by *pevlan-id* and any VLAN ID not in the CE-VLAN range is limited. This configuration is counted in the 16 VLAN ranges allowed. For example, if both the [**dhcpv6 relay access-limit 1 pevlan 2 cevlan 1 100**](cmdqueryname=dhcpv6+relay+access-limit+1+pevlan+2+cevlan+1+100) and [**dhcpv6 relay access-limit 2 pevlan 2 cevlan any**](cmdqueryname=dhcpv6+relay+access-limit+2+pevlan+2+cevlan+any) commands are run on GE 0/1/1.1, one DHCPv6 client whose packets carry PE-VLAN 2 and any CE-VLAN ID in the range 1â100 is allowed to go online, and two DHCPv6 clients whose packets carry PE-VLAN 2 and any CE-VLAN ID in the range 101â4094 are allowed to go online
   * The [**dhcpv6 relay access-limit**](cmdqueryname=dhcpv6+relay+access-limit) *limit-number* **vlan** **any** command configures the maximum number of DHCPv6 clients that can go online through single or double VLANs that do not have such a limit configured. This configuration is not counted in the 16 VLAN ranges allowed.
     
     To limit the maximum number of access DHCPv6 clients on a DHCPv6 relay interface in a specified VLAN, run this command. For example, if DHCPv6 clients send double-tagged packets to go online, each pair of VLAN tags identifies a VLAN. Run the [**dhcpv6 relay access-limit 1 vlan any**](cmdqueryname=dhcpv6+relay+access-limit+1+vlan+any) command to configure a DHCPv6 relay interface to allow only one client that sends double-tagged VLAN packets to go online. This configuration protects the device against packets with changing MAC addresses and DUIDs.
9. Run [**dhcpv6 relay strict-check interface-info**](cmdqueryname=dhcpv6+relay+strict-check+interface-info)
   
   
   
   The DHCPv6 relay interface is enabled to check the physical information of DHCPv6 messages.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
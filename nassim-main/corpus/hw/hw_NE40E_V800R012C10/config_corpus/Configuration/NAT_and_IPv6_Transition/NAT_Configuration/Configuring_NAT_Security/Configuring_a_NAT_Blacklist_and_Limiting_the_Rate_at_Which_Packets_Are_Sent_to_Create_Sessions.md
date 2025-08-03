Configuring a NAT Blacklist and Limiting the Rate at Which Packets Are Sent to Create Sessions
==============================================================================================

The NAT blacklist and session creation rate limit are used to prevent users from occupying a large number of CPU resources through traffic attacks, which affects the forwarding of common traffic.

#### Context

The NAT blacklist function defends a device against attacks initiated by sending network-side first packets with a specified set of a public IP address, a port number, and a protocol ID or to all IP addresses. If no internal server is configured or if public network traffic does not match sessions on a NAT device, the NAT device considers traffic transmitting at a rate reaching a specified threshold as attack traffic. The NAT device then adds the IP address and UDP or TCP destination port number of the attack traffic to a NAT blacklist. Once network-side attack traffic matches the blacklist, the NAT device drops the traffic and collects statistics about the traffic.

The NAT blacklist-based detection is performed in either of the following modes:

* Address-level detection: An address-level rate threshold is set for a NAT device to detect attacks only on IP addresses.
* Port-level detection: A port-level rate threshold is set for a NAT device to detect attacks using packets with a specified IP address, a specified port number, and a specified protocol ID.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin-VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**undo nat flow-defend reverse-blacklist disable**](cmdqueryname=undo+nat+flow-defend+reverse-blacklist+disable)
   
   
   
   The NAT blacklist function is enabled.
3. Run [**nat flow-defend**](cmdqueryname=nat+flow-defend) { **forward** | **fragment** | **reverse** } **rate** *rate-number* **slot** *slot-id* 
   
   
   
   The limit on the rate at which packets are sent to create sessions on a service board is set.
4. (Optional) Run [**nat flow-defend reverse-blacklist detect-threshold ip-port-level high-threshold**](cmdqueryname=nat+flow-defend+reverse-blacklist+detect-threshold+ip-port-level+high-threshold) *ip-port-level-high-threshold-value*
   
   
   
   A port-level rate threshold for the NAT blacklist is configured for a device. Threshold-crossing traffic is blacklisted.
   
   
   
   If the NAT blacklist function is enabled, after this command is run, the device detects the attack traffic for the IP address, port number, and protocol number. You can set the port-level rate threshold for the NAT blacklist to adjust the attack traffic detection rate.
5. (Optional) Run [**nat flow-defend reverse-blacklist detect-threshold ip-level high-threshold**](cmdqueryname=nat+flow-defend+reverse-blacklist+detect-threshold+ip-level+high-threshold) *ip-level-high-threshold-value*
   
   
   
   An address-level rate threshold for the NAT blacklist is configured for a device. Threshold-crossing traffic is blacklisted.
   
   
   
   If the NAT blacklist function is enabled, after this command is run, the device detects the attack traffic for the IP address. You can set the address-level rate threshold for the NAT blacklist to adjust the attack traffic detection rate.
   
   The port- and address-level rate thresholds can be configured together for the NAT blacklist. The two commands are independent of each other.
6. Run [**nat flow-defend reverse-blacklist auto-lock enable**](cmdqueryname=nat+flow-defend+reverse-blacklist+auto-lock+enable)
   
   
   
   Automatic locking of the NAT blacklist is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support this configuration.
   
   If NAT attack traffic reaches a specified detection threshold, entries are generated in a NAT blacklist. The NAT device automatically isolates IP addresses listed in the blacklist. Users with such IP addresses are logged out, and the IP addresses are not assigned to new users who want to get online.
7. Run [**nat flow-defend reverse-blacklist manual-lock lock-ip-address**](cmdqueryname=nat+flow-defend+reverse-blacklist+manual-lock+lock-ip-address) *lockip-address* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   An IP address to be locked and a VPN instance are configured for NAT attack defense.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support this configuration.
   
   
   After this command is run, the specified IP address is isolated, and a blackhole route is generated for the IP address. All traffic sent to the IP address is discarded on the involved interface board. In addition, all users using this IP address go offline, and new users cannot use this IP address to go online. To delete the manually locked IP address and VPN instance information in the NAT blacklist, run the [**reset nat flow-defend reverse-blacklist manual-lock lock-ip-address**](cmdqueryname=reset+nat+flow-defend+reverse-blacklist+manual-lock+lock-ip-address) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The automatic lock function of NAT blacklists can be configured only on [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595).
   * IP address locking and VPN instance information for NAT attack defense can be configured only on [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595).
   * The automatic lock function of NAT blacklists and the manual IP address lock function of NAT attack defense cannot take effect at the same time.
   * For on-board NAT, only alarms are generated after the NAT blacklist function is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configurations, you can run the following commands to check the configurations.

* Run the [**display nat flow-defend reverse-blacklist**](cmdqueryname=display+nat+flow-defend+reverse-blacklist) command to check information about blacklist entries of the reverse first packets on the CPU.
* Run the [**display nat flow-defend reverse-blacklist lock-ip-address**](cmdqueryname=display+nat+flow-defend+reverse-blacklist+lock-ip-address) command to check information about manually or automatically locked IP addresses in NAT attack defense.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
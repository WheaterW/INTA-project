Configuring IPsec NAT Traversal
===============================

When an NAT device exists between IPsec peers, the NAT traversal function must be enabled on both ends.

#### Context

AH is mainly used to ensure the message integrity, including the IP packet headers. Because the IP packet headers are modified by NAT, the IP packet header verification by AH fails. Therefore, an IPsec tunnel protected by AH cannot traverse the NAT gateway. Packets encrypted by ESP do not encounter this problem because the integrity verification by ESP does not include IP packet headers (outer IP packet header in tunnel mode).

When an IPsec packet traverses the NAT gateway, a standard UDP packet header is added between the original IP header and the ESP header. When the ESP packet traverses the NAT gateway, the NAT translates the address and port number in the outer IP header and added UDP header. When the translated packet reaches the peer end of the IPsec tunnel, it is processed as a common packet. However, in a response packet, a UDP header also needs to be added between the IP header and ESP header. [Figure 1](#EN-US_TASK_0172372442__fig_dc_vrp_ipsec_cfg_all_002601) shows a typical application of the IPsec NAT traversal. **Figure 1** Typical application of the IPsec NAT traversal  
![](images/fig_dc_vrp_ipsec_cfg_all_002601.png)

When the NAT gateway is configured to allocate indexes dynamically, the same private network IP address can be mapped by NAT to different addresses and port numbers after the IPsec SA is disconnected and reconnected. When the NAT gateway is configured to allocate indexes statically, a private network IP address is mapped by NAT to only one IP address and port number. Configuring the NAT gateway to allocate indexes statically is recommended.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run the [**ike peer**](cmdqueryname=ike+peer) *peer-name* command to create an IKE peer and enter the IKE peer view.
3. Run the [**nat traversal**](cmdqueryname=nat+traversal) command to enable NAT traversal.
4. Run the [**remote-address**](cmdqueryname=remote-address+authentication-address+vpn-instance) [ **authentication-address** | **vpn-instance** *vpn-instance-name* ] *remote-low-address* [ *remote-high-address* ] command to configure the peer IP address or address segment.
   
   
   1. Configuration of device A:
      
      * If the HQ network does not need to initiate access, you can configure the IPsec policy template for device A. The IKE peer defined in the IPsec policy template may not specify the peer IP address (that is, the [**remote-address**](cmdqueryname=remote-address) command used to configure the translated IP address for device A and device B, is not configured).
      * If the HQ network needs to initiate access, you must configure the IPsec policy in IKE mode for device A. The IKE peer defined in the IPsec policy must specify the peer IP address that is translated (running the [**remote-address**](cmdqueryname=remote-address) 172.16.0.1 command).
        
        If the local ID of device B is set to the IP address, you must run the [**remote-address**](cmdqueryname=remote-address+authentication-address) **authentication-address** command to set the outbound interface address or address segment (IP address before NAT) of gateway B as the verification address ([**remote-address**](cmdqueryname=remote-address+authentication-address) **authentication-address** 10.0.0.1) for device A.
   2. Configuration of device B:
      
      Configure the IPsec policy in IKE mode for device B. Specify the peer IP address ([**remote-address**](cmdqueryname=remote-address) 192.168.0.1) on the IKE peer defined in the IPsec policy.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Run the [**ike sa nat-keepalive-timer interval**](cmdqueryname=ike+sa+nat-keepalive-timer+interval) *seconds* command to set the interval at which NAT update packets are sent by IKE.
   
   
   
   A NAT session has a certain survival period on the NAT gateway. After a tunnel is established, if no packet traverses the gateway for a long period of time, the NAT session is deleted. As a result, data cannot be transmitted over the tunnel. A NAT-keepalive message can be sent to the peer party before the NAT session expires to maintain the NAT session and address the preceding issue.
7. Run the [**commit**](cmdqueryname=commit) command to make the configuration take effect.

#### Follow-up Procedure

Run the [**display ike peer**](cmdqueryname=display+ike+peer) command to check the **nat traversal** field in the output and determine whether NAT traversal is enabled.
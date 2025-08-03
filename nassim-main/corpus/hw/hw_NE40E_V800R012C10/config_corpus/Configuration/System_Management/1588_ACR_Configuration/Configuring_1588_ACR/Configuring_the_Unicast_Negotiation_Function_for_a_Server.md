Configuring the Unicast Negotiation Function for a Server
=========================================================

The unicast negotiation function and parameters for a connection between a client and a clock server are configured on the Router functioning as a 1588 ACR clock server.

#### Context

ACR, which is an adaptive clock recovery technology, allows a 1588 ACR client to exchange 1588v2 packets with a clock server on a link where a 1588v2-incapable device resides. After receiving 1588v2 packets, the client uses clock information carried in the packets to restore clock information.

1588 ACR client and 1588v2 (which implements hop-by-hop clock synchronization) are mutually exclusive. If 1588 ACR is enabled on a 1588v2-capable device, the 1588v2 configurations on the device no longer take effect. The 1588 ACR server and 1588v2 can be both configured on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable)
   
   
   
   1588 ACR is enabled.
3. Run [**ptp-adaptive device-type**](cmdqueryname=ptp-adaptive+device-type) **server**
   
   
   
   The 1588 ACR clock working mode is set to server.
4. (Optional) Run [**ptp-adaptive frequency profile**](cmdqueryname=ptp-adaptive+frequency+profile)
   
   
   
   The 1588 ACR-enabled device to totally comply with ITU-T G.8265.1 is configured.
   
   
   
   After the [**ptp-adaptive frequency profile**](cmdqueryname=ptp-adaptive+frequency+profile) command is run, the default domain value changes to 4. The domain value range changes to 4-23.
5. (Optional) Run [**ptp-adaptive domain**](cmdqueryname=ptp-adaptive+domain) *domain-value*
   
   
   
   A 1588 ACR domain is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The client and clock server, which exchange 1588 ACR packets for clock synchronization, must be in one 1588 ACR clock domain.
6. Run [**ptp-adaptive local-ip**](cmdqueryname=ptp-adaptive+local-ip) *ip-address*
   
   
   
   An IP address is assigned to the clock server.
   
   The clock server's and client's IP addresses uniquely identify a 1588 ACR connection, which is set up by exchanging Layer 3 unicast packets between a client and a clock server during negotiation. Configuring a loopback address as the server's IP address is recommended, helping the clock server direct packets to the client.
7. (Optional) Run [**ptp-adaptive vpn-instance**](cmdqueryname=ptp-adaptive+vpn-instance) *vpn-name*
   
   
   
   The VPN instance name carried in 1588v2 packets is specified, which identifies the VPN instance bound to the client's loopback interface.
8. Run [**ptp-adaptive**](cmdqueryname=ptp-adaptive) { **acr** [ **one-way** | **two-way** ] | **atr** } **unicast-negotiate** **enable**
   
   
   
   The 1588 ACR unicast negotiation on the device is configured.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
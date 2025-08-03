Configuring the Unicast Negotiation Function for a Client
=========================================================

The unicast negotiation function and parameters for a connection between a client and a clock server are configured on the Router functioning as a 1588 ACR client.

#### Context

ACR, which is an adaptive clock recovery technology, allows a 1588 ACR client to exchange 1588v2 packets with a clock server on a link where a 1588v2-incapable device resides. After receiving 1588v2 packets, the client uses clock information carried in the packets to restore clock information.

The 1588 ACR features supported by the NE40E are as follows:

* 1588 ACR clock synchronization in single-server scenarios
  
  In a 1588 ACR domain, a client establishes a client/server relationship only with the remote clock server. The client initiates unicast negotiation requests and obtains 1588v2 packets for clock restoration. If a clock server becomes faulty, the client does not automatically initiate a connection request to another clock server.
* 1588 ACR clock synchronization in dual-server scenarios
  
  In a 1588 ACR domain, a client establishes a client/server relationship with two remote clock servers. The client initiates unicast negotiation requests and obtains 1588v2 packets for clock restoration. If the master clock server becomes faulty, the client automatically initiates a connection request to the slave clock server.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) command to enable 1588 ACR on the device.
3. Run the [**ptp-adaptive device-type**](cmdqueryname=ptp-adaptive+device-type) **client** command to set the 1588 ACR clock working mode of the Router to client.
4. (Optional) Run the [**ptp-adaptive frequency profile**](cmdqueryname=ptp-adaptive+frequency+profile) command to configure the 1588 ACR-enabled device to totally comply with ITU-T G.8265.1.
   
   
   
   After the **ptp-adaptive frequency profile** command is run, the default domain value changes to 4. The domain value range changes to 4â23.
5. (Optional) Run the [**ptp-adaptive domain**](cmdqueryname=ptp-adaptive+domain) *domain-value* command to configure a 1588 ACR domain.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The client and clock server, which exchange 1588v2 packets for clock synchronization, must be in the same 1588 ACR clock domain.
6. Run the [**ptp-adaptive local-ip**](cmdqueryname=ptp-adaptive+local-ip) *ip-address* command to configure a local IP address for the 1588v2 device to initiate Layer 3 unicast negotiation.
   
   
   
   The clock server's and client's IP addresses uniquely identify a 1588 ACR connection, which is set up by exchanging Layer 3 unicast packets between a client and a clock server during negotiation. Configuring a loopback address as the client's IP address is recommended, not the IP address of the management network port on the device, helping the clock server direct packets to the client.
7. (Optional) Run the [**ptp-adaptive vpn-instance**](cmdqueryname=ptp-adaptive+vpn-instance) *vpn-name* command to specify the VPN instance name carried in 1588v2 packets, which identifies the VPN instance bound to the client's loopback interface.
8. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) { **remote-server1-ip** | **remote-server2-ip** } *ip-address* command to configure a remote clock server list for unicast negotiation.
   
   
   
   If multiple clock servers exist on a network, the Router, functioning as a client, traces its clock server based on the clock server's IP address.
   
   Running this command twice specifies master and slave clock servers.
   
   If two clock servers are configured, a client initiates connection requests to both servers. If a connection to a server fails to be established or is disconnected, the client automatically initiates a connection to the other client. The process repeats until the client is connected to a server.
9. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) { **acr** [ **one-way** | **two-way** ] | **atr** } **unicast-negotiate enable** command to enable 1588 ACR unicast negotiation on the Router and configure the frequency recovery mode.
10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
Configuring Unicast Negotiation on a 1588 ATR Client
====================================================

The unicast negotiation function and parameters for a connection between a client and a clock server are configured on the HUAWEI NE40E-M2 series functioning as a 1588 ATR client.

#### Context

ATR, which is an adaptive clock recovery technology, allows a 1588 ATR client to exchange 1588v2 packets with a clock server on a link where a 1588v2-incapable device resides. After receiving 1588v2 packets, the client uses clock information carried in the packets to restore clock information.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable 1588v2 on the device.
3. Run the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) command to enable 1588 ATR on the device.
4. Run the [**clock**](cmdqueryname=clock) **source** **ptp** **synchronization enable** command to specify a PTP clock to participate in clock source selection.
5. Run the [**ptp-adaptive device-type**](cmdqueryname=ptp-adaptive+device-type) **client** command to set the 1588 ATR clock working mode of the Router to client.
6. Run the [**ptp-adaptive time profile**](cmdqueryname=ptp-adaptive+time+profile) command to configure the 1588 ATR device to totally support ITU-T G.8275.2.
   
   
   
   After the [**ptp-adaptive time profile**](cmdqueryname=ptp-adaptive+time+profile) command is run, the default value of the clock domain changes to 44, and the value range changes to 44â63.
7. (Optional) Run the [**ptp-adaptive domain**](cmdqueryname=ptp-adaptive+domain) *domain-value* command to configure a 1588 ATR domain for the device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The 1588 ATR client and server, which exchange 1588 ATR packets for clock synchronization, must be in the same 1588 ATR clock domain.
8. Run the [**ptp-adaptive local-ip**](cmdqueryname=ptp-adaptive+local-ip) *ip-address* command to configure a local IP address for the 1588 ATR device to initiate Layer 3 unicast negotiation.
   
   
   
   The clock server's and client's IP addresses uniquely identify a 1588 ATR connection, which is set up by exchanging Layer 3 unicast packets between a client and a clock server during negotiation. Configuring a loopback address as the client's IP address is recommended, not the IP address of the management network port on the device, helping the clock server direct packets to the client.
9. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) { **remote-server1-ip** | **remote-server2-ip** } *ip-address* command to configure the list of remote clock servers for unicast negotiation.
   
   
   
   If multiple clock servers exist on a network, the Router, functioning as a client, traces a specific clock server based on the clock server's IP address.
   
   Running this command once specifies a clock server, and running it twice specifies a pair of master and slave clock servers.
   
   If two clock servers are configured, the client sends independent signaling packets to both clock servers. After the negotiation succeeds, the client periodically checks the negotiation result. If the traced server is faulty, the client automatically switches to the other server. If the two servers are normal, the client determines which server to trace by comparing the clock quality levels of the two servers.
10. Run the [**ptp-adaptive atr unicast-negotiate enable**](cmdqueryname=ptp-adaptive+atr+unicast-negotiate+enable) command to enable 1588 ATR unicast negotiation on the Router.
11. Enable 1588 ATR on the outbound interface used to transmit 1588 ATR packets.
    
    
    1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
    2. Run the [**ptp-adaptive atr enable**](cmdqueryname=ptp-adaptive+atr+enable) command to enable 1588 ATR on the interface.
    3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
    4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
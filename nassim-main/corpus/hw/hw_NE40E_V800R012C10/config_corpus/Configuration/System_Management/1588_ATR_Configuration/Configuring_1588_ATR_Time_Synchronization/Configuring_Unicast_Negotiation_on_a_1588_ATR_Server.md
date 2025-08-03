Configuring Unicast Negotiation on a 1588 ATR Server
====================================================

A Router that functions as a 1588 ATR server needs to be enabled with unicast negotiation so that it can use Layer 3 unicast packets to establish clock links with a 1588 ATR client and use PTP packets to implement time synchronization over a third-party network.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) command to enable 1588 ATR on the device.
3. Run the [**ptp-adaptive device-type**](cmdqueryname=ptp-adaptive+device-type) **server** command to configure the Router to function as a 1588 ATR server.
4. Run the [**ptp-adaptive time profile**](cmdqueryname=ptp-adaptive+time+profile) command to configure the 1588 ATR device to support ITU-T G.8275.2.
   
   
   
   After the [**ptp-adaptive time profile**](cmdqueryname=ptp-adaptive+time+profile) command is run, the default value of the clock domain changes to 44, and the value range changes to 44â63.
5. (Optional) Run the [**ptp-adaptive domain**](cmdqueryname=ptp-adaptive+domain) *domain-value* command to configure a 1588 ATR domain for the device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The 1588 ATR client and server, which exchange 1588 ATR packets for time synchronization, must be in the same clock domain.
6. Run the [**ptp-adaptive local-ip**](cmdqueryname=ptp-adaptive+local-ip) *ip-address* command to configure a local IP address for the server to initiate Layer 3 unicast negotiation.
   
   
   
   The clock server's and client's IP addresses uniquely identify a 1588 ATR connection, which is set up by exchanging Layer 3 unicast packets between a client and a clock server during negotiation. Configuring a loopback address as the client's IP address is recommended, helping the clock server direct packets to the client.
7. Run the [**ptp-adaptive atr unicast-negotiate enable**](cmdqueryname=ptp-adaptive+atr+unicast-negotiate+enable) command to enable 1588 ATR unicast negotiation on the Router.
8. Enable 1588 ATR on the outbound interface used to transmit 1588 ATR packets.
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   2. Run the [**ptp-adaptive atr enable**](cmdqueryname=ptp-adaptive+atr+enable) command to enable 1588 ATR on the interface.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
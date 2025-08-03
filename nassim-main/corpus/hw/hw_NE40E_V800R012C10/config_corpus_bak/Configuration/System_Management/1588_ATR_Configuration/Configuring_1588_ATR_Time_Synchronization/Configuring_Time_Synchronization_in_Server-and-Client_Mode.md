Configuring Time Synchronization in Server-and-Client Mode
==========================================================

Configuring_Time_Synchronization_in_Server-and-Client_Mode

#### Context

To achieve time synchronization across the VPN, the device needs to serve as both a client to synchronize time with the time source and a server to provide time services for the router close to the base station. The device must be configured to work in server-and-client mode. That is, the device must function as a T-BC.


#### Procedure

* On the upstream device:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the device.
  3. Run the [**ptp profile g-8275-1 enable**](cmdqueryname=ptp+profile+g-8275-1+enable) command to enable ITU-T G.8275.1 on the device.
  4. Run the [**ptp device-type**](cmdqueryname=ptp+device-type) **t-bc** command to set the device type to T-BC.
  5. Run the [**ptp clock-source atr enable**](cmdqueryname=ptp+clock-source+atr+enable) command to enable 1588 ATR time source synchronization.
  6. Run the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) command to enable 1588 ATR on the device.
  7. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) **time** **profile** command to configure the 1588 ATR device to support ITU-T G.8275.2.
  8. Run the [**ptp-adaptive device-type**](cmdqueryname=ptp-adaptive+device-type) **server-and-client** command to set the 1588 ATR working mode of the device to server-and-client.
  9. Run the [**ptp-adaptive master-only-vport**](cmdqueryname=ptp-adaptive+master-only-vport) *port-id* **port-ip** *ip-address* [ **vpn-instance** *vpn-name* ] command to configure the local IP address and VPN instance name used by the virtual upstream interface of the T-BC to initiate Layer 3 unicast negotiation.
  10. Enable 1588 ATR on the outbound interface used to transmit 1588 ATR packets.
      
      
      1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
      2. Run the [**ptp-adaptive atr enable**](cmdqueryname=ptp-adaptive+atr+enable) command to enable 1588 ATR on the interface.
      3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface. The IP address must be the same as that configured for the master-only-vport.
      4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  11. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  12. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) **atr** **unicast-negotiate enable** command to enable 1588 ATR unicast negotiation on the device.
  13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* On the downstream device:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the device.
  3. Run the [**ptp device-type**](cmdqueryname=ptp+device-type) **bc** command to set the device type to BC.
  4. Run the [**ptp clock-source atr enable**](cmdqueryname=ptp+clock-source+atr+enable) command to enable 1588 ATR time source synchronization.
  5. Run the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) command to enable 1588 ATR on the device.
  6. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) **time** **profile** command to configure the 1588 ATR device to support ITU-T G.8275.2.
  7. Run the [**ptp-adaptive device-type**](cmdqueryname=ptp-adaptive+device-type) **server-and-client** command to set the 1588 ATR working mode of the device to server-and-client.
  8. Run the [**ptp-adaptive vport**](cmdqueryname=ptp-adaptive+vport) *port-id* **port-ip** *ip-address* [ **vpn-instance** *vpn-name* ] command to configure the local IP address and VPN instance name used by the T-BC interface to initiate Layer 3 unicast negotiation.
  9. Run the [**ptp-adaptive vport**](cmdqueryname=ptp-adaptive+vport) *port-id* **remote-port-ip** *remote-ip-address* command to configure a list of remote clock servers for unicast negotiation with the specified virtual interface.
  10. Enable 1588 ATR on the inbound interface used to transmit 1588 ATR packets.
      
      
      1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
      2. Run the [**ptp-adaptive atr enable**](cmdqueryname=ptp-adaptive+atr+enable) command to enable 1588 ATR on the interface.
      3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface. The IP address must be the same as that configured for the vport.
      4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  11. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  12. Run the [**ptp-adaptive**](cmdqueryname=ptp-adaptive) **atr** **unicast-negotiate enable** command to enable 1588 ATR unicast negotiation on the device.
  13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
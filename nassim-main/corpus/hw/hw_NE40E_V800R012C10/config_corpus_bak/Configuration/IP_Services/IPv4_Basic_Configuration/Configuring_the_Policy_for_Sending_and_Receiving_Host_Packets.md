Configuring the Policy for Sending and Receiving Host Packets
=============================================================

You can configure the policy for sending and receiving host packets to control the selection of tunnels and the forwarding mode for transmitting host packets.

#### Usage Scenario

When a device is configured with multiple TE tunnels with various priorities, the device randomly selects a TE tunnel in load balancing mode to send host packets. To configure the device to send host packets over the TE tunnel with the highest priority, run the [**host-packet send service-class te enable**](cmdqueryname=host-packet+send+service-class+te+enable) command.

If a sub-interface on the local device has been configured with a VLAN priority for host packets using the [**8021p**](cmdqueryname=8021p) *8021p-value* command, a sub-interface on the peer device has been configured with the same VLAN priority and a VLAN ID using the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid+8021p+to) *low-pe-vid* **8021p** { *8021p-value1* [ **to** *8021p-value2* ] } &<1-8> command, and the IP addresses of the two sub-interfaces are on the same network segment, the local and peer devices fail to communicate with each other and the BGP peer relationship fails to be established between the local and peer devices. To disable fast reply of host packets based on the service type configured on the interface, run the [**host-packet fast-reply disable**](cmdqueryname=host-packet+fast-reply+disable) command.

A device proactively sends a large number of host packets during interface route switching. To relieve the CPU usage of the host module, run the [**host-packet fast-send enable**](cmdqueryname=host-packet+fast-send+enable) command to enable fast reply of host packets based on the service type configured on the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**host-packet send service-class te enable**](cmdqueryname=host-packet+send+service-class+te+enable)
   
   
   
   The device is configured to send host packets over a TE tunnel with the highest priority.
3. Run [**host-packet fast-reply**](cmdqueryname=host-packet+fast-reply+tcp+udp+rawip+disable) { **tcp** | **udp** | **rawip** } **disable**
   
   
   
   Fast reply of host packets is disabled.
4. Run [**host-packet fast-send**](cmdqueryname=host-packet+fast-send+tcp+udp+rawip+enable) { **tcp** | **udp** | **rawip** } **enable**
   
   
   
   Fast reply of host packets is enabled.
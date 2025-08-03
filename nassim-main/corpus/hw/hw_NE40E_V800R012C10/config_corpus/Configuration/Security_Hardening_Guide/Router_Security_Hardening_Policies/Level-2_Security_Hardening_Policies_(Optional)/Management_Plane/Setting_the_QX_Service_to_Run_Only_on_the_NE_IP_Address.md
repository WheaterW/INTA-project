Setting the QX Service to Run Only on the NE IP Address
=======================================================

Setting the QX Service to Run Only on the NE IP Address

#### Security Policy

QX is an application-layer protocol defined between the host software and a GNE. Using the QX packet format and mechanism, a GNE can forward packets received from the control plane to the management plane. In addition, a set of interfaces and mechanisms are provided for the APP protocol on the NE and GNE so that the APP protocol on the management plane can communicate with the NMS on the control plane.

If the QX service runs on all interfaces, that is, the local address of the listening port for QX packets is any address, security risks exist. Generally, the NMS uses only the NE IP address to connect to an NE. Therefore, you are advised to run the [**qx server all-interface disable**](cmdqueryname=qx+server+all-interface+disable) command to set the QX service to run only on the NE IP address to reduce security risks.


#### Attack Methods

An attacker constructs invalid QX packets with any destination address to launch brute force attacks on the device, consuming system resources and affecting the QX service.


#### Configuration and Maintenance Methods

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   The DCN view is displayed.
3. Run [**qx server all-interface disable**](cmdqueryname=qx+server+all-interface+disable)
   
   The QX service is set to run only on the NE IP address.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Checking the Security Hardening Result

Run the [**display tcp status**](cmdqueryname=display+tcp+status) command to check the IPv4 TCP connection status. In the command output, the value of **local Addr** for port 5432 is the NE IP address of the device.

Run the **[**display udp status**](cmdqueryname=display+udp+status)** command to check the IPv4 UDP connection status. In the command output, the value of **local Addr** for ports 1400 and 1500 is the NE IP address of the device.
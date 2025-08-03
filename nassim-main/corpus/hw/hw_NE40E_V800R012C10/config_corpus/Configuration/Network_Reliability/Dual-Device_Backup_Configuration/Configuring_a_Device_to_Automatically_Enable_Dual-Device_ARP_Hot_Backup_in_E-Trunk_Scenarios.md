Configuring a Device to Automatically Enable Dual-Device ARP Hot Backup in E-Trunk Scenarios
============================================================================================

This section describes how to configure a device to automatically enable dual-device ARP hot backup in E-Trunk scenarios.

#### Usage Scenario

L2GVE+L3GVE is deployed to terminate an L2VPN and access an L3VPN. An L2GVE interface joins an E-Trunk, and the E-Trunk's master/backup status determines the hot backup status of user ARP entries learned by an L3GVE interface. After a master/backup switchover is performed, services converge rapidly.

This feature is supported only on the Admin-VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
   
   
   
   An E-Trunk is configured, and the E-Trunk view is displayed.
3. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
   
   
   
   IP addresses are assigned to the local and peer ends of the E-Trunk.
   
   The peer IP address of the local end is the local IP address of the peer end. For example, an E-Trunk is established between device A and device B. On device A, the peer IP address is 2.2.2.2 and the local IP address is 1.1.1.1. Then, on device B, the peer IP address is 1.1.1.1 and the local IP address is 2.2.2.2.
4. Run [**backup tunnel port**](cmdqueryname=backup+tunnel+port) *port-value*
   
   
   
   A TCP port number is configured for a dual-device ARP hot backup channel.
   
   To prevent a configuration failure, ensure that the specified TCP port number is not used. After the command is run, the local and peer ends of an E-Trunk establish a TCP connection to form a hot backup channel, implementing dual-device ARP hot backup.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
(Optional) Configuring VPN over NAT Inter-chassis Hot Backup
============================================================

This section describes how to configure VPN over NAT inter-chassis hot backup to resolve NAT issues on a VPN.

#### Context

In VPN over NAT inter-chassis hot backup scenarios, a private IP address plus a private network VPN instance can be translated to a public IP address plus a private VPN instance, allowing private network users to access a public network over a VPN.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure VPN over NAT inter-chassis hot backup according to on-site requirements.
   
   
   * Perform the following operations to allow translation between private and public VPN instances:
     
     1. Run the [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name* command to enter the service-instance group view.
     2. Run the [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name* command to bind an RBS group to the service-instance group.
     3. Run the [**commit**](cmdqueryname=commit) command to commit the configurations.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**remote-backup-service**](cmdqueryname=remote-backup-service) command is applicable to translation between private VPN instances and public VPN instances and supports both centralized and distributed NAT inter-chassis hot backup scenarios. This method is recommended.
   * Perform the following operations to allow one-to-one translation between a private VPN instance and a public VPN instance. This is applicable only to translation of a single private VPN instance to a public VPN instance and supports only centralized NAT inter-chassis hot backup.
     
     1. Run the [**nat instance**](cmdqueryname=nat+instance) [ **id** *id* ] command to enter the NAT instance view.
     2. Run the [**nat allow-access**](cmdqueryname=nat+allow-access) { **inside vpn-instance** *inside-vpn-instance-name* | **global vpn-instance** *global-vpn-instance-name* } \* command to bind a user-side or network-side VPN instance to the NAT instance.
     3. Run the [**commit**](cmdqueryname=commit) command to commit the configurations.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**nat allow-access**](cmdqueryname=nat+allow-access) command is applicable only to translation of a single private VPN instance to a public VPN instance and supports only centralized NAT inter-chassis hot backup.
Configuring a DAD Link
======================

Configuring a DAD Link

#### Prerequisites

The IP addresses of the Layer 3 interfaces between which a DAD link is set up have been configured on the M-LAG master and backup devices, and the two devices can communicate with each other. The M-LAG DAD link can be set up between Ethernet management interfaces or service interfaces, or be an independent direct link. If the M-LAG is connected to a VPN network, you need to create a VPN instance on M-LAG member devices.


#### Context

The DAD link is used to transmit DAD packets, which detect whether two paired devices in an M-LAG both act as M-LAG master devices, periodically between the two paired devices. If the peer-link fails, the two paired M-LAG member devices do not send protocol packets and synchronization packets to each other; instead, they both function as M-LAG master devices, leading to traffic forwarding exceptions. In this case, some interfaces on one M-LAG device enter the error-down state to prevent this problem. DAD packets are UDP packets forwarded at Layer 3, sent by the M-LAG master and backup devices to each other every 1 second, with both devices expecting to receive response packets within 45 seconds by default. If one end does not receive the DAD packets after a timeout period, the DAD status of the device changes from **OK** to **LOST**.

For the CE6885-LL (low latency mode): IPv6-related configurations are not supported.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a DFS group and enter its view.
   
   
   ```
   [dfs-group](cmdqueryname=dfs-group) dfs-group-id
   ```
3. Bind an IP address to the DFS group. Run either of the following commands. The commands cannot be configured together.
   
   
   * Bind an IPv4 address and a VPN instance to the DFS group.
     
     ```
     [dual-active detection source ip](cmdqueryname=dual-active+detection+source+ip) ipv4-address1 [ [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name ] [ peer ipv4-address2 [ udp-port portnum ] ] [ timeout seconds ]
     ```
   * Bind an IPv6 address and a VPN instance to the DFS group.
     ```
     [dual-active detection source ipv6](cmdqueryname=dual-active+detection+source+ipv6) ipv6-address1 [ [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name ] [ peer ipv6-address2 [ udp-port portnum ] ] [ timeout seconds ]
     ```
   
   By default, no IP address is bound to a DFS group.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * A link cannot function as both the DAD link and peer-link. Otherwise, if the link is down, DAD packets cannot be forwarded over this link, resulting in a DAD failure. As a result, interfaces on one M-LAG member device will not enter the error-down state, leading to abnormal packet forwarding.
   * If the M-LAG DAD link is not set up between Ethernet management interfaces, you must run the **m-lag unpaired-port reserved** command on the interfaces at both ends of the DAD link. If this command is not run, two master devices may exist when the peer-link fails, causing abnormal traffic forwarding.
   * When binding an IP address to the DFS group, you are advised to configure the **peer** *ip-address* parameter. Otherwise, enhanced DAD for double-fault failures does not take effect.
   * The UDP port number of the local device must be the same as that of the peer device. To prevent a UDP port number conflict, you are advised to manually configure the **udp-port** *portnum* parameter.
   * If the peer-link is configured before the DAD link is configured, configure the DAD link when the peer-link interfaces are up to prevent interfaces on one M-LAG member device from entering the error-down state incorrectly.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
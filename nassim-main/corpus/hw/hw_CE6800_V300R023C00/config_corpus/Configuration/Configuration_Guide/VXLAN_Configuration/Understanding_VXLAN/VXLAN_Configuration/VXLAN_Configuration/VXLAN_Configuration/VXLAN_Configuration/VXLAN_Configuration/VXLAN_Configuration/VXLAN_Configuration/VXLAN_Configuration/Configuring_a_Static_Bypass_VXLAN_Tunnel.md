Configuring a Static Bypass VXLAN Tunnel
========================================

Configuring a Static Bypass VXLAN Tunnel

#### Prerequisites

You have completed the following tasks:

* Configure M-LAG active-active gateways.
* Configure VXLAN VNIs for the BDs corresponding to the active-active gateways' VBDIF interfaces.

#### Context

In a physical peer-link scenario where a device is dual-homed to a VXLAN network through an M-LAG and an access-side link fails, service traffic needs to be transmitted through the bypass VXLAN tunnel between M-LAG member devices. In this scenario, a static bypass VXLAN tunnel must be configured between M-LAG member devices.

In a virtual peer-link scenario, a static bypass VXLAN tunnel needs to be deployed between M-LAG member devices to replace the peer-link physical connection.

In a physical peer-link scenario, the traffic of the bypass VXLAN tunnel must traverse the peer-link physical connection. In a virtual peer-link scenario, the traffic of the bypass VXLAN tunnel can be forwarded based on routes.

![](../public_sys-resources/note_3.0-en-us.png) 

In a virtual peer-link scenario, if a bypass VXLAN tunnel already exists when you configure the peer-link, you do not need to configure the tunnel again.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLANIF interface view.
   
   
   ```
   [interface](cmdqueryname=interface) vlanif vlan-id
   ```
3. Configure an IP address for the VLANIF interface of the peer-link interface. This address is used as the source IP address of the static bypass VXLAN tunnel.
   
   
   * In an underlay IPv4 VXLAN scenario, run the following commands:
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     ```
   * In an underlay IPv6 VXLAN scenario, run the following commands:
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ]
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     If the [**vxlan tunnel-status track exact-route**](cmdqueryname=vxlan+tunnel-status+track+exact-route) command has been run on a device, subscription to the status of exact routes to the VXLAN tunnel destination is enabled. The tunnel status is up only when exact routes to the tunnel destination IP address are reachable. In this case, you are advised to use loopback addresses to establish a bypass VXLAN tunnel between M-LAG devices.
4. (Optional) Reserve the VLANIF interface IP address for the bypass VXLAN tunnel.
   
   
   ```
   [reserved for vxlan bypass](cmdqueryname=reserved+for+vxlan+bypass)
   ```
   
   By default, the IP address of a VLANIF interface is not reserved for exclusive use by the bypass VXLAN tunnel.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the M-LAG configuration consistency check is enabled by running the [**consistency-check enable**](cmdqueryname=consistency-check+enable) command on M-LAG member devices, the configurations of VLANIF interfaces for peer-link interfaces on the M-LAG master and backup devices are checked. If the configurations are inconsistent, an alarm is reported. In this case, you can run this command to configure the IP address of the VLANIF interface for a peer-link interface to be used exclusively by the bypass VXLAN tunnel, and then configure the system to perform any consistency check on VLANIF interfaces' IP and MAC addresses on the M-LAG master and backup devices. If they are consistent, the system reports an alarm.
5. Exit the VLANIF interface view.
   
   
   ```
   quit
   ```
6. Enter the NVE interface view.
   
   
   ```
   [interface](cmdqueryname=interface) nve nve-number
   ```
7. Create a static bypass VXLAN tunnel and specify the source and peer addresses.
   
   
   ```
   [pip-source](cmdqueryname=pip-source) src-ip peer peer-ip bypass
   ```
   
   By default, no static bypass VXLAN tunnel is created between M-LAG devices.
   
   The values of *src-ip* and *peer-ip* are IPv4 addresses in an underlay IPv4 VXLAN scenario, and IPv6 addresses in an underlay IPv6 VXLAN scenario.![](../public_sys-resources/note_3.0-en-us.png) 
   * In a physical peer-link scenario, ensure that the outbound interface of the bypass VXLAN tunnel (the outbound interface of the route to *peer-ip*) is the peer-link interface. Otherwise, the bypass VXLAN tunnel may fail to forward traffic.
   * An IPv4 bypass VXLAN tunnel and an IPv6 bypass VXLAN tunnel are mutually exclusive.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
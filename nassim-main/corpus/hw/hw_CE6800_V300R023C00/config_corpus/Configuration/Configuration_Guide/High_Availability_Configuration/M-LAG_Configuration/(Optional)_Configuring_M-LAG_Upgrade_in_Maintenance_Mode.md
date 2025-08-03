(Optional) Configuring M-LAG Upgrade in Maintenance Mode
========================================================

(Optional) Configuring M-LAG Upgrade in Maintenance Mode

#### Context

To implement the upgrade in maintenance mode on a device, you need to configure a routing protocol on the device to be upgraded, and enable the function of setting member interfaces of the Eth-Trunk interface that functions as the M-LAG member interface to down, to switch traffic to the backup link. After the device upgrade is complete, delete the traffic switching configuration to switch traffic back to the upgraded device.

M-LAG upgrade in maintenance mode supports the following network-side routing protocols: OSPF, OSPFv3, BGP, and BGP4+.

For the CE6885-LL (low latency mode): IPv6-related configurations are not supported.

![](../public_sys-resources/note_3.0-en-us.png) 

The maintenance view is controlled by a license (CE-LIC-LU). You need to load the license before entering the maintenance view.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the maintenance view.
   
   
   ```
   [maintenance](cmdqueryname=maintenance)
   ```
3. Perform one of the following steps depending on the route type to implement network-side traffic switching:
   
   
   * OSPF routes: Configure the device to change the costs of all its OSPF LSAs to be advertised to the maximum values.
     ```
     [ospf advertise max-cost](cmdqueryname=ospf+advertise+max-cost)
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL (low latency mode) does not support this command.
     
     By default, a device does not change the costs of any of its OSPF LSAs to be advertised to the maximum value.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     After the [**ospf advertise max-cost**](cmdqueryname=ospf+advertise+max-cost) command is run, the device changes the costs of all its OSPF LSAs to be advertised to their maximum values. The costs of router-LSAs (Type 1) are increased to 65535, and the costs of summary-LSAs (Type 3 and Type 4), AS-external-LSAs (Type 5), and NSSA-LSAs (Type 7) are all increased to 16711680.
   * OSPFv3 routes: Configure the device to change the costs of all its OSPFv3 LSAs to be advertised to their maximum values.
     ```
     [ospfv3 advertise max-cost](cmdqueryname=ospfv3+advertise+max-cost)
     ```
     
     By default, a device does not change the cost of any of its OSPFv3 LSAs to be advertised to the maximum value.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     After the [**ospfv3 advertise max-cost**](cmdqueryname=ospfv3+advertise+max-cost) command is run, the device changes the costs of all its OSPFv3 LSAs to be advertised to their maximum values. The costs of router-LSAs (Type 1) are increased to 65535, and the costs of inter-area-prefix-LSAs (Type 3), inter-area-router-LSAs (Type 4), AS-external-LSAs (Type 5), and NSSA-LSAs (Type 7) are all increased to 16711680.
   * BGP-IPv4 unicast address family and BGP-VPN instance IPv4 address family routes: Enable BGP to set the priorities of BGP-IPv4 unicast address family and BGP-VPN instance IPv4 address family routes to be advertised to the lowest.
     ```
     [advertise bgp ipv4-family unicast lowest-priority enable](cmdqueryname=advertise+bgp+ipv4-family+unicast+lowest-priority+enable)
     ```
     
     By default, BGP does not set the priorities of BGP routes to be advertised to the lowest.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The [**advertise bgp ipv4-family unicast lowest-priority enable**](cmdqueryname=advertise+bgp+ipv4-family+unicast+lowest-priority+enable) and [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) commands can be used to control route advertisement. Either command can enable BGP to set the priorities of routes to be advertised in the preceding address families to the lowest when BGP peers in these address families go from down to up.
     
     After the [**advertise bgp ipv4-family unicast lowest-priority enable**](cmdqueryname=advertise+bgp+ipv4-family+unicast+lowest-priority+enable) command is run, the MED and Local\_Pref attributes of BGP routes to be advertised cannot be modified through an export routing policy.
   * BGP-IPv6 unicast address family and BGP-VPN instance IPv6 address family routes: Enable BGP to set the priorities of BGP-IPv6 unicast address family and BGP-VPN instance IPv6 address family routes to be advertised to the lowest.
     ```
     [advertise bgp ipv6-family unicast lowest-priority enable](cmdqueryname=advertise+bgp+ipv6-family+unicast+lowest-priority+enable)
     ```
     
     By default, BGP does not set the priorities of BGP routes to be advertised to the lowest.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The [**advertise bgp ipv6-family unicast lowest-priority enable**](cmdqueryname=advertise+bgp+ipv6-family+unicast+lowest-priority+enable) and [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) commands can be used to control route advertisement. Either command can enable BGP to set the priorities of routes to be advertised in the preceding address families to the lowest when BGP peers in these address families go from down to up.
     
     After the [**advertise bgp ipv6-family unicast lowest-priority enable**](cmdqueryname=advertise+bgp+ipv6-family+unicast+lowest-priority+enable) command is run, the MED and Local\_Pref attributes of BGP routes to be advertised cannot be modified through an export routing policy.
   * EVPN address family routes: Enable BGP to set the priorities of EVPN address family routes to be advertised to the lowest.
     ```
     [advertise bgp l2vpn-family evpn lowest-priority enable](cmdqueryname=advertise+bgp+l2vpn-family+evpn+lowest-priority+enable)
     ```
     
     By default, BGP does not set the priorities of BGP routes to be advertised to the lowest.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The [**advertise bgp l2vpn-family evpn lowest-priority enable**](cmdqueryname=advertise+bgp+l2vpn-family+evpn+lowest-priority+enable) and [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) commands can be used to control route advertisement. Either command can enable BGP to set the priorities of routes to be advertised in the preceding address family to the lowest when BGP peers in the address family go from down to up.
     
     After the [**advertise bgp l2vpn-family evpn lowest-priority enable**](cmdqueryname=advertise+bgp+l2vpn-family+evpn+lowest-priority+enable) command is run, the MED and Local\_Pref attributes of BGP routes to be advertised cannot be modified through an export routing policy.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
5. Enable the function of setting member interfaces of the Eth-Trunk interface that functions as the M-LAG member interface to down to trigger user-side traffic switching. (This configuration does not take effect on M-LAG member interfaces in active/standby mode.)
   
   
   ```
   [lacp force-down](cmdqueryname=lacp+force-down)
   ```
   
   By default, the function of forcibly setting member interfaces of the Eth-Trunk interface that functions as the M-LAG member interface to down is disabled.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
7. Upgrade the device. After the upgrade is complete, perform the following steps to switch traffic back to the upgraded device.
8. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
9. Enter the maintenance view.
   
   
   ```
   [maintenance](cmdqueryname=maintenance)
   ```
10. Disable the function of setting member interfaces of the Eth-Trunk interface that functions as the M-LAG member interface to down. This allows user-side traffic to be switched back to the upgraded device. (This configuration does not take effect on M-LAG member interfaces in active/standby mode.)
    
    
    ```
    [undo lacp force-down](cmdqueryname=undo+lacp+force-down)
    ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
12. Perform one of the following steps depending on the route type to switch network-side traffic back to the upgraded device:
    
    
    * OSPF routes: Configure the device to restore the costs of all its OSPF LSAs to be advertised to the original values.
      ```
      [undo ospf advertise max-cost](cmdqueryname=undo+ospf+advertise+max-cost)
      ```
    * OSPFv3 routes: Configure the device to restore the costs of all its OSPFv3 LSAs to be advertised to the original values.
      ```
      [undo ospfv3 advertise max-cost](cmdqueryname=undo+ospfv3+advertise+max-cost)
      ```
    * BGP-IPv4 unicast address family and BGP-VPN instance IPv4 address family routes: Disable BGP from setting the priorities of BGP-IPv4 unicast address family and BGP-VPN instance IPv4 address family routes to be advertised to the lowest.
      ```
      [undo advertise bgp ipv4-family unicast lowest-priority enable](cmdqueryname=undo+advertise+bgp+ipv4-family+unicast+lowest-priority+enable)
      ```
    * BGP-IPv6 unicast address family and BGP-VPN instance IPv6 address family routes: Disable BGP from setting the priorities of BGP-IPv6 unicast address family and BGP-VPN instance IPv6 address family routes to be advertised to the lowest.
      ```
      undo advertise bgp ipv6-family unicast lowest-priority enable
      ```
    * EVPN address family routes: Disable BGP from setting the priorities of EVPN address family routes to be advertised to the lowest.
      ```
      undo advertise bgp l2vpn-family evpn lowest-priority enable
      ```
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
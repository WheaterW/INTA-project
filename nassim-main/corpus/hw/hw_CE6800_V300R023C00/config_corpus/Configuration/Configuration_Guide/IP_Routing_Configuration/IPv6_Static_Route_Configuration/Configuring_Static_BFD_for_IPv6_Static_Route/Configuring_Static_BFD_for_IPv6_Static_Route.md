Configuring Static BFD for IPv6 Static Route
============================================

Configuring Static BFD for IPv6 Static Route

#### Prerequisites

Before configuring static BFD for IPv6 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of each interface is up.

#### Context

To configure static BFD for IPv6 static route, you need to configure a static BFD session and then bind the static route to the BFD session.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Exit the BFD session view and return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Create a BFD session and enter the BFD session view.
   
   
   ```
   [bfd](cmdqueryname=bfd) session-name bind peer-ipv6 peer-ipv6
   ```
5. Set a local discriminator for the BFD session.
   
   
   ```
   [discriminator](cmdqueryname=discriminator) local discr-value
   ```
6. Set a remote discriminator for the BFD session.
   
   
   ```
   [discriminator](cmdqueryname=discriminator) remote discr-value
   ```
7. Exit the BFD session view and return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Perform either of the following operations to configure an IPv6 static route and bind it to the static BFD session.
   
   
   * Configure an IPv6 static route on the public network and bind it to the static BFD session.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length { nexthop-ipv6-address | interface-type interface-number } track bfd-session cfg-name
     ```
   * Configure an IPv6 static route in a specified VPN instance and bind it to the static BFD session.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) vpn-instance vpn-source-name dest-ipv6-address prefix-length { nexthop-ipv6-address | interface-type interface-number } track bfd-session cfg-name 
     ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   BFD is bidirectional. Therefore, BFD sessions must be configured on both ends of the link corresponding to a static route.
9. (Optional) Disable the IPv6 static routes bound to a BFD session from participating in route selection when the BFD session is in the AdminDown state.
   
   
   ```
   [ipv6 route-static track bfd-session session name](cmdqueryname=ipv6+route-static+track+bfd-session+session+name) bfd-name admindown invalid
   ```
   
   By default, static routes can participate in route selection even when the BFD session bound to them is in the AdminDown state. However, this is not the case for some non-Huawei devices. As a result, Huawei devices cannot interwork with such non-Huawei devices. In this case, you can perform this step to disable the IPv6 static routes bound to a BFD session from participating in route selection when the BFD session is in the AdminDown state. This unifies the static route processing mode on the Huawei and non-Huawei devices in this scenario.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
Configuring Static BFD for IPv4 Static Route
============================================

Configuring Static BFD for IPv4 Static Route

#### Prerequisites

Before configuring static BFD for IPv4 static route, you have completed the following task:

* Set data link layer protocol parameters for interfaces to ensure that the data link layer protocol status of the interfaces is up.

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
   [bfd](cmdqueryname=bfd) session-name bind peer-ip peer-ip
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
8. Perform either of the following operations to configure an IPv4 static route and bind it to the static BFD session.
   
   
   * Configure an IPv4 static route on the public network and bind it to a static BFD session.
     ```
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } { nexthop-address | { interface-name | interface-type interface-number } [ nexthop-address ] | vpn-instance vpn-instance-name nexthop-address } track bfd-session cfg-name [ description text ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   * Configure an IPv4 static route in a specified VPN instance and bind it to a BFD session.
     ```
     [ip route-static vpn-instance](cmdqueryname=ip+route-static+vpn-instance) vpn-source-name destination-address { mask | mask-length } { nexthop-address | { interface-name | interface-type interface-number } [ nexthop-address ] } track bfd-session cfg-name [ description text ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   BFD is bidirectional. Therefore, BFD sessions must be configured on both ends of the link corresponding to a static route.
9. (Optional) Disable the IPv4 static routes bound to a BFD session from participating in route selection when the BFD session is in the AdminDown state.
   
   
   ```
   [ip route-static track bfd-session session name](cmdqueryname=ip+route-static+track+bfd-session+session+name) bfd-name admindown invalid
   ```
   
   By default, static routes can participate in route selection even when the BFD session bound to them is in the AdminDown state. However, this is not the case for some non-Huawei devices. As a result, Huawei devices cannot interwork with such non-Huawei devices. In this case, you can perform this step to disable the IPv6 static routes bound to a BFD session from participating in route selection when the BFD session is in the AdminDown state. This unifies the static route processing mode on the Huawei and non-Huawei devices in this scenario.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
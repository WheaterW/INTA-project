Configuring BGP Multi-Instance
==============================

BGP multi-instance allows routes to be managed and maintained separately.

#### Context

By default, all BGP routes are stored in the BGP base instance, meaning that it is impossible to implement separate route management and maintenance. BGP multi-instance can solve this problem. A device can run two types of BGP instances simultaneously: BGP base instance and BGP multi-instance. They are independent of each other and can have either the same or different AS numbers. You can deploy different address families for the BGP base instance and BGP multi-instance based on network deployment requirements to carry different routes and implement separate route management and maintenance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VPN instance and enter the VPN instance view.
   
   
   ```
   [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
   ```
3. Enable the VPN instance IPv4 address family and enter the VPN instance IPv4 address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family)
   ```
4. Configure an RD for the VPN instance IPv4 address family.
   
   
   ```
   [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
   ```
5. Configure VPN targets for the VPN instance IPv4 address family.
   
   
   ```
   [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [vrfRtType ]
   ```
6. Enter the VPN instance view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Enter the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Enter the BGP multi-instance view.
   
   
   ```
   [bgp](cmdqueryname=bgp+instance) as-number instance instance-name
   ```
9. Specify the IP address of a peer and the number of the AS where the peer resides.
   
   
   ```
   [peer](cmdqueryname=peer) ipv4-address [as-number](cmdqueryname=as-number) as-number
   ```
   
   The IP address can be one of the following:
   
   * IP address of an interface on a directly connected peer
   * IP address of a sub-interface on a directly connected peer
   * IP address of a routable loopback interface on the peer
10. (Optional) Configure a dynamic multi-instance peer group.
    1. (Optional) Set the maximum number of dynamic BGP peer sessions that can be established.
       
       
       ```
       [bgp dynamic-session-limit](cmdqueryname=bgp+dynamic-session-limit) max-num
       ```
       
       By default, the maximum number of dynamic BGP peer sessions that can be established is 100.
    2. Create a dynamic BGP peer group. **internal** is used to create a dynamic IBGP peer group, and **external** is used to create a dynamic EBGP peer group.
       
       
       ```
       [group](cmdqueryname=group) group-name [listen](cmdqueryname=listen) { internal | external }
       ```
    3. (Optional) Configure the peer AS number for which the dynamic EBGP peer group listens.
       
       
       ```
       [peer](cmdqueryname=peer) group-name [listen-as](cmdqueryname=listen-as) { asn } &<1-6>
       ```
       ![](public_sys-resources/note_3.0-en-us.png) 
       
       You do not need to perform the configurations related to dynamic EBGP peer groups for dynamic IBGP peer groups.
    4. (Optional) Configure the peer AS segment for which the dynamic EBGP peer group listens.
       
       
       ```
       [peer](cmdqueryname=peer+begin-as+end-as) group-name [listen-as-segment](cmdqueryname=listen-as-segment) begin-as begin-asn end-as end-asn
       ```
    5. Specify a network segment for which the dynamic peer group listens.
       
       
       ```
       [peer](cmdqueryname=peer) group-name [listen-net](cmdqueryname=listen-net) ipv4-address [ mask-length | mask ]
       ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the **display bgp** **instance** *instance-name* **vpnv4 all group** command to check information about BGP multi-instance peer groups.
* Run the **display bgp** **instance** *instance-name* **vpnv4 all peer** command to check information about dynamic BGP multi-instance peers.
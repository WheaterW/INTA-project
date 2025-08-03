Configuring VPN Instances and Interfaces
========================================

Configuring VPN Instances and Interfaces

#### Context

Each network node in adaptive routing needs to maintain three routing tables, which respectively correspond to three instances:

* Public network instance: exists on the device by default. The public network routing table is used to advertise the shortest path routing information.
* Non-min VPN instance: needs to be created manually. The routing table of a Non-min VPN instance contains the routing information of the non-shortest paths.
* Mix VPN instance: needs to be created manually. The routing table of a Mix VPN instance contains the routing information of both the shortest and non-shortest paths.

Three types of interfaces need to be configured for network nodes in adaptive routing:

* Access port: connects to a compute node and is bound to a Mix VPN instance.
* Global port: public network interface that connects nodes between groups. It is not bound to any VPN instances.
* Local port: connects to nodes in a group. Two Layer 3 sub-interfaces (min sub-interface and non-min sub-interface) are created on a local port.
  + Min sub-interface: public network interface, which is not bound to any VPN instances.
  + Non-min sub-interface: bound to a Non-min VPN instance.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure Mix VPN and Non-min VPN instances.
   
   
   1. Create a VPN instance and enter the VPN instance view.
      ```
      [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
      ```
   2. Enable the VPN instance IPv4 address family and enter the VPN instance IPv4 address family view.
      ```
      [ipv4-family](cmdqueryname=ipv4-family)
      ```
   3. Configure an RD for the VPN instance IPv4 address family.
      ```
      [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
      ```
   4. Configure VPN targets for the Non-min VPN instance IPv4 address family.
      ```
      [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [ both | export-extcommunity | import-extcommunity ]
      ```
   5. Return to the system view.
      ```
      [quit](cmdqueryname=quit)
      [quit](cmdqueryname=quit)
      ```
   6. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```
3. Configure a global port.
   
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
      ```
   2. Switch the interface working mode from Layer 2 to Layer 3.
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
   3. Exit the interface view.
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Create a Layer 3 sub-interface for the global port and enter the sub-interface view.
      ```
      [interface](cmdqueryname=interface) interface-type interface-number.sub-number
      ```
   5. Configure the description of the sub-interface.
      ```
      [description](cmdqueryname=description) description
      ```
   6. Configure an IP address for the sub-interface.
      ```
      [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
      ```
   7. Configure the encapsulation type for the sub-interface and VLAN associated with the sub-interface.
      ```
      [dot1q termination vid](cmdqueryname=dot1q+termination+vid) low-pe-vid
      ```
   8. Exit the interface view.
      ```
      [quit](cmdqueryname=quit)
      ```
   9. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```
4. Configure a local port.
   
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
      ```
   2. Switch the interface working mode from Layer 2 to Layer 3.
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
   3. Exit the interface view.
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Configure a min sub-interface for the local port.
      1. Create a min sub-interface and enter the sub-interface view.
         ```
         [interface](cmdqueryname=interface) interface-type interface-number.sub-number
         ```
      2. Configure the description of the sub-interface.
         ```
         [description](cmdqueryname=description) description
         ```
      3. Configure an IP address for the sub-interface.
         ```
         [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
         ```
      4. Configure the encapsulation type for the sub-interface and VLAN associated with the sub-interface.
         ```
         [dot1q termination vid](cmdqueryname=dot1q+termination+vid) low-pe-vid
         ```
      5. Exit the interface view.
         ```
         [quit](cmdqueryname=quit)
         ```
      6. Commit the configuration.
         ```
         [commit](cmdqueryname=commit)
         ```
   5. Configure a non-min sub-interface for the local port.
      1. Create a non-min sub-interface and enter the sub-interface view.
         ```
         [interface](cmdqueryname=interface) interface-type interface-number.sub-number
         ```
      2. Configure the description of the sub-interface.
         ```
         [description](cmdqueryname=description) description
         ```
      3. Bind the sub-interface to the Non-min VPN instance.
         ```
         [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
         ```
      4. Configure an IP address for the sub-interface.
         ```
         [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
         ```
      5. Configure the encapsulation type for the sub-interface and VLAN associated with the sub-interface.
         ```
         [dot1q termination vid](cmdqueryname=dot1q+termination+vid) low-pe-vid
         ```
      6. Exit the interface view.
         ```
         [quit](cmdqueryname=quit)
         ```
      7. Commit the configuration.
         ```
         [commit](cmdqueryname=commit)
         ```
5. Configure an access port.
   
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
      ```
   2. Switch the interface working mode from Layer 2 to Layer 3.
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
      
      Decide whether to perform this step based on the actual interface type.
   3. Configure the description of the interface.
      ```
      [description](cmdqueryname=description) description
      ```
   4. Bind the interface to a Mix VPN instance.
      ```
      [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
      ```
   5. Configure an IP address for the interface.
      ```
      [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
      ```
   6. Exit the interface view.
      ```
      [quit](cmdqueryname=quit)
      ```
   7. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```
Configuring Association Between VRRP6 and Interface Status
==========================================================

Configuring Association Between VRRP6 and Interface Status

#### Prerequisites

Before associating VRRP6 with interface status, you have completed the following tasks:

* Configure a VRRP6 group.
* Configure the master and backup devices in the VRRP6 group to work in preemption mode.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Run either of the following commands based on the protocol type of the tracked interface.
   * To track the IPv4 status of the interface, run:
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id track interface { interface-name | interface-type interface-number  } [  value-increased |  value-decreased ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     When you configure a VRRP6 group to track the IPv4 status of an interface, the network-layer protocols of the tracked interface must contain IPv4. Otherwise, the VRRP6 group tracks the link status of the interface.
   * To track the IPv6 status of the interface, run:
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id track ipv6 interface { interface-name | interface-type interface-number  } [  value-increased |  value-decreased ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     When you configure a VRRP6 group to track the IPv6 status of an interface, the network-layer protocols of the tracked interface must contain IPv6. Otherwise, the VRRP6 group tracks the link status of the interface.
   
   By default, a VRRP6 device reduces its priority by 10 if the tracked interface goes down.
   
   * **increase** *value-increased* specifies the value by which a VRRP6 device increases its priority if the tracked interface goes down.
   * **reduce** *value-decreased* specifies the value by which a VRRP6 device reduces its priority if the tracked interface goes down.![](public_sys-resources/note_3.0-en-us.png) 
   * If a device is the IPv6 address owner, its interfaces cannot be tracked.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.
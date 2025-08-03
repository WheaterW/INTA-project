Configuring Static BFD for RIP
==============================

Configuring Static BFD for RIP

#### Prerequisites

Before configuring static BFD for RIP, you have completed the following tasks:

* Assign an IP address to each interface to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic RIP functions](vrp_rip_cfg_0008.html).


#### Context

Establishing BFD sessions between RIP neighbors enables the rapid detection of link faults and speeds up RIP's response to network topology changes. If all the devices on a network support BFD, configure BFD on both ends to implement fault detection. To configure a static BFD session, you need to manually configure BFD detection using commands so that BFD session establishment requests can be delivered.


#### Procedure

1. Enable BFD globally.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable BFD globally.
      
      
      ```
      [bfd](cmdqueryname=bfd)
      ```
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Configure static BFD for RIP.
   1. Create a BFD session.
      
      
      ```
      [bfd](cmdqueryname=bfd) session-name bind peer-ip peer-ip [ interface interface-type interface-number ] [ source-ip source-ip ]
      ```
      
      
      
      If **peer-ip** and **interface** are specified, BFD only monitors a single-hop link with **interface** as the outbound interface and **peer-ip** as the next hop address.
   2. Configure the local device's local discriminator to be the same as the remote device's remote discriminator.
      
      
      * Configure the local discriminator.
      ```
      [discriminator](cmdqueryname=discriminator) local discr-value
      ```
      
      
      * Configure the remote discriminator.
      ```
      [discriminator](cmdqueryname=discriminator) remote discr-value
      ```
      
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      The local device's local discriminator and remote discriminator must be the same as the remote device's remote discriminator and local discriminator, respectively. Otherwise, a BFD session cannot be established.
      
      Specifically, **local** *discr-value* of the local device must be the same as the **remote** *discr-value* of the remote device, and **remote** *discr-value* of the local device must be the same as **local** *discr-value* of the remote device.
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. Enable static BFD on an interface.
   1. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Enable static BFD on the interface.
      
      
      ```
      [rip bfd static](cmdqueryname=rip+bfd+static)
      ```
   3. (Optional) Enable static BFD for a specified neighbor.
      
      
      ```
      [rip bfd static binding](cmdqueryname=rip+bfd+static+binding) peer-address
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      If you run both this command and the [**rip bfd static**](cmdqueryname=rip+bfd+static) command, the latest configuration overrides the previous one. This command will change the existing BFD configuration mode.
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

After completing the configuration, run the [**display rip**](cmdqueryname=display+rip) *process-id* **interface** [ *interface-type* *interface-number* ] **verbose** command to check BFD for RIP configurations on the specified interface.
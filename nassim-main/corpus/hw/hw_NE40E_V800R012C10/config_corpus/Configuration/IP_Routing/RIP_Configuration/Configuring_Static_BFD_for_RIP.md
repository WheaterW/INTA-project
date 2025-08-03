Configuring Static BFD for RIP
==============================

BFD provides link failure detection featuring light load and high speed. Static BFD for RIP is a mode to implement the BFD function.

#### Context

Establishing BFD sessions between RIP neighbors enables the rapid detection of link faults and speeds up RIP's response to network topology changes. On a link that requires fast fault response and supports BFD on both ends, you can configure static BFD on both ends to implement common BFD detection.

To configure a static BFD session, you need to manually configure BFD detection using commands and deliver a BFD session establishment request.


#### Pre-configuration Tasks

Before configuring static BFD for RIP, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* [Configure basic RIP functions](dc_vrp_rip_cfg_0003.html).


#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | ID of a RIP process |
| 2 | Type and number of the interface to be enabled with BFD |



#### Procedure

1. Enable BFD globally.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
2. Configure static BFD.
   1. Run the [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *peer-ip* [ **interface** *interface-type* *interface-number* ] [ **source-ip** *source-ip* ] command to create BFD binding.
      
      
      
      If both **peer-ip** (IP address of the peer end) and **interface** (local interface) are specified, BFD only monitors a single-hop link with **interface** as the outbound interface and **peer-ip** as the next hop address.
   2. Set discriminators.
      
      
      * To set the local discriminator, run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command.
      * To set the remote discriminator, run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command.
      
      The local device's local discriminator and remote discriminator must be the same as the remote device's remote discriminator and local discriminator, respectively. Otherwise, a BFD session cannot be established.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Specifically, **local** *discr-value* of the local device must be the same as the **remote** *discr-value* of the remote device, and **remote** *discr-value* of the local device must be the same as **local** *discr-value* of the remote device.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Enable static BFD on an interface.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of a specified interface.
   2. Run the [**rip bfd static**](cmdqueryname=rip+bfd+static) command to enable static BFD on the interface.
   3. (Optional) Run the [**rip bfd static binding**](cmdqueryname=rip+bfd+static+binding) *peer-address* command to enable static BFD for the specified neighbor.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If you run both this command and the [**rip bfd static**](cmdqueryname=rip+bfd+static) command, the latest configuration overrides the previous one. If the command is run, the existing BFD configuration mode will be changed.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring static BFD for RIP, run the [**display rip**](cmdqueryname=display+rip) *process-id* **interface** [ *interface-type* *interface-number* ] **verbose** command to check the BFD for RIP configuration on a specified interface.
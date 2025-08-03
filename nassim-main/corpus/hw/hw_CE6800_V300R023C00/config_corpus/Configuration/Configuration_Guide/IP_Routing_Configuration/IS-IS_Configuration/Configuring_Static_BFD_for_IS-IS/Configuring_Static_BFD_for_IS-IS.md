Configuring Static BFD for IS-IS
================================

Configuring Static BFD for IS-IS

#### Context

IS-IS detects neighbor state changes through IIH exchanges. By default, if no response is received to three consecutive IIHs within a specified period (30 seconds by default), a neighbor is considered down. For networks that require fast convergence and zero packet loss, IS-IS cannot meet link fault detection requirements. To address this problem, you can configure BFD for IS-IS.

BFD includes static BFD and dynamic BFD. Static BFD is easy to control and flexible to deploy. To save memory and ensure the reliability of key links, you can deploy static BFD on these links. Static BFD helps detect link faults rapidly to achieve fast route convergence.

To configure a static BFD session, you need to manually set parameters for the BFD session, including the local and remote discriminators.

![](public_sys-resources/note_3.0-en-us.png) 

Currently, BFD sessions cannot detect route switching. If a change in the bound peer IP address causes a route to switch to another link, the BFD session is renegotiated only when the original link fails.



#### Procedure

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
4. Create a binding between a BFD for IS-IS session and a peer IP address, and then enter the BFD session view.
   
   
   ```
   [bfd](cmdqueryname=bfd) session-name bind peer-ip peer-ip [ interface { interface-name | interface-type interface-number } ]
   ```
   
   
   
   If **peer-ip** and **interface** are specified, BFD only monitors a single-hop link with **interface** as the outbound interface and **peer-ip** as the next hop address.
5. Configure discriminators.
   
   
   * Configure a local discriminator.
     ```
     [discriminator](cmdqueryname=discriminator) local discr-value
     ```
   * Configure a remote discriminator.
     ```
     [discriminator](cmdqueryname=discriminator) remote discr-value
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The **local** *discr-value* on the local device must be the same as the **remote** *discr-value* on the remote device, and the **remote** *discr-value* on the local device must be the same as the **local** *discr-value* on the remote device. Otherwise, no BFD sessions can be established between the two devices. In addition, the local and remote discriminators cannot be modified after being configured.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
8. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
9. Enable static BFD for IS-IS on the interface.
   
   
   ```
   [isis bfd static](cmdqueryname=isis+bfd+static)
   ```
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **session** { **peer**  *peer-address* | **all** } command to check BFD session information.
* Run the [**display isis interface**](cmdqueryname=display+isis+interface) **verbose** command to check the configurations of BFD for IS-IS on interfaces.
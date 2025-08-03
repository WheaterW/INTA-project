Configuring Static BFD for IS-IS
================================

BFD can provide link fault detection featuring light load and high speed (within milliseconds). Static BFD needs to be configured.

#### Usage Scenario

On IS-IS networks, IS-IS neighbors periodically send Hello packets to detect neighbor status changes. For networks that require fast convergence and zero packet loss, IS-IS is unreliable to detect link faults. To address this issue, configure BFD for IS-IS.

BFD includes static BFD and dynamic BFD. Static BFD is easy to control and flexible to deploy. To save memory and ensure the reliability of key links, implement BFD on these links. Static BFD helps detect link faults rapidly and implement fast route convergence.

To configure a static BFD session, you need to manually configure BFD session parameters, including the local and remote discriminators.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

BFD detects only the one-hop link between IS-IS neighbors because IS-IS establishes only one-hop neighbors.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   Global BFD is enabled on the local end.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. (Optional) To configure BFD session check for an IS-IS process, perform the following steps:
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**bfd session-up check**](cmdqueryname=bfd+session-up+check)
      
      
      
      BFD session check is configured for the IS-IS process.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the Layer 2 network is normal, IS-IS neighbor relationships can be established and routes can be delivered. However, if the Layer 3 network is unreachable, upper-layer traffic loss occurs. To resolve this problem, configure BFD session check for an IS-IS process by running the [**bfd session-up check**](cmdqueryname=bfd+session-up+check) command. This ensures that an IS-IS neighbor relationship is established only when the BFD session is up on corresponding interfaces. After this function is configured, it applies only to the neighbor relationships to be established (it does not apply to existing neighbor relationships).
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   BFD can be enabled on physical interfaces only.
6. Run [**isis bfd static**](cmdqueryname=isis+bfd+static)
   
   
   
   Static BFD is enabled on the interface.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *peer-ip* [ **interface** { *interface-name* | *interface-type interface-number* } ]
   
   
   
   A BFD session is created and its view is displayed.
   
   
   
   If both **peer-ip** (IP address of the peer end) and **interface** (local interface) are specified, BFD only monitors a single-hop link with **interface** as the outbound interface and **peer-ip** as the next hop address.
9. Configure a discriminator.
   
   
   * To set the local discriminator, run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command.
   * To set the remote discriminator, run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local discriminator of the local device must be the same as the remote discriminator of the peer device, and the remote discriminator of the local device must be the same as the local discriminator of the peer device.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **session** { **peer** *ip-address* | **all** } command to view the information about the BFD session.
* Run the [**display isis interface**](cmdqueryname=display+isis+interface) **verbose** command to view the configurations of BFD for IS-IS on an interface.
Configuring MAC Accounting for a Broadcast Domain
=================================================

MAC accounting can be enabled for a specified broadcast domain, allowing the device to collect Layer 2 traffic statistics of the target domain based on MAC addresses.

#### Usage Scenario

MAC accounting applies to the following scenario:

* If a device is under DDoS attacks, enable MAC accounting, allowing the device to collect the statistics of traffic from each peer based on MAC addresses. If the traffic from a peer is huge, the peer may be an attack source.


#### Pre-configuration Tasks

Before configuring MAC accounting for a broadcast domain, complete the following task:

* Complete the target broadcast domain configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* MAC accounting applies only to the BD and VSI types of broadcast domains.
* MAC accounting does not apply to VSIs in bridge mode or PBB mode.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Enable MAC accounting for a broadcast domain.
   
   
   
   Enable MAC accounting for a BD.
   
   
   
   1. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
      
      
      
      The BD view is displayed.
   2. Run [**mac accounting enable**](cmdqueryname=mac+accounting+enable)
      
      
      
      MAC accounting is enabled for the BD.
   
   
   
   Enable MAC accounting for a VSI.
   
   
   
   1. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
      
      
      
      The VSI view is displayed.
   2. Run [**mac accounting enable**](cmdqueryname=mac+accounting+enable)
      
      
      
      MAC accounting is enabled for the VSI.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display mac-address**](cmdqueryname=display+mac-address) command to check the MAC address-based accounting statistics of the broadcast domain.
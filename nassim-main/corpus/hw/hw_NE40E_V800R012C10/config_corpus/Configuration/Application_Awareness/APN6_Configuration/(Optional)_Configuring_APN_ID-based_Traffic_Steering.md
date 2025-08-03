(Optional) Configuring APN ID-based Traffic Steering
====================================================

You can configure APN ID-based traffic steering to recurse a route to an SRv6 TE Policy based on APN IDs, thereby ensuring traffic is forwarded through a path in the SRv6 TE Policy.

#### Prerequisites

Configure an SRv6 TE Policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   The SRv6 view is displayed.
3. Run [**mapping-policy**](cmdqueryname=mapping-policy)*name-value* **color***color-value*
   
   
   
   An SRv6 mapping policy is created, and its view is displayed.
4. (Optional) Run [**description**](cmdqueryname=description) *description-value*
   
   
   
   A description is configured for the SRv6 mapping policy.
5. Run [**match-type apn-id-ipv6**](cmdqueryname=match-type+apn-id-ipv6)
   
   
   
   The mapping type of the SRv6 mapping policy is set to APN ID.
6. Run the following commands as required to map an APN ID instance with an SRv6 TE Policy or native IP link in an SRv6 TE flow group.
   
   
   * **index** *index-value* **[**instance**](cmdqueryname=instance)** *instance-name* **match** { **srv6-te-policy** **color** **color-value** | **native-ip** }
   * **default** **[**match**](cmdqueryname=match)** { **srv6-te-policy** **color** **color-value** | **native-ip** }
   
   
   
   An APN ID instance can map with only one SRv6 TE Policy or native IP link. A path can be mapped with an APN ID instance only when the path is in the up state.
   
   When a packet carrying an APN ID is sent to an SRv6 TE flow group, a device forwards it based on the following rules:
   1. The device searches for a mapping SRv6 TE Policy or native IP link according to the *index-value* sequence. If a mapping path is found, the packet is forwarded over this path.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The *index-value* sequence means that an APN ID instance with a smaller *index-value* has a higher priority during path searching. Specifically, if multiple APN ID instances have the same APN ID, the search for a mapping path starts from the APN ID instance with the smallest *index-value*.
   2. If no mapping path is found or the mapping path is faulty, the packet is forwarded over the SRv6 TE Policy or native IP link specified in the **default** command. However, if the **default** command is not run or the path specified in **default** command is not up, a path corresponding to the APN ID instance with the smallest *index-value* is selected among the paths that are in the up state.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For APN ID instances of low-priority services, you are advised to set a small *index-value*. This ensures that, when no path maps with the APN ID of a packet, the packet preferentially preempts the bandwidth of low-priority services.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the SRv6 view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
   
   
   
   A tunnel policy is created, and its view is displayed.
10. (Optional) Run [**description**](cmdqueryname=description) *description-text*
    
    
    
    A description is configured for the tunnel policy.
11. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6** **srv6-te-flow-group** **load-balance-number** *loadBalanceNumber*
    
    
    
    A tunnel selection policy is configured.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

1. Run the [**display srv6-te flow-group**](cmdqueryname=display+srv6-te+flow-group) command to check detailed status information of SRv6 TE flow groups.
2. Run the [**display srv6-te flow-group last-down-reason**](cmdqueryname=display+srv6-te+flow-group+last-down-reason) command to check the records of SRv6 TE flow groups that entered the down state.
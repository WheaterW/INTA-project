Configuring an SRv6 TE Policy
=============================

An SRv6 TE Policy can either be configured manually or be delivered by a controller. This section describes how to configure an SRv6 TE Policy manually.

#### Context

SRv6 TE Policies are used to direct traffic to traverse an SRv6 TE network. Each SRv6 TE Policy can have multiple candidate paths with different preferences. From the valid candidate paths, the one with the highest preference is selected as the primary path, and the one with the second highest preference is selected as the backup path.


#### Procedure

1. Configure a segment list.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Run [**segment-list**](cmdqueryname=segment-list) *list-name*
      
      
      
      A segment list is created for the SRv6 TE Policy candidate path, and the segment list view is displayed.
   4. Run [**index**](cmdqueryname=index) *index* **sid** **ipv6** *ipv6address* [ **compress** **block** *block-value* ] [ **compress****-16** **block** *block-value* **node-length** *node-length-value* **function-length** *function-length-value* [ **compress-flavor** { ****coc-next**** | ****next**** | ****coc**** } ] ] [ **verification** ]
      
      
      
      The next-hop SID in the segment list is specified.
      
      
      
      You can run the command multiple times to specify multiple SIDs. According to [**index**](cmdqueryname=index) *index*, the system generates a SID stack in ascending order. If a candidate path in the SRv6 TE Policy is preferentially selected, traffic is forwarded using the segment lists of the candidate path. A maximum of 10 SIDs can be configured for each segment list.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In SRv6 SRH compression scenarios, pay attention to the following points:
      
      1. When configuring a segment list in 32-bit compression mode, you need to configure the **compress** **block** *block-value* parameter, with the value of *block-value* being the same as that of *block-length* specified in the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* **compress** **block** *block-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ] command.
      2. When configuring a segment list in 16-bit compression mode, you need to configure the ****compress-16********block**** **block-value** parameter, with the value of *block-value* being the same as the value obtained by subtracting 16 from the value of *mask-length* specified in the **locator** *locator-name* **compress-16** **ipv6-prefix** *ipv6-address* *mask-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* command.
      3. In 32-bit compression mode, the last SID in a segment list cannot be of the COC type.
      4. If the **verification** parameter is configured, the system performs IGP route reachability verification for the specified SID in the SRv6 TE Policy. Do not configure this parameter for any cross-domain or binding SID. Otherwise, the verification fails due to IGP route unreachability.
      5. In the SRv6 SRH, 16-bit compressed SIDs with the **node-length** value of 0 do not support fault detection or enhanced fault detection. If the **verification** parameter is configured in the command, the command configuration fails to be delivered. If fault detection is enabled, the verification result is Up regardless of whether 16-bit compressed SIDs with the **node-length** value of 0 are reachable.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure an SRv6 TE Policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. (Optional) Run [**local-end-x encapsulation**](cmdqueryname=local-end-x+encapsulation)
      
      
      
      The function of encapsulating the first-hop local End.X SID is enabled.
   4. (Optional) Run [**ttl-mode**](cmdqueryname=ttl-mode) { **uniform** | **pipe** }
      
      
      
      A TTL processing mode is configured for SRv6 TE Policies to which public network IP routes recurse.
   5. (Optional) Run [**srv6-te-policy switch-delay**](cmdqueryname=srv6-te-policy+switch-delay) *switchDelay* **delete-delay** *deleteDelay*
      
      
      
      Switching and deletion delays are configured for all SRv6 TE Policies.
   6. Run [**srv6-te-policy locator**](cmdqueryname=srv6-te-policy+locator) *locator-name*
      
      
      
      A locator to be associated with the SRv6 TE Policy is configured. This configuration allows you to specify a binding SID for the SRv6 TE Policy in the locator range.
   7. Run [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* **endpoint** *endpoint-ip* **color** *color-value*
      
      
      
      An SRv6 TE Policy is created, and the SRv6 TE Policy view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In color-only scenarios, *endpoint-ip* needs to be set to **::**.
   8. (Optional) Run [**encapsulation-mode**](cmdqueryname=encapsulation-mode) { **insert** | **encaps** | **insert-encaps** }
      
      
      
      An SRv6 TE Policy encapsulation mode is configured.
      
      
      
      When forwarded data enters an SRv6 TE Policy, new SID stack encapsulation is required. If no service SID is available, the SRv6 TE Policy needs to support the **encaps** encapsulation mode. Otherwise, the endpoint cannot remove the SRv6 encapsulation. The headend of the SRv6 TE Policy encapsulates IPv6 header and SRH information into data when the data enters the SRv6 TE Policy, and the endpoint implements the USD flavor to remove the encapsulated IPv6 header and SRH information.
   9. (Optional) Run [**binding-sid**](cmdqueryname=binding-sid) *binding-sid*
      
      
      
      A binding SID is specified for the SRv6 TE Policy.
      
      
      
      The value of *binding-sid* must be within the static range defined using the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command.
   10. Run [**candidate-path preference**](cmdqueryname=candidate-path+preference) *preference*
       
       
       
       A candidate path with a specified preference is configured for the SRv6 TE Policy.
       
       
       
       Each SRv6 TE Policy supports multiple candidate paths. A larger *preference* value indicates a higher candidate path preference. If multiple candidate paths are configured, the one with the highest preference takes effect.
   11. Run [**segment-list**](cmdqueryname=segment-list) *list-name* [ **weight** *weight-value* | **path-mtu** *mtu-value* | **binding-sid** *binding-sid-value* | **reverse-binding-sid** *reverse-binding-sid-value* ] \*
       
       
       
       A segment list is configured for the candidate path of the SRv6 TE Policy.
       
       
       
       The segment list must have been created using the [**segment-list (Segment-routing IPv6 view)**](cmdqueryname=segment-list+%28Segment-routing+IPv6+view%29) command.
       
       In unaffiliated BFD (U-BFD) for SRv6 TE Policy scenarios, return packets are forwarded through IPv6 routes by default, which may cause the U-BFD status to be incorrect. To enable U-BFD return packets to be forwarded through an SRv6 TE Policy, use the **reverse-binding-sid** *reverse-binding-sid-value* parameter to specify a binding SID for the reverse segment list. Alternatively, use the **binding-sid** *binding-sid-value* parameter to specify a binding SID for the local segment list so that the peer end can reference this SID.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
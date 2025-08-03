Configuring TE-Class-based Traffic Steering into an SRv6 TE Policy
==================================================================

You can configure TE-Class-based traffic steering to recurse a route to an SRv6 TE Policy based on TE-Class IDs, so that traffic can be forwarded through a path in the SRv6 TE Policy.

#### Prerequisites

Before configuring TE-Class-based traffic steering into an SRv6 TE Policy, complete the following tasks:

* Configure a traffic classifier.
* Configure an SRv6 TE Policy.

#### Context

After an SRv6 TE Policy is configured, traffic needs to be steered into it for forwarding. This process is called traffic steering. Currently, SRv6 TE Policies can be used for various services, such as BGP L3VPN and EVPN services. This section describes how to configure services to recurse to an SRv6 TE Policy through a specified tunnel policy.

Smart policy routing (SPR) is a route selection mechanism that proactively detects link quality and selects the optimal link to forward service data according to service quality requirements, implementing intelligent traffic steering.

TE-Class IDs can be used to identify flows, helping differentiate the flows and steer them into different SRv6 TE Policies, SPR paths, or native IP links.


#### Procedure

1. Configure TE-Class IDs for traffic.
   1. Configure a traffic classifier. For details, see [Class-based QoS Configuration](../ne/dc_ne_qos_cfg_0037.html).
   2. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   3. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is created, and the traffic behavior view is displayed.
   4. Run [**remark te-class**](cmdqueryname=remark+te-class)*classid*
      
      
      
      A TE-Class ID is configured.
      
      
      
      In SPR traffic steering, multi-field (MF) classification needs to be performed to set different TE-class IDs for different flows based on 5-tuple information. Then, the device queries the FIB based on the destination address of this flow to obtain a mapping policy, in which the path matching the specified TE-Class ID is used for forwarding.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is configured, and the traffic policy view is displayed.
   7. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]
      
      
      
      A traffic behavior is specified for the traffic classifier in the traffic policy, and a policy-based matching priority is set.
   8. (Optional) Run [**statistics enable**](cmdqueryname=statistics+enable)
      
      
      
      The statistics collection function is enabled for the traffic policy.
      
      
      
      To conserve memory resources, the statistics collection function of traffic policies is disabled by default. To check traffic policy statistics, run the [**statistics enable**](cmdqueryname=statistics+enable) command to enable the statistics collection function for the traffic policy.
   9. (Optional) Run [**share-mode**](cmdqueryname=share-mode)
      
      
      
      The traffic policy is enabled to be shared.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
       
       
       
       The interface view is displayed.
   12. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }
       
       
       
       The traffic policy is applied to a Layer 3 interface.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
2. Configure SPR.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      The SRv6 view is displayed.
   2. Run [**smart-policy-route**](cmdqueryname=smart-policy-route)
      
      
      
      SPR is configured, and the SRv6 smart policy route view is displayed.
   3. (Optional) Run **refresh-period** *time-value*
      
      
      
      An update period is configured for SPR route selection.
   4. (Optional) Run **measure count** { **one-way** | **two-way-average** }
      
      
      
      An SPR switching mode is configured.
      
      
      
      In one-way switching, the forward tunnel's data is used for calculation. In two-way switching, the forward and reverse tunnels' data is used for calculation.
   5. Run [**spr-policy**](cmdqueryname=spr-policy) *name-value*
      
      
      
      An SPR policy template is created, and the SRv6 SPR policy view is displayed.
      
      
      
      According to service flow characteristics, traffic is classified and internal priorities (TE-Class) are set, with different internal priorities being mapped to different SPR policies. Intelligent traffic steering is implemented for service flows based on policy configurations.
   6. (Optional) Configure SPR policy parameters.
      
      
      * Run the **switch-period** *time-value* command to configure an SPR switching period.
        
        SPR determines whether to perform a link switchover based on the SLA detection result, which it obtains periodically. If the optimal link computed based on the obtained SLA detection result is different from the currently used link, the switching period timer starts. The timer is reset if the two links are the same before the expiration of the switching period and restarts when the next link inconsistency occurs. If link inconsistency persists during the switching period, SPR performs a link switchover.
        
        Configure a switching period based on service characteristics. For example, configure a short switching period for voice services because they have high requirements on real-time performance.
      * Run the **wait-to-restore-period** *time-value* command to configure an SPR switchback wait-to-restore (WTR) period.
        
        If traffic is switched from an abnormal high-priority link to a low-priority link, SPR immediately switches traffic back to the high-priority link when this link recovers. This causes traffic loss if key services are being transmitted over the low-priority link. After an SPR switchback WTR period is configured, the device does not switch traffic back to the high-priority link when detecting that the link recovers. This ensures the reliable transmission of key services over the low-priority link during this period.
        
        After an SPR switchback WTR period is configured, the device starts the timer when the high-priority link recovers following a traffic switchover to the low-priority link through SPR. If the high-priority link remains normal within the configured switchback period, SPR switches traffic from the low-priority link back to the high-priority link after the switchback period expires. If the device detects that the high-priority link does not meet traffic forwarding requirements within the configured switchback WTR period, it restarts the timer when detecting that the high-priority link recovers next time.
      * Run the **cmi threshold** *value* command to configure a composite measure indicator (CMI) threshold for services in SPR.
        
        The CMI is calculated using the formula D (Delay) + J (Jitter) + L (Loss). A smaller CMI value indicates better link quality.
        
        Many services have requirements for link indicators including the delay, jitter, and packet loss rate. As such, you need to configure a CMI threshold based on service characteristics. If the value calculated using the preceding formula is greater than the configured CMI threshold, the link CMI does not meet service requirements.
      * Run the **delay threshold** *time-value* command to configure a delay threshold for services in SPR.
        
        The service delay threshold is the maximum delay allowed by services. It needs to be specified for services that have link delay requirements. If the delay of a link exceeds the threshold, the link does not meet the delay requirements of services.
      * Run the **jitter threshold** *time-value* command to configure a jitter threshold for services in SPR.
        
        The service jitter threshold is the maximum jitter allowed by services. It needs to be specified for services that have link jitter requirements. If the jitter of a link exceeds the threshold, the link does not meet the jitter requirements of services.
      * Run the **loss threshold** *value* command to configure a threshold for the packet loss rate of services in SPR.
        
        The packet loss rate threshold is the maximum packet loss rate allowed by services. It needs to be specified for services that have requirements for the packet loss rate. If the packet loss rate of a link exceeds the threshold, the link does not meet the packet loss rate requirements of services.
   7. Run [**srv6-te-policy color**](cmdqueryname=srv6-te-policy+color+priority)*color-value* **priority** *priority-value*
      
      
      
      An SRv6 TE Policy is configured for SPR.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the SRv6 view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Configure TE-Class-based traffic steering into an SRv6 TE Policy.
   1. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      The SRv6 view is displayed.
   2. Run [**mapping-policy**](cmdqueryname=mapping-policy)*name-value* **color***color-value*
      
      
      
      An SRv6 mapping policy is created, and the SRv6 mapping policy view is displayed.
   3. (Optional) Run [**description**](cmdqueryname=description) *description-value*
      
      
      
      A description is configured for the SRv6 mapping policy.
   4. Run [**match-type te-class**](cmdqueryname=match-type+te-class)
      
      
      
      The mapping type of the SRv6 mapping policy is set to TE-Class.
   5. Configure a rule for the mapping between SPR policies, SRv6 TE Policies, or native IP links in an SRv6 TE flow group and TE-Class values.
      
      
      * Configure a rule for the mapping between SPR policies in an SRv6 TE flow group and TE-Class values.
        
        [**index**](cmdqueryname=index+te-class+match)*index-value* **te-class** *te-class-id* **match** **spr-policy** *spr-name*
        
        **[**default match spr-policy**](cmdqueryname=default+match+spr-policy)** *spr-name*
      * Configure a rule for the mapping between SRv6 TE Policies in an SRv6 TE flow group and TE-Class values.
        
        **[**index**](cmdqueryname=index+te-class+match)** *index-value* **te-class** *te-class-id* **match** **srv6-te-policy** **color** *color-value*
        
        [**default match srv6-te-policy color**](cmdqueryname=default+match+srv6-te-policy+color) *color-value*
      * Configure a rule for the mapping between native IP links in an SRv6 TE flow group and TE-Class values.
        
        **[**index**](cmdqueryname=index+te-class+match)** *index-value* **te-class** *te-class-id* **match** **native-ip**
        
        [**default match native-ip**](cmdqueryname=default+match+native-ip)
      
      Each SRv6 TE Policy in an SRv6 TE flow group has its own color attribute.
      
      The [**index te-class match**](cmdqueryname=index+te-class+match) and [**default match**](cmdqueryname=default+match) commands are used together to specify the mapping between color and TE-Class values.
      
      In an SRv6 TE flow group, TE-Class values and SRv6 TE Policies are associated using the color attribute. IP packets can then be steered into the specified SRv6 TE Policy based on their TE-Class values.
      
      * The [**index te-class match spr-policy**](cmdqueryname=index+te-class+match+spr-policy) and [**default match spr-policy**](cmdqueryname=default+match+spr-policy) *spr-name* commands configure the mapping between SPR policies and TE-Class values.
      * The [**index te-class match srv6-te-policy color**](cmdqueryname=index+te-class+match+srv6-te-policy+color) and [**default match srv6-te-policy color**](cmdqueryname=default+match+srv6-te-policy+color) *color-value* commands configure the mapping between SRv6 TE Policies and TE-Class values.
      * The [**index te-class match native-ip**](cmdqueryname=index+te-class+match+native-ip) and [**default match native-ip**](cmdqueryname=default+match+native-ip) commands configure the mapping between native IP links and TE-Class values.
      
      During forwarding, IP packets are steered into the specified SRv6 TE Policy based on their TE-Class values. If no SRv6 TE Policy matching a specified TE-Class value is found, the packets are steered into the SRv6 TE Policy specified using the [**default match**](cmdqueryname=default+match) command.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the SRv6 view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
      
      
      
      A tunnel policy is created, and its view is displayed.
   9. (Optional) Run [**description**](cmdqueryname=description) *description-text*
      
      
      
      A description is configured for the tunnel policy.
   10. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **ipv6** **srv6-te-flow-group** **load-balance-number** *loadBalanceNumber*
       
       
       
       A tunnel selection policy is configured.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Because there can be only one effective SRv6 TE Policy with the endpoint and color specified, load balancing is not involved.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
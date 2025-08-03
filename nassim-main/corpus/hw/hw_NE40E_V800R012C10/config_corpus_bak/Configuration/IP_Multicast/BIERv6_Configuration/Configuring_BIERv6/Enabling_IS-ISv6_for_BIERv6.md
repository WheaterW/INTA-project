Enabling IS-ISv6 for BIERv6
===========================

If IS-ISv6 for BIERv6 is enabled on BFRs, BIFTs can be generated on the BIERv6 control plane.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and the IS-IS view is displayed.
3. (Optional) Run [**network-entity**](cmdqueryname=network-entity) **net-addr**
   
   
   
   A network entity title (NET) is configured.
   
   
   
   On a BIERv6 network, all-0 NETs are not supported. If a NET that meets requirements has been configured on the device, skip this step.
4. (Optional) Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** | **compatible** }
   
   
   
   A cost style is set to control route accepting and sending by the IS-IS device.
   
   
   
   The **wide** cost style enables the device to accept and send only the routes whose cost style is wide. The **wide-compatible** enables the device to accept the routes whose cost style is narrow or wide but send only the routes whose cost style is wide. The **compatible** cost style enables the device to accept and send the routes whose cost style is narrow or wide.
   
   On a BIERv6 network, one of the preceding cost styles must be set. If a cost style that meets requirements has been set for the local device, skip this step.
5. (Optional) Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology ipv6**
   
   
   
   The IPv6 topology type is configured.
   
   
   
   On a BIERv6 network, only the IPv6 topology type is supported. If this configuration has been performed for the device, skip this step.
6. (Optional) Run [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** }
   
   
   
   An IS-IS level is configured for the device.
   
   
   
   If this configuration has been performed for the device, skip this step.
7. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+%28IS-IS+view%29) **locator** *locator-name* [ **auto-sid-disable** ]
   
   
   
   IS-IS SRv6 is enabled.
8. Run [**bier enable**](cmdqueryname=bier+enable)
   
   
   
   BIER is enabled in the IS-IS process.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the IS-IS view.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
11. (Optional) Enable IS-IS on interfaces.
    
    
    
    The following operations must be performed on all the interfaces that connect BFRs and on the loopback interface whose IP address is used as the BFR-prefix. If this configuration has been performed for the device, skip this step.
    
    
    
    1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
       
       
       
       The interface view is displayed.
    2. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
       
       
       
       IPv6 is enabled on the interface.
    3. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
       
       
       
       IS-IS IPv6 is enabled on the interface.
    4. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the interface view.
    5. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
12. Repeat [1](#EN-US_TASK_0271431861__step5253145172748) to [11](#EN-US_TASK_0271431861__step1029271815259) to configure all other BFRs on the BIERv6 network.
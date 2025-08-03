Sampling IPv4 Flows
===================

You can enable NetStream to sample and analyze the incoming or outgoing flows on an interface.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a NetStream-enabled interface is bound to a VPN instance, all packets in the VPN instance are sampled.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a sampling mode and sampling ratio by performing at least one of the following steps:
   
   
   * Configure a sampling mode and sampling ratio globally.
     1. Run [**ip netstream sampler**](cmdqueryname=ip+netstream+sampler) { **fix-packets** *packet-interval* | **random-packets** *packet-interval* | **fix-time** *time-interval* } { **inbound** | **outbound** }
        
        A global sampling mode and sampling ratio are configured.
     2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
   * Configure a sampling mode and sampling ratio on an interface.
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
     2. Run [**ip netstream sampler**](cmdqueryname=ip+netstream+sampler) { **fix-packets** *packet-interval* | **random-packets** *packet-interval* | **fix-time** *time-interval* } { **inbound** | **outbound** }
        
        A sampling mode and sampling ratio are configured on the interface.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The sampling mode and sampling ratio configured in the system view are applicable to all interfaces on the device. The sampling mode and sampling ratio configured in the interface view take precedence over those configured in the system view.
3. Run [**ip netstream**](cmdqueryname=ip+netstream) { **inbound** | **outbound** }
   
   
   
   NetStream is enabled on the interface.
   
   Statistics about packets' BGP next-hop information can also be collected. Original flows output in V5 format, however, cannot carry the BGP next-hop information.
4. (Optional) Run [**ip netstream statistics enable**](cmdqueryname=ip+netstream+statistics+enable)
   
   
   
   The traffic statistics diagnosis function is enabled so that you can compare the traffic statistics collected by the device with those restored by the NMS to determine the cause of inaccurate sampling.
5. (Optional) Run [**ip netstream sampler except deny-action**](cmdqueryname=ip+netstream+sampler+except+deny-action)
   
   
   
   NetStream is not applied to traffic matching the ACL rule or traffic behavior that contains **deny**.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The traffic behavior view must be entered before you run this command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
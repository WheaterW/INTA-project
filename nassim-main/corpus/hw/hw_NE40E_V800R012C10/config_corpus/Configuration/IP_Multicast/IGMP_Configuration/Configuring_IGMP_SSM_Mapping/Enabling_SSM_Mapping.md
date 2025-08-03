Enabling SSM Mapping
====================

On the network segment that provides SSM services, interfaces on multicast devices run IGMPv3. Due to various restrictions, some hosts must run IGMPv1 or IGMPv2. To provide SSM services for these hosts, IGMP SSM mapping needs to be configured on the multicast devices' interfaces connected to the user network segment. Enabling SSM mapping is a prerequisite for configuring static SSM mapping. If SSM mapping is not enabled on an interface, SSM source/group address mapping entries cannot take effect on the interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**igmp version**](cmdqueryname=igmp+version) **3**
   
   
   
   The IGMP version is set to 3.
   
   
   
   To ensure that all user hosts (running any IGMP version) can obtain SSM services, IGMPv3 is recommended.
4. Run [**igmp ssm-mapping enable**](cmdqueryname=igmp+ssm-mapping+enable)
   
   
   
   The SSM mapping function is enabled.
5. (Optional) Run [**igmp ssm-mapping enable policy**](cmdqueryname=igmp+ssm-mapping+enable+policy) *policy-name*
   
   
   
   SSM mapping is enabled, and an SSM mapping policy is configured.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
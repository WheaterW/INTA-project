Enabling SSM Mapping
====================

Enable the Source-Specific Multicast (SSM) mapping function on an interface before you configure MLD SSM mapping. If SSM mapping is not enabled, SSM source/group address mapping entries cannot take effect on the interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mld version**](cmdqueryname=mld+version) **2**
   
   
   
   The MLD version is set to 2. To ensure that all user hosts (running any MLD version) can obtain SSM services, MLDv2 is recommended.
4. Run [**mld ssm-mapping enable**](cmdqueryname=mld+ssm-mapping+enable)
   
   
   
   The SSM mapping function is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
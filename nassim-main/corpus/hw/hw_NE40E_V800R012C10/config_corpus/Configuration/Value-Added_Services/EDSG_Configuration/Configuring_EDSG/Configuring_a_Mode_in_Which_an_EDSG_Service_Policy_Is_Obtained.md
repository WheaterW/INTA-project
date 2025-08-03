Configuring a Mode in Which an EDSG Service Policy Is Obtained
==============================================================

An EDSG service policy can be downloaded from local configurations or a RADIUS server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-policy download**](cmdqueryname=service-policy+download) { **local** | **radius** *server-group* **password cipher** *cipher-password* } \*
   
   
   
   A mode in which an EDSG service policy is obtained is configured.
   
   To configure the BRAS to obtain an EDSG service policy from local configurations, you must have configured an authentication scheme, an accounting scheme, and a RADIUS server group for the EDSG service policy. For configuration details, see [Configuring AAA Schemes](dc_ne_aaa_cfg_0515.html). To configure the BRAS to obtain an EDSG service policy from a RADIUS server, you must have configured the RADIUS server. For configuration details, see [Configuring a Device as a RADIUS Client](dc_ne_aaa_cfg_0600.html).
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
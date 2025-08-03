Enabling Local MT
=================

After local MT is enabled, routers through which a TE tunnel passes can generate multicast forwarding entries.

#### Context

Enable local MT in the IS-IS system view before configuring IS-IS MT. To enable the Router through which an IGP Shortcut-enabled TE tunnel passes to generate multicast forwarding entries, perform the following operations on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**cost-style**](cmdqueryname=cost-style) { **narrow** | **wide** | **wide-compatible** | { **compatible** | **narrow-compatible** } [ **relax-spf-limit** ] }
   
   
   
   The cost style is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   MPLS TE features take effect only when the cost style is **compatible**, **wide**, or **wide-compatible**.
4. Run [**traffic-eng**](cmdqueryname=traffic-eng) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   TE is configured for the process.
5. Run [**local-mt enable**](cmdqueryname=local-mt+enable)
   
   
   
   Local MT is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
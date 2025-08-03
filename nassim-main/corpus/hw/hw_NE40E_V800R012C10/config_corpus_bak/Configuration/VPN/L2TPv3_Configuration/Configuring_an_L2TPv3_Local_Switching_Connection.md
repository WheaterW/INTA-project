Configuring an L2TPv3 Local Switching Connection
================================================

An L2TPv3 local switching connection can be configured
for two CEs connecting to the same PE to exchange packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tpv3 enable**](cmdqueryname=l2tpv3+enable)
   
   
   
   L2TPv3 is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.
4. Run [**l2tpv3 local connection**](cmdqueryname=l2tpv3+local+connection) *connection-name* **interface** { *interface-type* *interface-number* | *interface-name* } **out-interface** { *out-interface-type* *out-interface-number* | *out-interface-name* }
   
   
   
   An L2TPv3 local
   switching connection is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.
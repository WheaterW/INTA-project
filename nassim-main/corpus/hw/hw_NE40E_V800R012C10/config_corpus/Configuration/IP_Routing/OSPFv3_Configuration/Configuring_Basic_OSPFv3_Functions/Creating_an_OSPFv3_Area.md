Creating an OSPFv3 Area
=======================

After an AS is divided into different areas and OSPFv3 interfaces and areas to which these interfaces belong are specified, OSPFv3 can discover and calculate routes in the AS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPFv3 area view is displayed.
   
   The area ID can be a decimal integer or in the IPv4 address format, but it is displayed in the IPv4 address format.
   
   The description of an OSPFv3 area helps identify special processes by the [**description**](cmdqueryname=description) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
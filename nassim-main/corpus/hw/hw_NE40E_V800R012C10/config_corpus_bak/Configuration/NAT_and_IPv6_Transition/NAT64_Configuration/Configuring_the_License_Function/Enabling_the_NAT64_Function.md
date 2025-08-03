Enabling the NAT64 Function
===========================

The NAT64 function must be enabled in the license view before basic NAT64 functions are configured.

#### Context

Before you configure basic NAT64 functions, apply for a NAT64 license for a service board and run the [**active nat64 vsuf**](cmdqueryname=active+nat64+vsuf) command in the license view.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active nat64 vsuf**](cmdqueryname=active+nat64+vsuf) **slot** *slot-id*
   
   
   
   NAT64 is enabled on a specified service board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
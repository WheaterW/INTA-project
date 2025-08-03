Configuring an Overload Bit for an IPv4 IS-IS Device
====================================================

If an IS-IS device needs to be temporarily isolated, configure the overload state for it to prevent other devices from forwarding traffic to this IS-IS device and prevent routing black holes.

#### Context

If an IS-IS device needs to be temporarily isolated, for upgrade or maintenance purposes for example, configure the overload state for it so that no other devices will forward traffic to this IS-IS device.

IS-IS routes converge more quickly than BGP routes do. To prevent routing black holes on a network where both IS-IS and BGP are configured, set an overload bit to instruct an IS-IS device to enter the overload state during its start or restart. After BGP convergence is complete, cancel the overload bit.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**set-overload**](cmdqueryname=set-overload) { **on-startup** [ *timeout1* | **start-from-nbr** *system-id* [ *timeout1* [ *timeout2* ] ] | **wait-for-bgp** [ *timeout1* ] ] [ **route-delay-distribute** *timeout4* ] [ **send-sa-bit** [ *timeout3* ] ] [ **route-max-metric** ] } [ **allow** { **interlevel** | **external** } \* ]
   
   
   
   The overload bit is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
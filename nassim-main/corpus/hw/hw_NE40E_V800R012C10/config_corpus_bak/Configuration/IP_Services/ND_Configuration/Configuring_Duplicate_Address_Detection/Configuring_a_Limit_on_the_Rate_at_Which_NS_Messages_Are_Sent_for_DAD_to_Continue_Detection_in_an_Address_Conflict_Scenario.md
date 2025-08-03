Configuring a Limit on the Rate at Which NS Messages Are Sent for DAD to Continue Detection in an Address Conflict Scenario
===========================================================================================================================

Configuring_a_Limit_on_the_Rate_at_Which_NS_Messages_Are_Sent_for_DAD_to_Continue_Detection_in_an_Address_Conflict_Scenario

#### Context

When DAD detects an address conflict on an interface, the IPv6 protocol status of the interface becomes down. The interface can go up only after being manually shut down and then restarted. To address this issue, deploy address conflict self-recovery. After detecting an IPv6 address conflict, DAD continues detection until the conflict is removed and the IPv6 protocol status of the interface becomes up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd dad detect rate-limit**](cmdqueryname=ipv6+nd+dad+detect+rate-limit) *rate-value*
   
   
   
   A limit on the rate at which NS messages are sent for DAD to continue detection in an address conflict self-recovery scenario is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
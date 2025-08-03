Configuring a Threshold for DAD to Consider an Address Available in an Address Conflict Self-Recovery Scenario
==============================================================================================================

Configuring_a_Threshold_for_DAD_to_Consider_an_Address_Available_in_an_Address_Conflict_Self-Recovery_Scenario

#### Context

If an address conflict occurs on an interface in an address conflict self-recovery scenario, DAD continues detection on the interface until the address conflict is removed. The device considers the address conflict removed when DAD does not receive conflict packets for a specified number of consecutive times. This number, referred to as the address conflict removal threshold, can be configured using the [**ipv6 nd dad detect attempts**](cmdqueryname=ipv6+nd+dad+detect+attempts) command. In this case, DAD considers the address available. Otherwise, DAD considers the address unavailable and continues detection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd dad detect attempts**](cmdqueryname=ipv6+nd+dad+detect+attempts) *attempts-value*
   
   
   
   A threshold is configured for DAD to consider an address available in an address conflict self-recovery scenario.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
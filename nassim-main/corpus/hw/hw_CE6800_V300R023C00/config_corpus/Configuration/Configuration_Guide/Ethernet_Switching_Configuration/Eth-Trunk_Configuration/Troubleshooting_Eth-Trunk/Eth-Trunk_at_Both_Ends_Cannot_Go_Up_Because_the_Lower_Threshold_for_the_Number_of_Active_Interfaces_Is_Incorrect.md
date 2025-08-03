Eth-Trunk at Both Ends Cannot Go Up Because the Lower Threshold for the Number of Active Interfaces Is Incorrect
================================================================================================================

Eth-Trunk at Both Ends Cannot Go Up Because the Lower Threshold for the Number of Active Interfaces Is Incorrect

#### Fault Symptom

The Eth-Trunk is down because the lower threshold for the number of active interfaces is incorrect.


#### Procedure

1. Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) *trunk-id* command to check whether the lower threshold for the number of active interfaces of an Eth-Trunk interface is set.
   
   If the number of Eth-Trunk member interfaces in up state is lower than the lower threshold, the Eth-Trunk goes down.
2. Run the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command to configure the lower threshold for the number of active interfaces of an Eth-Trunk interface to be smaller than the number of Eth-Trunk member interfaces in up state.
   
   The local and peer devices can be configured with different lower thresholds for the number of active interfaces. If the lower thresholds are different, the larger value takes effect.
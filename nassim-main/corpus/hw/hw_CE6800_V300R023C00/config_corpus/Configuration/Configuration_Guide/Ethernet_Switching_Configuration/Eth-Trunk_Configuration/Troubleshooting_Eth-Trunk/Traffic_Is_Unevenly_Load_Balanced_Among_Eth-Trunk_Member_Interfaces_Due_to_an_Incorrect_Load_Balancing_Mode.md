Traffic Is Unevenly Load Balanced Among Eth-Trunk Member Interfaces Due to an Incorrect Load Balancing Mode
===========================================================================================================

![](public_sys-resources/note_3.0-en-us.png) 

Only the CE6881H, CE6881H-K, CE6863H, CE6863H-K, CE6820H, CE6820H-K, and CE6820S support this configuration.


#### Fault Symptom

Traffic is unevenly load balanced among Eth-Trunk member interfaces due to the incorrect load balancing mode.


#### Procedure

1. Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command to check whether the load balancing mode of the Eth-Trunk interface meets networking requirements. For example, source or destination IP address-based load balancing is not recommended in Layer 2 networking.
2. Run the [**load-balance**](cmdqueryname=load-balance) command in the Eth-Trunk interface view to configure an appropriate load balancing mode based on the actual traffic.
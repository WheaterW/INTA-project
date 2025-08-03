(Optional) Configuring Load Balancing of Downstream Traffic on Eth-Trunk Interfaces
===================================================================================

(Optional)_Configuring_Load_Balancing_of_Downstream_Traffic_on_Eth-Trunk_Interfaces

#### Context

Load balancing can be enabled for downstream traffic of users on Eth-Trunk interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**trunk downstream load-balance enable**](cmdqueryname=trunk+downstream+load-balance+enable)
   
   
   
   Load balancing of downstream traffic is enabled on user-side Eth-Trunk interfaces.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
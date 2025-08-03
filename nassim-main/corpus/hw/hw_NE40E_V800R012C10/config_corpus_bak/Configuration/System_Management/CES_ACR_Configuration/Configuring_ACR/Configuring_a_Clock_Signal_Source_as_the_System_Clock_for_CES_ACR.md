Configuring a Clock Signal Source as the System Clock for CES ACR
=================================================================

Configuring_a_Clock_Signal_Source_as_the_System_Clock_for_CES_ACR

#### Procedure

1. Configure the attributes of a clock source in the recovery domain.
   
   
   
   Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-id* **recovery-domain** *domain-value* **ssm** { **prc** | **ssua** | **ssub** | **sec** | **dnu** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the CES ACR clock source.
   
   
   
   Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-id* **recovery-domain** *domain-value* **clock-id** *clock-id* command to configure a clock ID for the CES ACR clock source.
   
   
   
   Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-id* **recovery-domain** *domain-value* **priority** *priority-value* command to configure a priority for the CES ACR clock source.
2. Enable clock synchronization for the clock source in the clock recovery domain.
   
   
   
   Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-number* **recovery-domain** *domain-value* **synchronization** **enable** command to enable clock synchronization for the clock source in the clock recovery domain.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
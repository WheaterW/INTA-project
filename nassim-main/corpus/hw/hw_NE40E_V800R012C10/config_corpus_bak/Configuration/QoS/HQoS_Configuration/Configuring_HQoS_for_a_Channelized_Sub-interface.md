Configuring HQoS for a Channelized Sub-interface
================================================

After HQoS is configured for channelized sub-interfaces, each one performs independent HQoS scheduling, thereby isolating different types of services.

#### Context

To prevent services from affecting each other, a mechanism to isolate different types of services is needed. Different service flows are forwarded through VLAN channelized sub-interfaces with different encapsulation modes, and each channelized sub-interface implements independent HQoS scheduling to isolate services of different types.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mode channel network-header-length**](cmdqueryname=mode+channel+network-header-length) [ *network-header-length-value* ] **adjustment** **enable**
   
   
   
   A network header length is configured for channelized sub-interfaces.
   
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   A network header length can be configured only on Eth-Trunk and GE main interfaces that support channelized sub-interfaces.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The channelized sub-interface view is displayed.
   
   
   
   For details about how to configure a channelized sub-interface, see "[Configuring a Channelized Sub-interface](../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_7011_01.html)" in *Interface and Data Link* > *Interface Management Configuration* > *Logical Interface Configuration*.
6. Run [**qos default flow-queue**](cmdqueryname=qos+default+flow-queue) *flow-queue-template-name* **outbound**
   
   
   
   An FQ profile is applied to the channelized sub-interface.
   
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Only one FQ profile can be applied to a channelized sub-interface.
   
   For details about how to configure an FQ profile, see [(Optional) Configuring an FQ Profile in Common 8-CoS Mode](../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5043_a.html).
7. Run **[**qos default service-template**](cmdqueryname=qos+default+service-template)** **service-template-name** ****outbound****
   
   
   
   A service profile is applied to the channelized sub-interface.
   
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the **qos default service-template** command is run in the channelized sub-interface view (to apply a service profile configured with a network header length) and the **[**mode channel network-header-length adjustment enable**](cmdqueryname=mode+channel+network-header-length+adjustment+enable)** command is run in the main interface view (to enable network header length adjustment for the channelized sub-interface and configure a network header length), the network header length configured in the service profile takes precedence over that configured in the **[**mode channel network-header-length adjustment enable**](cmdqueryname=mode+channel+network-header-length+adjustment+enable)** command.
   
   For details about how to configure a service profile, see [(Optional) Configuring a Service Profile](../software/nev8r10_vrpv8r16/user/ne/dc_ne_hqos_cfg_5043_5.html).
8. (Optional) Run [**mode channel bandwidth maximize**](cmdqueryname=mode+channel+bandwidth+maximize)
   
   
   
   The bandwidth extension mode is enabled for the channelized sub-interface.
   
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be configured only on an Eth-Trunk channelized sub-interface.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
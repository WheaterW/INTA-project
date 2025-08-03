Disabling the Optical Module Alarm Function
===========================================

You can disable the alarm function for an optical module to prevent the optical module from reporting alarms when its optical power exceeds the threshold.

#### Context

The system automatically obtains the vendor-defined power threshold of an optical module and compares it with the actual power. If the actual power exceeds the vendor-defined threshold, an alarm will be generated. Generally, the actual power is greater than the vendor-defined threshold, which means frequent alarm reporting. It is unfeasible to install an attenuator on each optical module to prevent frequent reporting of such power alarms. You can disable the alarm function for the optical module by executing the following command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The device has two types of optical module power alarms: warning and alarm. A warning is reported when the difference between the actual power and vendor-defined threshold is not great. It can also be considered as a precaution. Some optical modules can continue working properly when the actual optical power is at the warning level. You can disable the alarm function for these optical modules to prevent these optical modules from frequently reporting warnings by executing the following command.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**port-alarm disable optical-module**](cmdqueryname=port-alarm+disable+optical-module) { **rx-power-high-warning** | **rx-power-low-warning** | **tx-power-high-warning** | **tx-power-low-warning** | **voltage-high-warning** | **voltage-low-warning** } \*
   
   
   
   The alarm function is disabled for the optical module.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
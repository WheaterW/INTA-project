Managing Non-Huawei-Certified Optical Modules
=============================================

To manage non-Huawei-certified optical modules, you can suppress the alarms for non-Huawei-certified optical modules and enable the function of setting interfaces with the optical modules inserted to Down.

#### Context

When an interface is inserted with a non-Huawei-certified optical module, the system automatically reports an alarm. If you want to suppress the alarm, you can disable the function of reporting the alarm for the non-Huawei-certified optical module. If you do not want to use the interface with the optical module inserted, you can enable the function of setting the interface to Down.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**transceiver non-certified-alarm disable**](cmdqueryname=transceiver+non-certified-alarm+disable)
   
   
   
   The function of reporting an alarm for a non-Huawei-certified optical module is disabled.
3. Run [**transceiver non-certified-alarm port-down enable**](cmdqueryname=transceiver+non-certified-alarm+port-down+enable)
   
   
   
   The function of setting an interface with a non-Huawei-certified optical module inserted to Down is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
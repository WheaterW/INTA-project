Enabling the Optical Module Alarm Threshold Standardization Function
====================================================================

You can enable the alarm standardization function for an optical module to prevent the optical module from reporting alarms when its optical power exceeds the threshold.

#### Context

The system automatically obtains the vendor-defined power threshold of an optical module and compares it with the actual power. If the actual power exceeds the vendor-defined threshold, an alarm will be generated. However, the vendor-defined power threshold of an optical module may not meet user requirements. If the alarm standardization function is enabled, a unified power threshold is used, and the threshold is calculated based on the optical module transmission distance and bandwidth.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The device has two types of optical module power alarms: warning and alarm. A warning is reported when the difference between the actual power and vendor-defined threshold is not great. It can also be considered as a precaution. Some optical modules can continue working properly when the actual optical power is at the warning level. You can disable warning detection as required.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**optical-module alarm-threshold standardization enable**](cmdqueryname=optical-module+alarm-threshold+standardization+enable)
   
   
   
   The alarm threshold standardization function is enabled for the optical module.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
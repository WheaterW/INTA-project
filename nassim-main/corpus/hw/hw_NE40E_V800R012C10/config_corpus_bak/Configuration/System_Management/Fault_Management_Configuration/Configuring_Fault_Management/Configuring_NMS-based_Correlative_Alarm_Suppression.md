Configuring NMS-based Correlative Alarm Suppression
===================================================

This section describes how to configure NMS-based correlative alarm suppression. This function enables the system to mask NMS-based correlative alarms and only reports root alarms to an NMS.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**correlation-analyze enable**](cmdqueryname=correlation-analyze+enable) command to enable the alarm correlation analysis function.
   
   
   
   This function must be enabled before you configure correlative alarm suppression.
4. Run the [**alarm correlation-suppress enable target-host**](cmdqueryname=alarm+correlation-suppress+enable+target-host) *ip-address* **securityname** **security-name**[ **vpn-instance** *vpn-instance-name* ] command to enable NMS-based correlative alarm suppression.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
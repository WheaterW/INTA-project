(Optional) Configuring the IP Packet Check Alarm Function
=========================================================

(Optional) Configuring the IP Packet Check Alarm Function

#### Context

After the IP packet check alarm function is configured, the device generates logs when IP packets are discarded. If the number of discarded packets reaches the threshold, the device will send alarms to the NMS.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the IP packet check alarm function.
   
   
   * Enable the IP packet check alarm function in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [ip source check user-bind alarm enable](cmdqueryname=ip+source+check+user-bind+alarm+enable)
     [quit](cmdqueryname=quit)
     ```
   * Enable the IP packet check alarm function in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [ip source check user-bind alarm enable](cmdqueryname=ip+source+check+user-bind+alarm+enable)
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, the IP packet check alarm function is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support **ip source check user-bind alarm enable**.
3. Configure the threshold of the IP packet check alarm.
   
   
   * Configure the threshold of the IP packet check alarm in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [ip source check user-bind alarm threshold](cmdqueryname=ip+source+check+user-bind+alarm+threshold) threshold
     [quit](cmdqueryname=quit)
     ```
   * Configure the threshold of the IP packet check alarm in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [ip source check user-bind alarm threshold](cmdqueryname=ip+source+check+user-bind+alarm+threshold) threshold
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, the alarm threshold is 100.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support **ip source check user-bind alarm threshold**.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
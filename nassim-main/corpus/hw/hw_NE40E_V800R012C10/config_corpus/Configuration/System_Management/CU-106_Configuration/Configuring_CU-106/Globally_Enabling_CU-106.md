Globally Enabling CU-106
========================

To ensure CU-106 for time synchronization, enable CU-106 globally in the system view and configure basic information on a device, such as the device type (T-BC or T-TC) and domain value.

#### Context

Perform the following steps on the T-BC and T-TC:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the device.
3. Run [**ptp profile cu-106 enable**](cmdqueryname=ptp+profile+cu-106+enable)
   
   
   
   CU-106 is enabled on the device.
4. Run [**ptp device-type**](cmdqueryname=ptp+device-type) { **t-bc** | **t-tc** }
   
   
   
   The device type is set to T-BC or T-TC.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to set the device type to T-BC. A T-BC can implement time synchronization and then transmit the time to the next hop. Setting the device type to T-TC is not recommended because a T-TC cannot synchronize time and can only correct the forwarding time to the next hop.
5. Run [**ptp domain**](cmdqueryname=ptp+domain) *domain-value*
   
   
   
   The domain where the device resides is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   All the T-BCs that use CU-106 to perform time synchronization must reside in the same clock domain.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
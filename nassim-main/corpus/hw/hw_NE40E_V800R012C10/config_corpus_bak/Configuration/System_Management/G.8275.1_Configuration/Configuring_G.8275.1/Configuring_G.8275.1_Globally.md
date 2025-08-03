Configuring G.8275.1 Globally
=============================

To ensure G.8275.1 for time synchronization, you need to globally enable G.8275.1 in the system view, set the device type to T-BC/T-TC, and configure basic information such as the domain value.

#### Context

Perform the following steps on each T-BC/T-TC:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the device.
3. Run the [**ptp profile g-8275-1 enable**](cmdqueryname=ptp+profile+g-8275-1+enable) command to enable G.8275.1 on the device.
4. Run the [**ptp device-type**](cmdqueryname=ptp+device-type) { **t-bc** | **t-tc** } command to set the device type to T-BC or T-TC.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to set the device type to T-BC. A T-BC can implement time synchronization and then transmit the time to the next hop. Setting the device type to T-TC is not recommended because a T-TC cannot synchronize time and can only correct the forwarding time to the next hop.
5. Run the [**ptp domain**](cmdqueryname=ptp+domain) *domain-value* command to configure the clock domain where the device resides.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When G.8275.1 is used to perform time synchronization, T-BCs and T-TCs must reside in the same clock domain.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
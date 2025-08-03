Configuring a Monitor Link Group
================================

Configuring a Monitor Link Group

#### Context

The specified interface can be added to only one Monitor Link group.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a Monitor Link group.
   
   
   ```
   [monitor-link group](cmdqueryname=monitor-link+group) group-id
   ```
3. Configure uplink and downlink interfaces for the Monitor Link group.
   * Configure a specified interface as the uplink or downlink interface for the Monitor Link group.
     ```
     port {interface-type interface-number | interface-name }{ downlink [ downlink-id ] | uplink }
     ```
     
     Configure the uplink interface first. This is necessary because the downlink interface will enter the Down state if it is configured first and no uplink interface exists.
4. (Optional) Configure a WTR time.
   
   
   ```
   [timer recover-time](cmdqueryname=timer+recover-time) recover-time
   ```
   
   
   
   By default, the switchback function of a Monitor Link group is enabled, with a default WTR time of 3s.
5. (Optional) Configure an interval at which downlink interfaces in the Monitor Link group go up one by one.
   
   
   ```
   [downlink recover interval](cmdqueryname=downlink+recover+interval) interval-value
   ```
   
   By default, the interval is 0s. That is, all downlink interfaces in a Monitor Link group are enabled at the same time.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **display monitor-link group** { **all** | *group-id* } command to check the basic Monitor Link group configuration.


#### Follow-up Procedure

* To restore a downlink interface from the Error-Down state to the Up state, rectify the fault of the uplink interface. After the uplink interface goes up and the WTR time expires, the downlink interface is restored to the Up state.
* To temporarily change the uplink status without affecting the downlink interface status, run the [**monitor-link disable**](cmdqueryname=monitor-link+disable) command to disable the Monitor Link function.
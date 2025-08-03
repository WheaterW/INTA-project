Disabling the Function of Generating Alarms for Non-Huawei-Certified Optical Modules
====================================================================================

Disabling the Function of Generating Alarms for Non-Huawei-Certified Optical Modules

#### Context

If non-Huawei-certified optical modules are used on a device, to facilitate optical module management and maintenance, the device will generate a large number of alarms to prompt users to replace these optical modules with Huawei-certified ones. To shield these alarms, disable the function of generating alarms for non-Huawei-certified optical modules.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the function of generating alarms for non-Huawei-certified optical modules.
   
   
   ```
   [transceiver non-certified-alarm disable](cmdqueryname=transceiver+non-certified-alarm+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* *interface-number* | **slot** *slot-id* ] **transceiver** [ **verbose** ] command to check optical module information on a device port. If the **Non-Huawei-certified transceiver** field is not displayed under **Alarm information**, the function of generating alarms for non-Huawei-certified optical modules is successfully disabled.
* Run the [**display interface**](cmdqueryname=display+interface) **transceiver** **non-certified** [ **verbose** ] command to check information about non-Huawei-certified optical modules. If the **Non-Huawei-certified transceiver** field is not displayed under **Alarm information**, the function of generating alarms for non-Huawei-certified optical modules is successfully disabled.
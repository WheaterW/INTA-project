DLDP Cannot Discover a Directly Connected Neighbor
==================================================

DLDP Cannot Discover a Directly Connected Neighbor

#### Possible Causes

1. A link fault occurs.
2. DLDP is not enabled on the remote device.
3. DLDP parameters on the local and remote devices are different.

#### Procedure

1. Check the **current state** field to verify whether the interface of the neighbor is working normally.
   
   
   ```
   [display interface](cmdqueryname=display+interface) interface-type interface-name
   ```
   * If the interface is down, rectify the interface fault.
   * If the interface is up, go to Step 2.
2. Check whether DLDP is enabled globally.
   
   
   ```
   [display dldp](cmdqueryname=display+dldp)
   ```
   * If the command output does not contain the **DLDP enable** field, run the [**dldp enable**](cmdqueryname=dldp+enable) command in the system view to enable DLDP.
   * If the **DLDP enable** field is displayed in the command output, DLDP is enabled globally. Go to Step 3.
3. Check whether DLDP is enabled on the interface.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   * If the command output does not contain the **DLDP enable** field, run the [**dldp enable**](cmdqueryname=dldp+enable) command in the interface view to enable DLDP.
   * If the **DLDP enable** field is displayed in the command output, DLDP is enabled on the interface. Go to Step 4.
4. Check whether the parameter settings on the local and remote devices are the same.
   
   
   ```
   [display dldp](cmdqueryname=display+dldp)
   ```
   
   
   * Check the **DLDP interval** field. If different intervals for sending DLDPDUs are configured for the two devices, run the [**dldp interval**](cmdqueryname=dldp+interval) *interval* command in the system view to change the interval on one end so that the intervals on both ends are the same.
   * Check the **DLDP authentication-mode** field. If different authentication modes or passwords are configured for the two devices, run the [**dldp authentication-mode**](cmdqueryname=dldp+authentication-mode) { **md5****md5-password** | **sha****sha-password** | **simple** **simple-password**| **none** } command in the system view to configure the same authentication mode for the two devices.
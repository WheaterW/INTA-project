Setting the System Master Key
=============================

You can set the system master key to improve data security and reliability.

#### Context

In real-world situations, networks and devices are provided and maintained by network providers, while data is owned by tenants. To ensure secure data transmission and storage on a network, you must fully control the key, preventing the key from being leaked to the network provider or other tenants.

To achieve this, you can manually change the system master key to enhance data security and reliability.


#### Procedure

1. Run the [**set master-key**](cmdqueryname=set+master-key) command in the user view to set the system master key.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To clear historical system master keys, run the [**clear master-key**](cmdqueryname=clear+master-key) command.
   
   
   When changing the system master key, note the following points:
   * After the new master key is entered, enter **Y** on the terminal interface to proceed to the next operation. If you enter **N**, the system exits the master key change process.
   * Enter the new master key twice. The system proceeds to the next operation only when the two inputs are the same.
   
   If an error occurs during the master key change, the system prompts a message indicating a master key change failure and advising you to try again. If the failure persists, contact technical support.
   
   After the master key is changed, the configuration file of the device cannot be shared to other devices. After a configuration file is copied from another device to the local device for next startup, if the master key on that remote device is not the default one and does not exist on the local device, the configuration fails. To resolve this issue, use one of the following methods:
   * Change the master key on the local device to be the same as that on the remote device.
   * Change the master key on the remote device to be the same as that on the local device. Then, save and export the configuration file, upload it to the local device, and specify the configuration file for next startup.
   * Specify the master key on the remote device as the default one. Then, save and export the configuration file, upload it to the local device, and specify the configuration file for next startup.
   After the master key is changed and an encrypted file is copied from another device to the local device for next startup, if the master key on that remote device is not the default one and does not exist on the local device, the local device cannot decrypt the copied file due to master key mismatch. To resolve this issue, use one of the following methods:
   * Change the master key on the local device to be the same as that on the remote device.
   * Change the master key on the remote device to be the same as that on the local device. Then, export the encrypted file and upload it to the local device for decryption.
   * Specify the master key on the remote device as the default one. Then, export the encrypted file and upload it to the local device for decryption.
2. (Optional) Run the [**set master-key auto-update**](cmdqueryname=set+master-key+auto-update) **interval** *interval-time* command in the system view to enable automatic update of the system master key at a specified interval.
   
   
   
   The system master key can be the default or a manually configured one.
   
   Using the default master key for an extended period poses a risk of theft and cracking. Periodically change and maintain a manually configured master key.
   
   To reduce manual maintenance workload, run the [**set master-key auto-update**](cmdqueryname=set+master-key+auto-update) **interval** *interval-time* command to enable automatic update of the master key. The system then periodically generates a new master key composed of 32 characters.
   
   To disable the automatic update function, run the [**undo set master-key auto-update**](cmdqueryname=undo+set+master-key+auto-update) [ **interval** *interval-time* ] command. After the automatic update function is disabled, the system retains the last automatically generated master key and does not automatically update it any more.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In scenarios where automatic update of the master key is enabled, if you run the [**set master-key**](cmdqueryname=set+master-key) command to manually set the master key, the system displays a message indicating that this operation will disable the automatic update function.

#### Verifying the Configuration

After the configuration is complete, you can run the following commands to check the configuration.

* Run the [**display master-key configuration**](cmdqueryname=display+master-key+configuration) command to check the configuration of the system master key.
  
  In VS mode, this command is supported only by the admin VS.
* Run the [**display master-key version**](cmdqueryname=display+master-key+version) command to check the KMC version information of all boards on the device.
  
  In VS mode, this command is supported only by the admin VS.
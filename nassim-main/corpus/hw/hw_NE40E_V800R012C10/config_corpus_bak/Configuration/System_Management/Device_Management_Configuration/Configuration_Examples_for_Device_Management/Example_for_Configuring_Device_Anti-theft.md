Example for Configuring Device Anti-theft
=========================================

When a device cannot connect to the NMS, you can configure the device in offline mode, including enabling the anti-theft function and temporarily authorizing the device to unlock it.

#### Networking Requirements

The license for the anti-theft function has been loaded to the device. A public key and private key have been generated on the NMS. The public key has been delivered to the device. The device cannot connect to the NMS for anti-theft enabling or unlocking.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the device anti-theft function.
2. Install the temporary authorization file for device anti-theft.

#### Data Preparation

To complete the configuration, you need the following data:

* Public key file for enabling device anti-theft
* Temporary authorization file for device anti-theft

#### Procedure

1. Enable the device anti-theft function.
   
   
   ```
   <HUAWEI> anti-theft install enable file DevlockFile.dat
   Warning: This operation enables the anti-theft function. Are you sure you want to continue? [Y/N]:Y
   Please wait...............................................................
   Info: The task end success.
   ```
   
   **DevlockFile.dat** is the name of the public key file for enabling anti-theft.
2. Install the temporary authorization file for device anti-theft.
   
   
   ```
   <HUAWEI> anti-theft install authorization file temp-authorization-file.dat
   Warning: This operation authorizes the anti-theft function on the device. Are you sure you want to continue? [Y/N]:Y
   ```
   
   **temp-authorization-file.dat** is the name of the temporary authorization file for anti-theft.
3. Verify the configuration.
   
   
   
   Run the following command to check whether the anti-theft configuration takes effect, including the device anti-theft status (temporarily-authorized), authorization time, remaining authorization time, grace time, remaining grace time, and operator name.
   
   ```
   <HUAWEI> display anti-theft status
   Status:                         temporarily-authorized
   Authorization time:             50h
   Remaining authorization time:   3d 10h 25m
   Grace time:                     7d
   Remaining grace time:           5d 12h 45m
   Operator name:                  TEST
   ```

#### Configuration Files

None
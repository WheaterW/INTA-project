Reusing the Configuration File of Another Device
================================================

Reusing the Configuration File of Another Device

#### Context

A configuration file may contain a ciphertext encrypted using a system master key. As a system master key is randomly generated if the system master key is set to an automatically generated master key, different devices have different system master keys. In this case, the ciphertext in a configuration file of a device cannot be decrypted on another device. As a result, the ciphertext cannot be restored on another device and will be used as a plaintext. To decrypt the ciphertext in the configuration file on another device, perform the following operations.


#### Procedure

1. Export the configuration file from device A.
   1. Save the configuration file.
      
      
      ```
      [save](cmdqueryname=save) shareable-configuration configuration-file [ password ]
      ```
   2. Export the configuration file.
      
      
      
      For details, see [Backing Up the Configuration File to an SFTP Server or Client](vrp_cfgfile_cfg_0013.html).
2. On device B, reuse the configuration file exported from device A.
   1. Copy the configuration file of device A to device B.
      
      
      
      For details, see [Copying the Configuration File from an SFTP Server or Client to the Device](vrp_cfgfile_cfg_0018.html).
   2. Configure the exported configuration file as the configuration file to be loaded for the next startup of device B.
      
      
      ```
      [startup](cmdqueryname=startup) shareable-configuration configuration-file [ password ]
      ```

#### Verifying the Configuration

* Run the **display configuration recover-result** command to check the configuration restoration result after the restart and the failure cause.
* Run the **display master-key configuration** command to check whether the system master key is the configured one.
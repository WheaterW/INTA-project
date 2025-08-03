Creating an Application
=======================

Creating an Application

#### Context

Before creating an application, you need to create a root directory partition for storing application running information.

The device provides two methods for configuring applications:

* Specify the default configuration file when creating an application.
  
  In this mode, you need to prepare the configuration file and its signature file in advance and upload them to the device. Install the public key corresponding to the signature. For details about how to upload a file, see "File System Management Configuration" in *Configuration Guide* > *Basic Configuration*.
* Do not specify the default configuration file when creating an application. After the application is created, you can run commands to configure the application.

#### Procedure

1. Create the root directory partition for running applications.
   
   
   ```
   [create virtual-partition](cmdqueryname=create+virtual-partition) size partition-size type rootfs slot slot-id
   ```
2. Create an application.
   
   
   ```
   [application](cmdqueryname=application) application-name [ config-file config-file-name ]
   ```
   
   You can specify the **config-file** parameter to configure the application using the configuration file. In this configuration mode, you need to upload the public key file corresponding to the signature of the configuration file to **flash:/oas/images**, and then run the [**install public-key**](cmdqueryname=install+public-key) *public-key-name* **fingerprint** *fingerprint-key* command to install the public key. For details about the format and requirements of the configuration file, see [Container Configuration File](vrp_OAS_cfg_0025.html).
3. Configure the application.
   
   
   
   If no configuration file is specified or the parameters in the configuration file need to be adjusted, you can run commands to configure the parameters before starting the application.
   
   
   
   1. Configure the image software package of the application.
      ```
      [software](cmdqueryname=software) software-name
      ```
      
      If no configuration file is specified or no image software package is specified in the configuration file, you must run this command. Otherwise, the application fails to be started.
      
      After running this command, run the **commit** command to commit the configuration. Otherwise, the subsequent configuration of the running options of the application will fail.
   2. Configure the running options of the application.
      ```
      [run-options](cmdqueryname=run-options) options
      ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the application is started, you can also run the preceding two commands to adjust the configuration. However, the configuration takes effect only after the application is restarted.
4. Create an application instance and start it.
   
   
   ```
   [start](cmdqueryname=start) position { slot slot-id | type board-type }
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display oas application**](cmdqueryname=display+oas+application) [ **verbose** ] command to view information about installed applications.
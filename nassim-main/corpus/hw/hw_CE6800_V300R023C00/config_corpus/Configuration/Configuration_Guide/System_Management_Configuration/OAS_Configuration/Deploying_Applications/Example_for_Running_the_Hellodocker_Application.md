Example for Running the Hellodocker Application
===============================================

Example for Running the Hellodocker Application

#### Networking Requirements

The image software package **hellodocker.zip** is installed on the device, an application is created, and the application is configured using commands.

#### Precautions

* Log in to the Huawei technical support website, search for the corresponding product and version in the software download area, and download the OAS feature package.
* Follow steps in [Creating an Image Software Package](vrp_OAS_cfg_0005.html) to create the image software package **hellodocker.zip** and public key file **public-key.txt**.


#### Procedure

1. Upload the OAS feature package to the device. The SFTP mode is used as an example. For details, see "Using SFTP to Operate Files" in *Configuration Guide* > *Basic Configuration*.
2. Install the OAS feature package.
   
   
   ```
   <HUAWEI> install feature-software Product_Version_OAS_FeatureVersion.ccx
   Info: Checking, please wait for a moment...done.
   Info: Start to install the package Product_Version_OAS_FeatureVersion.ccx.
   Info: Operating, please wait for a moment....done.
   Info: Succeeded in installing the software.
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The name of the OAS feature package is only an example. Change it based on the site requirements.
3. Enter the OAS view.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] oas enable
   [*HUAWEI] commit
   [~HUAWEI] oas
   ```
4. Create a virtual partition for the image.
   
   
   ```
   [~HUAWEI-oas] create virtual-partition size 100 type image
   Warning: The virtual partition will be created. Continue? [Y/N]:y
   Info: Operating, please wait for a moment.......done.
   Info: The virtual partition is created successfully.
   ```
5. Upload the image software package **hellodocker.zip** and public key file **public-key.txt** to the **flash:/oas/images** folder on the device. The SFTP mode is used as an example. For details, see "Using SFTP to Operate Files" in *Configuration Guide* > *Basic Configuration*.
6. Install the public key file **public-key.txt**.
   
   
   ```
   [~HUAWEI-oas] install public-key public-key.txt fingerprint 30675D557CC7D5C7B669781BED95712FF104F735
   Info: Operating, please wait for a moment......done.
   Info: The public key is installed successfully.
   ```
7. Install the image software package **hellodocker.zip**.
   
   
   ```
   [~HUAWEI-oas] install application-software hellodocker.zip
   Info: Operating, please wait for a moment...........done.
   Info: The application software package is successfully installed.
   ```
8. Create the root directory partition for running applications.
   
   
   ```
   [~HUAWEI-oas] create virtual-partition size 100 type rootfs slot 1
   Warning: The virtual partition will be created. Continue? [Y/N]:y
   Info: Operating, please wait for a moment........done.
   Info: The virtual partition is created successfully.
   ```
9. Create a network resource pool.
   
   
   ```
   [~HUAWEI-oas]ipv4 source address 10.0.0.1
   [*HUAWEI-oas]ipv4 source address 10.0.0.2
   [*HUAWEI-oas]ipv4 management-interface address 10.0.0.3 16
   [*HUAWEI-oas]ip dynamic-port 50020 to 50030
   [*HUAWEI-oas] commit
   ```
10. Create applications.
    
    
    
    # Create app1.
    
    
    
    ```
    [~HUAWEI-oas] application app1
    [*HUAWEI-oas-app1] commit
    ```
    
    
    
    # Create app2.
    
    
    
    ```
    [~HUAWEI-oas] application app2
    [*HUAWEI-oas-app2] commit
    ```
11. Configure the image software package and running options of the applications.
    
    
    
    # Configure app1.
    
    ```
    [~HUAWEI-oas-app1] software hellodocker.zip
    [*HUAWEI-oas-app1] commit
    [*HUAWEI-oas-app1] run-options "--blkio-weight 16"
    ```
    
    # Configure app2.
    
    ```
    [~HUAWEI-oas-app2] software hellodocker.zip
    [*HUAWEI-oas-app2] commit
    [*HUAWEI-oas-app2] run-options "--blkio-weight 16"
    ```
12. Configure the communication network parameters of the applications.
    
    
    
    # Configure app1.
    
    
    
    ```
    [*HUAWEI-oas-app1] run-options "--business-ip 10.0.0.1"
    [*HUAWEI-oas-app1] run-options "--manage-ip 10.0.0.3"
    [*HUAWEI-oas-app1] run-options "--port-range 50020-50030"
    [*HUAWEI-oas-app1] commit
    ```
    
    # Configure app2.
    
    ```
    [*HUAWEI-oas-app2] run-options "--business-ip 10.0.0.2"
    [*HUAWEI-oas-app2] run-options "--port-range 50020-50030"
    [*HUAWEI-oas-app2] commit
    ```
13. Start the applications.
    
    
    
    # Start app1.
    
    
    
    ```
    [~HUAWEI-oas-app1] start position slot 1
    [*HUAWEI-oas-app1] commit
    ```
    
    # Start app2.
    
    ```
    [~HUAWEI-oas-app2] start position slot 1
    [*HUAWEI-oas-app2] commit
    ```

#### Verifying the Configuration

# After the preceding configuration is complete, run the following command to check the application configuration.

```
[~HUAWEI-oas] display oas application verbose
Application information:
--------------------------------------------------------------------------------
Application Name        : app1
Slot ID                 : 1
Software Name           : hellodocker.zip
Running State           : running
CPU ID                  : 0
Container ID            : 513c6e356c66
Container PIDS          : 2
Runtime Options         : --restart on-failure:5 --blkio-weight 16 --business-ip 10.0.0.1 --manage-ip 10.0.0.3 --port-range 50020-50030
Memory Usage / Limits   : 1.457MiB / 15.43GiB
Memory Using Percentage : 0.01%
CPU Using Percentage    : 2.80%
Net I/O                 : 0B / 0B
Block I/O               : 4.3MB / 0B

Application Name        : app2
Slot ID                 : 1
Software Name           : hellodocker.zip
Running State           : running
CPU ID                  : 0
Container ID            : 513c6e356c77
Container PIDS          : 2
Runtime Options         : --restart on-failure:5 --blkio-weight 16 --business-ip 10.0.0.2 --port-range 50020-50030
Memory Usage / Limits   : 1.457MiB / 15.43GiB
Memory Using Percentage : 0.01%
CPU Using Percentage    : 2.80%
Net I/O                 : 0B / 0B
Block I/O               : 4.3MB / 0B
--------------------------------------------------------------------------------
```

#### Configuration Scripts

```
#
sysname HUAWEI
#
oas enable
oas
 ipv4 source address 10.0.0.1
 ipv4 source address 10.0.0.2
 ipv4 management-interface address 10.0.0.3 16
 ip dynamic-port 50020 to 50030
 application app1
  software hellodocker.zip 
  run-options " --restart on-failure:5 --blkio-weight 16 --business-ip 10.0.0.1 --manage-ip 10.0.0.3 --port-range 50020-50030"
  start position slot 1
 application app2
  software hellodocker.zip 
  run-options " --restart on-failure:5 --blkio-weight 16 --business-ip 10.0.0.2 --port-range 50020-50030"
  start position slot 1
#
```
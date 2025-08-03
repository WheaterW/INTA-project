Installing the Image Software Package
=====================================

Installing the Image Software Package

#### Context

Currently, only the local image software package can be installed. Before the installation, perform the following operations:

* Create an image storage partition to store the image software package and public key file.
* Upload the image software package to the **flash:/oas/images/** directory of the device.
* Upload the public key file corresponding to the signature of the image description file to the **flash:/oas/images** directory of the device.

#### Procedure

1. Create an image storage partition.
   
   
   ```
   [create virtual-partition](cmdqueryname=create+virtual-partition) size partition-size type image
   ```
   
   After this command is executed, the **flash:/oas/images** directory is created to store the image software package and public key file.
2. Upload the image software package and public key file to the **flash:/oas/images** directory. For details about how to upload a file, see "File System Management Configuration" in Configuration Guide > Basic Configuration.
3. Install the public key corresponding to the signature of the image description file.
   
   
   ```
   [install public-key](cmdqueryname=install+public-key) public-key-name fingerprint fingerprint-key
   ```
4. Install the image software package for the application.
   
   
   ```
   [install application-software](cmdqueryname=install+application-software) software-path
   ```

#### Verifying the Configuration

* Run the [**display oas virtual-partition**](cmdqueryname=display+oas+virtual-partition) command to check information about the created virtual partition.
* Run the [**display oas public-key**](cmdqueryname=display+oas+public-key) command to check the list of installed public keys.
* Run the [**display oas application-software**](cmdqueryname=display+oas+application-software) [ *software-name* **verbose** ] command to check information about the installed image software package.
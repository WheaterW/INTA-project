Configuring EVA Based on JSON Scripts
=====================================

Configuring EVA Based on JSON Scripts

#### Context

EVA obtains data by loading and parsing JSON scripts. JSON scripts are classified into single-task scripts and PMI scripts. PMI scripts have the PMI function.


#### Procedure

1. (Optional) Configure gRPC in dial-in mode.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the eva.kpi function is used in JSON scripts, this step is mandatory.
   
   
   
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the gRPC view.
      
      
      ```
      [grpc](cmdqueryname=grpc)
      ```
   3. Enter the server view.
      
      
      ```
      [grpc server](cmdqueryname=grpc+server)
      ```
   4. Configure the source IPv4 address of the gRPC server.
      
      
      ```
      [source-ip](cmdqueryname=source-ip) 0.0.0.0
      ```
   5. Set the port number of the gRPC server to 57400.
      
      
      ```
      [server-port](cmdqueryname=server-port) 57400
      ```
   6. Enable the gRPC service.
      
      
      ```
      [server enable](cmdqueryname=server+enable)
      ```
   7. Exit the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      [quit](cmdqueryname=quit)
      ```
   8. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. (Optional) Enable NETCONF.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the eva.netconfGet function is used in JSON scripts, this step is mandatory.
   
   
   
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable NETCONF.
      
      
      ```
      [snetconf server enable](cmdqueryname=snetconf+server+enable)
      ```
   3. Exit the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. Install and register the script.
   
   
   * Method 1: You can manually download scripts from servers (for single-task scripts and PMI scripts).
     1. Upload a script to the device.
        
        For details on how to upload a file to the device, see "File System Management Configuration" in Configuration Guide > Basic Configuration.
     2. Install and register the script.
        ```
        [install eva script](cmdqueryname=install+eva+script) fileName [ inspection ]
        ```
        
        When installing the PMI script, you must specify the **inspection** parameter. Before the PMI script is executed, you cannot install it again.
   * Method 2: The EVA module automatically downloads scripts from servers (only for PMI scripts).Download, install, and register the script.
     ```
     [install eva script](cmdqueryname=install+eva+script) fileName inspection { [ftp](cmdqueryname=ftp) | sftp } { ipv4 ipv4Address | ipv6 ipv6Address } port portNum username userName password pwd [ vpn-instance vpnInstance ] [ server-path serverPath ]
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the [**install feature-software**](cmdqueryname=install+feature-software) **WEAKEA** command.
     
     SFTP is recommended because it is more secure than FTP.
4. (Optional) Uninstall a script.
   
   
   * Uninstall a single-task script.
     ```
     [uninstall eva script](cmdqueryname=uninstall+eva+script) fileName
     ```
   * Uninstall a PMI script.
     ```
     [uninstall eva script inspection](cmdqueryname=uninstall+eva+script+inspection)
     ```
     
     You cannot install the PMI script again before the uninstallation is complete.
5. (Optional) Configure the system to save the EVA script check result and collected data in the buffer to the **flash:/eva/checkresult** or **flash:/eva/collection** directory. (This step is performed only for single-task scripts).
   
   
   ```
   [save eva check-result](cmdqueryname=save+eva+check-result)
   ```
   
   By default, the system saves the EVA script check result and collected data in the buffer to the **flash:/eva/checkresult** or **flash:/eva/collection** directory only when the size of the EVA script check result and collected data in the buffer exceeds 2 MB or the number of the result and data records exceeds 50, or the system saves the EVA script check result and collected data in the buffer to the **flash:/eva/checkresult** or **flash:/eva/collection** directory every 30 minutes.
   
   You do not need to run this command for PMI scripts. After the PMI is complete, the system automatically saves the EVA script check result and collected data in the buffer to the **flash:/eva/checkresult** or **flash:/eva/collection** directory, compresses the result and data into **eva\_inspection\_***current time***.zip**, and saves the file to the **flash:/eva** directory. If the device directly downloads the script from the FTP or SFTP server and installs and registers the script, it automatically uploads the content in the **flash:/eva** directory to the server and deletes the **eva\_inspection\_***current time***.zip** package after the PMI.

#### Verifying the Configuration

* Run the [**display eva fault-event**](cmdqueryname=display+eva+fault-event) [ *filename* ] { **matched** | **unmatched** | **all** } [ *begintime* *endtime* ] command to check EVA events and matching information about related strategies.
* Run the [**display eva fault**](cmdqueryname=display+eva+fault) [ **unrecovered** | **recovered** ] [ *object* ] [ *beginTime* *endTime* ] command to check the fault data managed using EVA.
* Run the [**display eva register-events**](cmdqueryname=display+eva+register-events) [ *filename* ] command to check registration information about the event configured in an EVA script.
* Run the [**display eva register-status**](cmdqueryname=display+eva+register-status) [ *filename* ] command to check the registration status of an EVA script.
* Run the [**display eva register-strategy**](cmdqueryname=display+eva+register-strategy) [ *filename* ] command to check registration information about the strategy configured in an EVA script.
* Run the [**display eva script-item status**](cmdqueryname=display+eva+script-item+status) command to check the running status of an EVA script.
* Run the [**display eva inspection history**](cmdqueryname=display+eva+inspection+history) command to check the execution history of the EVA PMI script.
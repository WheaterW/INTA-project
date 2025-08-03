Configuring EVA Based on Python Scripts
=======================================

Configuring EVA Based on Python Scripts

#### Context

EVA extends the Python rules of OPS to use customized Python scripts to analyze and judge telemetry data, and perform troubleshooting based on customized strategies.

This function does not have independent configuration or commands. OPS commands are used to install and register related Python scripts.

![](../public_sys-resources/note_3.0-en-us.png) 

Before using the EVA function, you need to complete the basic configurations of the OPS function.



#### Procedure

1. (Optional) Configure gRPC in dial-in mode.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the addkpi or addinnerkpi function is used in Python scripts, this step is mandatory.
   
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
   7. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```
2. Upload a script to the device.
   
   
   
   For details on how to upload a file to the device, see "File System Management Configuration" in Configuration Guide > Basic Configuration.
3. Install and register the script.
   
   
   
   This operation must be performed using OPS commands. For details, see "Manually Running a Python Script" under "Configuring a Command Assistant" in Configuration Guide > System Management Configuration > OPS Configuration.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If another script is nested in the script, run the [**ops install file**](cmdqueryname=ops+install+file) command to install the nested script before registering the script.
   
   When running the [**ops run python**](cmdqueryname=ops+run+python) *script-name* *arguments* command to register a script, set *script-name* to the EVA built-in script **evamain.py** and *arguments* to **install** *customized script name*. An example is as follows:
   
   ```
   ops run python evamain.py install cpuMemHigh.py
   ```
4. (Optional) Uninstall a script.
   
   
   
   Run the [**ops run python**](cmdqueryname=ops+run+python) *script-name* *arguments* command, with *script-name* set to **evamain.py** (EVA built-in script name) and *arguments* set to **uninstall** *customized script name*. The built-in scripts **cpuHigh.py** and **memHigh.py** cannot be uninstalled.

#### Verifying the Configuration

* Run the [**display eva fault-event**](cmdqueryname=display+eva+fault-event) [ *filename* ] { **matched** | **unmatched** | **all** } [ *begintime* *endtime* ] command to check EVA events and matching information about related strategies.
* Run the [**display eva fault**](cmdqueryname=display+eva+fault) [ **unrecovered** | **recovered** ] [ *object* ] [ *beginTime* *endTime* ] command to check the fault data managed using EVA.
* Run the [**display eva register-events**](cmdqueryname=display+eva+register-events) [ *filename* ] command to check registration information about the event configured in an EVA script.
* Run the [**display eva register-status**](cmdqueryname=display+eva+register-status) [ *filename* ] command to check the registration status of an EVA script.
* Run the [**display eva register-strategy**](cmdqueryname=display+eva+register-strategy) [ *filename* ] command to check registration information about the strategy configured in an EVA script.
* Run the [**display eva script-item status**](cmdqueryname=display+eva+script-item+status) command to check the running status of an EVA script.
* Run the [**display eva operation-result**](cmdqueryname=display+eva+operation-result) [ *filename* ] command to check the execution result of the action in an EVA script.
Adding Ports to MSTP Processes
==============================

Adding Ports to MSTP Processes

#### Context

Ports added to MSTP processes will be included in MSTP calculation.

* Links that connect MSTP-enabled devices and access rings are access links.
* The link shared by multiple access rings is a shared link. Ports on a shared link are included in MSTP calculation in multiple access rings and MSTP processes.


#### Procedure

* Add a port on an access link to an MSTP process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view. In this command, specify the Layer 2 interface that connects the device to the access ring.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Add the port to a specified MSTP process.
     
     
     ```
     [stp binding process](cmdqueryname=stp+binding+process) process-id
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Add a port on a shared link to MSTP processes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view. In this command, specify the interface on the shared link between the devices configured with MSTP multi-process, but not the interface that connects the device to the access ring.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure the port to participate in calculation in multiple MSTP processes.
     
     
     ```
     [stp binding process](cmdqueryname=stp+binding+process) process-id1 [ to process-id2 ] link-share
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If an MSTP process has one or more shared links, run the [**stp enable**](cmdqueryname=stp+enable) command in the MSTP process view. For a port on a shared link, run the [**stp enable**](cmdqueryname=stp+enable) command in the interface view.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
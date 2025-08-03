Creating an MSTP Process
========================

Creating an MSTP Process

#### Context

A process ID uniquely identifies an MSTP process. An MSTP-enabled device performs MSTP calculation on a per-process basis after its ports are added to processes. Only relevant ports are processed in this calculation.

The following procedure applies only to devices that are connected to access rings.

![](public_sys-resources/note_3.0-en-us.png) 

A default MSTP process with an ID of 0 is established when a device starts. MSTP configurations in the system view and interface view belong to this process, which works in MSTP mode by default.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an MSTP process and enter the MSTP process view.
   
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
3. Configure the device to work in MSTP mode.
   
   
   ```
   [stp mode](cmdqueryname=stp+mode) mstp
   ```
4. Configure the TC notification function for the new MSTP process. After the new MSTP process receives a TC BPDU, it immediately notifies MSTIs in the default MSTP process to update MAC address entries and ARP entries. This prevents service interruptions.
   
   
   ```
   [stp tc-notify process 0](cmdqueryname=stp+tc-notify+process+0)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
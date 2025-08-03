Enabling MSTP
=============

Enabling MSTP

#### Context

After MSTP multi-process is enabled on a device, you must enable MSTP in the MSTP process view so configuration can take effect.

Enabling MSTP on a ring network immediately triggers spanning tree calculation, during which network flapping may occur if there are changes to parameters such as device and interface priorities. To ensure rapid and stable spanning tree calculation, it is important to complete basic configurations on devices and interfaces before enabling MSTP.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSTP process view by specifying the process ID.
   
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
3. Enable MSTP.
   
   
   ```
   [stp enable](cmdqueryname=stp+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
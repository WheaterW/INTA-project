Setting a Restart Mode for a Laser
==================================

Setting a Restart Mode for a Laser

#### Context

After ALS is enabled, the laser is automatically shut down if a fiber is not properly installed on an interface or an optical fiber link is faulty. You can determine whether to restart the laser automatically or manually after the fault condition is cleared:

* Automatic restart mode: The laser automatically emits pulses at intervals to detect whether the fault condition is rectified. If the fault condition is rectified, the laser automatically starts up.
* Manual restart mode: You must start the laser manually after the fault condition is rectified. The laser then sends a pulse to detect whether the fault condition is rectified.

#### Procedure

* Configure the automatic restart mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the laser of the optical module to work in automatic restart mode.
     
     
     ```
     [als restart mode](cmdqueryname=als+restart+mode) [automatic](cmdqueryname=automatic)
     ```
     
     By default, a laser works in automatic restart mode.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the manual restart mode.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the laser of the optical module to work in manual restart mode.
     
     
     ```
     [als restart mode](cmdqueryname=als+restart+mode) [manual](cmdqueryname=manual)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  5. Start the laser of the optical module manually. After a fiber is installed on the interface or the connected optical link recovers, you must use this command to manually start the laser.
     
     
     ```
     [als restart](cmdqueryname=als+restart)
     ```
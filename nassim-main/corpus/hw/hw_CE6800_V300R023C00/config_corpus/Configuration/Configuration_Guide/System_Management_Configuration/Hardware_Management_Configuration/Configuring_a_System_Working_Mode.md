Configuring a System Working Mode
=================================

Configuring a System Working Mode

#### Context

A device can work in low-latency mode or standard-forward mode. When a device starts with the factory default configuration, it starts in low-latency mode. After a device starts, you can run a command to manually configure the system working mode for next startup.

![](public_sys-resources/note_3.0-en-us.png) 

* After configuring the system working mode for next startup, you need to restart the device for the configuration to take effect.
* Only the CE6885-LL-56F supports this configuration.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Configure a system working mode for next startup.
   
   
   ```
   
   [set system next-work-mode](cmdqueryname=set+system+next-work-mode) { standard-forward | low-latency }
   ```
   
   By default, a device starts in low-latency mode.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

Run the [**display system work-mode**](cmdqueryname=display+system+work-mode) command to check the current working mode and the working mode for next startup.
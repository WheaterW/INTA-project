Disabling Device Reset Triggered by System Database Faults
==========================================================

Disabling Device Reset Triggered by System Database Faults

#### Context

When a fault occurs in the system database of a network device, a device reset is triggered by default. If you determine that the fault does not affect services and the device does not need to be restarted, you can disable device reset triggered by silent faults.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable device reset triggered by faults.
   
   
   ```
   [ndb silent fault disable](cmdqueryname=ndb+silent+fault+disable)
   ```
   
   By default, a device is reset when a fault occurs in the system database of a network device.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
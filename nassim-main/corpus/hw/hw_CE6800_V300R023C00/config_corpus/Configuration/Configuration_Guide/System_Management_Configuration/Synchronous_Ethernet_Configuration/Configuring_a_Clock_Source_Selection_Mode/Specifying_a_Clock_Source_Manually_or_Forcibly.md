Specifying a Clock Source Manually or Forcibly
==============================================

Specifying a Clock Source Manually or Forcibly

#### Context

By default, the system uses the automatic clock source selection algorithm to determine the clock source to be synchronized with. You can also manually or forcibly specify the clock source to be synchronized with based on the priority of each clock source.

* In manual mode:
  + The manually specified clock source takes effect only when it is in the normal or holdoff (the intermediate state between the hold state and normal state) state and has the highest SSM quality level.
  + If a manually specified clock source becomes invalid, the device switches to work in automatic clock source selection mode. If the fault of the manually specified clock source is rectified, the device will not switch back to work in manual clock source selection mode. After the device restarts, the automatic clock source selection mode is restored.
* In forcible mode:
  + Ensure that clock synchronization is enabled for the forcibly specified clock source.
  + The system clock enters the synchronization state only when the clock source is in the normal state and the SSM quality level is not DNU. Otherwise, the system clock enters the hold state.
  + If the forcibly specified clock source becomes invalid, the system clock enters the hold state. After the forcibly specified clock source recovers, the system clock re-synchronizes with the forcibly specified clock source. The device continues to work in forcible mode even after it restarts.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Manually or forcibly specify the clock source to be synchronized with for the system clock.
   
   
   ```
   [clock](cmdqueryname=clock) { manual | force } source { interface interface-type interface-number | ptp }
   ```
   
   By default, the system uses the automatic clock source selection algorithm to determine the clock source to be synchronized with.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
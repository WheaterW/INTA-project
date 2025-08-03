Configuring the Hold Time of a Clock Source If Its Signals Become Invalid
=========================================================================

Configuring the Hold Time of a Clock Source If Its Signals Become Invalid

#### Context

If the signals of a clock source become invalid, the system waits until the specified hold time elapses before reporting the status change and triggering clock source re-selection based on the clock source selection algorithm. This prevents frequent clock source re-selection when clock signals become invalid intermittently.

You can set the hold time based on the clock source stability on a clock synchronization network.

* To quickly synchronize with another clock source when the current clock source becomes invalid, configure a shorter hold time for the current clock source.
* To prevent frequent clock source selection when the current clock source becomes invalid intermittently, configure a longer hold time for the current clock source.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the hold time of a clock source after its signals become invalid.
   
   
   ```
   [clock source-lost holdoff-time](cmdqueryname=clock+source-lost+holdoff-time) holdoff-time-value
   ```
   
   By default, the hold time of a clock source after its signals become invalid is 1000 ms.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
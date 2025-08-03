Setting an ALS Pulse Interval and Width for a Laser
===================================================

Setting an ALS Pulse Interval and Width for a Laser

#### Context

The ALS pulse interval indicates the time between two consecutive pulses and applies only to the automatic restart mode. The ALS pulse width indicates the pulse duration and applies to both the automatic and manual restart modes.

* In automatic restart mode, a small pulse width and a long pulse interval use less energy but cannot ensure the timely detection of a recovered optical link.
* In manual restart mode, a small pulse width uses less energy but takes longer to detect a recovered optical link. Conversely, a large pulse width ensures the prompt detection of a recovered optical link but uses more energy.

Determine a suitable laser pulse interval and width based on your network requirements.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   interface interface-type interface-number
   ```
3. Set an ALS pulse interval of the laser.
   
   
   ```
   [als restart pulse](cmdqueryname=als+restart+pulse) [interval](cmdqueryname=interval) interval-value
   ```
   
   The default ALS pulse interval is 100s.
4. Set an ALS pulse width of the laser.
   
   
   ```
   [als restart pulse](cmdqueryname=als+restart+pulse) [width](cmdqueryname=width) width-value
   ```
   
   The default ALS pulse width is 2s.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
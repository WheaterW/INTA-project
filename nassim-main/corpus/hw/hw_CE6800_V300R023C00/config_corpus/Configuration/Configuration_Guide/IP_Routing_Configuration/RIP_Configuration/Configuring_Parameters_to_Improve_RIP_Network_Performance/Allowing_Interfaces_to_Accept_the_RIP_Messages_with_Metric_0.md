Allowing Interfaces to Accept the RIP Messages with Metric 0
============================================================

Allowing Interfaces to Accept the RIP Messages with Metric 0

#### Context

On the live network, devices of some vendors do not accept the messages with metric 0. By default, Huawei devices do not accept the messages with metric 0. Therefore, RIP interfaces discard all the RIP messages with metric 0. To ensure that a Huawei device can interwork with a non-Huawei device that accepts the RIP messages with metric 0, run the [**undo zero-metric-check**](cmdqueryname=undo+zero-metric-check) command on the Huawei device to allow its interfaces to accept the RIP messages with metric 0.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Allow interfaces to accept the RIP messages with metric 0.
   
   
   ```
   [undo zero-metric-check](cmdqueryname=undo+zero-metric-check)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

To restore the default configuration, whereby an interface will not accept RIP messages with metric 0, run the [**zero-metric-check**](cmdqueryname=zero-metric-check) command.
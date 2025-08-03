Disabling RIP from Checking the RIP Packets with Metric 0
=========================================================

To ensure communication between two devices, only one of which accepts RIP packets with metric 0, you can disable the device that does not accept such packets from checking the RIP packets with metric 0.

#### Context

On the live network, devices of some vendors do not accept the packets with metric 0. By default, a Huawei device does not accept the packets with metric 0. Therefore, RIP interfaces discard all the RIP packets with metric 0. To ensure that a Huawei device can interwork with a non-Huawei device that accepts the RIP packets with metric 0, run the [**undo zero-metric-check**](cmdqueryname=undo+zero-metric-check) command on the Huawei device to allow its interfaces to accept the RIP packets with metric 0.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**rip**](cmdqueryname=rip) [ *process-id*] command to create a RIP process and enter the RIP view.
3. Run the [**undo zero-metric-check**](cmdqueryname=undo+zero-metric-check) command to allow interfaces to accept the RIP packets with metric 0.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

To restore the default configuration, whereby interfaces do not accept RIP packets with metric 0, run the [**zero-metric-check**](cmdqueryname=zero-metric-check) command.
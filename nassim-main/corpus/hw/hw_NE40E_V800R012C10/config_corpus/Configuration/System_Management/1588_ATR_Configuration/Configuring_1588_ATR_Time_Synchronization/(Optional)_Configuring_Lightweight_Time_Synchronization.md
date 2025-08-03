(Optional) Configuring Lightweight Time Synchronization
=======================================================

Lightweight time synchronization implements automatic identification and switching within a device, loosening the requirements on time synchronization precision and simplifying the configuration process.

#### Context

The system preferentially uses hop-by-hop 1588v2 time synchronization in In-situ Flow Information Telemetry (IFIT) delay measurement or other sub-millisecond-level synchronization precision scenarios. Hop-by-hop 1588v2 time synchronization requires that all devices on the network support 1588v2 in order to achieve delay measurement in the sub-microsecond range. If some devices on the network do not support 1588v2, you can enable lightweight and sub-millisecond-level time synchronization on downstream devices to achieve delay measurement in the sub-millisecond range.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* After lightweight time synchronization is enabled, reported PTSF alarms are cleared, and new PTSF alarms cannot be reported.
* Lightweight time synchronization does not need to be configured in non-IFIT or other non-sub-millisecond-level synchronization precision scenarios as doing so will impact time synchronization precision.
* Lightweight clocks cannot be used in mobile transport scenarios, because lightweight time synchronization cannot meet base station performance requirements.
* Do not enable lightweight time synchronization between inter-city devices for applications such as IFIT delay measurement that require sub-millisecond-level precision. For time synchronization between different cities, it is recommended that a time source device tracing the GNSS be deployed in each city; for time synchronization within the same city, deploy a lightweight time source device to synchronize time with the GNSS. This can meet the sub-millisecond-level time synchronization precision requirement.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp lite-sync**](cmdqueryname=ptp+lite-sync) **sub-ms enable** command to enable lightweight time synchronization.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
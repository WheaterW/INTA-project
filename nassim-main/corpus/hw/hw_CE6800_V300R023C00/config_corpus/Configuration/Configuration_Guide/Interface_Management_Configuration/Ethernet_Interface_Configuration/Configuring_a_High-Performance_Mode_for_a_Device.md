Configuring a High-Performance Mode for a Device
================================================

Configuring a High-Performance Mode for a Device

#### Context

A device consists of two forwarding chips. 25GE interfaces numbered 1 to 24 and 100GE interfaces numbered 1 to 3 belong to chip 1. 25GE interfaces numbered 25 to 48 and 100GE interfaces numbered 4 to 6 belong to chip 2. Chips 1 and 2 communicate with each other through internal communication interfaces. The bandwidth of a single chip on a device is 900 Gbit/s, whereas the bandwidth of an internal communication interface is only 300 Gbit/s. As such, the bandwidth of an internal communication interface is much lower than that of a single chip on the device. When the bandwidth of an internal communication interface cannot meet the bandwidth requirements for the interconnection between two chips, an hwBoardWarning alarm is generated (when the bandwidth usage of the internal communication interface exceeds 80% or packet loss occurs on the internal communication interface). In this case, you need to change the high-performance mode of the device to adjust the bandwidth of an internal communication interface. You can change the mode to **mode2**, **mode3**, **mode4**, and **mode5** in sequence until the hwBoardWarning alarm is cleared.

| Parameter | Meaning | Bandwidths of an Internal Communication Interface and a Single Chip |
| --- | --- | --- |
| mode1 | High-performance mode 1: All interfaces are available. | * Single chip: 900 Gbit/s * Internal communication interface: 300 Gbit/s |
| mode2 | High-performance mode 2: 25GE interfaces numbered 21 to 28 are unavailable. | * Single chip: 800 Gbit/s * Internal communication interface: 400 Gbit/s |
| mode3 | High-performance mode 3: 25GE interfaces numbered 19 to 30 are unavailable. | * Single chip: 750 Gbit/s * Internal communication interface: 450 Gbit/s |
| mode4 | High-performance mode 4: 25GE interfaces numbered 17 to 32 are unavailable. | * Single chip: 700 Gbit/s * Internal communication interface: 500 Gbit/s |
| mode5 | High-performance mode 5: 25GE interfaces numbered 13 to 36 are unavailable. | * Single chip: 600 Gbit/s * Internal communication interface: 600 Gbit/s |


![](public_sys-resources/note_3.0-en-us.png) 

Only the CE6863H/CE6863H-K supports this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a high-performance mode for the device.
   
   
   ```
   [port high-performance mode](cmdqueryname=port+high-performance+mode) { mode1 | mode2 | mode3 | mode4 | mode5 }
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
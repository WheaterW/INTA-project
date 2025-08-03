Protection Switching
====================

The protection switching mechanism used in clock synchronization enables another clock source to take over automatically if a clock source with which a device is synchronized is missing. The new clock source may synchronize clock signals from the same reference clock as the old clock source, or it may be a clock source with a lower SSM quality level. When the original clock source is restored, the device determines whether to re-select a clock source based on the configuration.

#### Protection Switching in Automatic Clock Source Selection Mode

As shown in [Figure 1](#EN-US_CONCEPT_0000001513039874__fig1873013613199), when the network functions properly, the device determines clock source 1 and the corresponding clock synchronization path by using the automatic clock source selection algorithm based on clock source priorities and SSM quality levels.

**Figure 1** Protection switching in automatic clock source selection mode when the network functions properly  
![](figure/en-us_image_0000001513039930.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001513039874__fig1240533832316), if a link fails, the device determines that the clock source to be synchronized with remains unchanged by using the automatic clock source selection algorithm and only updates the clock synchronization path.

**Figure 2** Protection switching in automatic clock source selection mode in case of a link fault  
![](figure/en-us_image_0000001563879885.png)

As shown in [Figure 3](#EN-US_CONCEPT_0000001513039874__fig14150193213254), if a clock source fails, the device determines to switch to clock source 2 by using the automatic clock source selection algorithm and updates the clock synchronization path.

**Figure 3** Protection switching in automatic clock source selection mode in case of a clock source fault  
![](figure/en-us_image_0000001512840350.png)

As shown in [Figure 4](#EN-US_CONCEPT_0000001513039874__fig1083919143271), if the link or clock source fault is rectified, the device determines to re-synchronize the time with clock source 1 by using the automatic clock source selection algorithm and updates the clock synchronization path.

**Figure 4** Protection switching in automatic clock source selection mode when the link or clock source fault is rectified  
![](figure/en-us_image_0000001564119981.png)

#### Protection Switching in Manual Clock Source Selection Mode

* If the manually specified clock source functions properly, the device synchronizes with this clock source.
* If the manually specified clock source is faulty, the device switches to work in automatic clock source selection mode. It then synchronizes with a new clock source using the automatic clock source selection algorithm and updates the clock synchronization path.
* After the fault of the manually specified clock source is rectified, the device remains in automatic clock source selection mode and uses the automatic clock source selection algorithm to determine whether to synchronize with the clock source.

#### Protection Switching in Forcible Clock Source Selection Mode

* If the forcibly specified clock source functions properly, the device synchronizes with this clock source.
* If the forcibly specified clock source is faulty, the device clock enters the hold state.
* After the fault of the forcibly specified clock source is rectified, the device re-synchronizes with the forcibly specified clock source.
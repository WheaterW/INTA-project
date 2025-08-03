Configuring the Automatic Clock Source Selection Mode
=====================================================

Configuring the Automatic Clock Source Selection Mode

#### Usage Scenario

The NE40E supports three clock source selection modes: automatic clock source selection, manual clock source selection, and forcible clock source selection. In automatic clock source selection mode, the device uses the automatic clock source selection algorithm to determine a clock source to be traced. For details about how to configure manual or forcible clock source selection, see [Configuring the Manual or Forcible Clock Source Selection Mode](dc_ne_clock_cfg_5010.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

On a clock synchronization network, if the status or quality of clock sources cannot remain stable for a long time, you are advised to configure the automatic clock source selection mode to ensure that the device can trace the optimal clock source. Manual and forcible clock source selection modes do not support automatic protection switching of clock sources.



#### Pre-configuration Tasks

None


[Configuring a Clock Source](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_clock_cfg_5006.html)



[(Optional) Configuring Parameters for Automatic Clock Source Selection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_clock_cfg_5007.html)



[Verifying the Configuration of the Automatic Clock Source Selection Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_clock_cfg_5009.html)
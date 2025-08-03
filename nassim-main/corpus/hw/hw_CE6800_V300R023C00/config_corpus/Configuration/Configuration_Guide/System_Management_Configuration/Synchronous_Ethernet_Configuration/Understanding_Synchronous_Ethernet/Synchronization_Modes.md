Synchronization Modes
=====================

Two clock synchronization modes are available on a communications network: pseudo synchronization and master-slave synchronization.

#### Pseudo Synchronization

In pseudo synchronization, each switching office has an independent clock (typically a cesium clock) with high precision and stability. Clock synchronization is not performed between the switching offices, as each office has an independent clock. In this scenario, the frequency and phase differences among the clocks of different switching offices are too small to affect network transmission and can therefore be ignored.

Pseudo synchronization is typically used on communications networks between countries.


#### Master-Slave Synchronization

**Classification of Master-Slave Synchronization**

In master-slave synchronization, a high-precision clock is configured as the master clock, a switching office synchronizes the time with the master clock, and all branch offices synchronize the time with their upper-level clocks.

Master-slave synchronization is typically used on a communications network inside a country or region, where one high-precision master clock serves as the reference clock for other NEs on the network.

Master-slave synchronization is classified as direct or hierarchical master-slave synchronization.

* Direct master-slave synchronization
  
  [Figure 1](#EN-US_CONCEPT_0000001513159814__fig148541932153811) illustrates direct master-slave synchronization, which applies to simple networks. All slave clocks synchronize with the master clock.
  
  **Figure 1** Direct master-slave synchronization  
  ![](figure/en-us_image_0000001513159846.png)
* Hierarchical master-slave synchronization
  
  [Figure 2](#EN-US_CONCEPT_0000001513159814__fig1671742917412) illustrates hierarchical master-slave synchronization, which applies to large and complex networks. In this mode, there are three stratums of clocks: stratum-1 master clock, stratum-2 slave clock, and stratum-3 slave clock. The stratum-2 slave clock synchronizes with the stratum-1 master clock, and the stratum-3 slave clock synchronizes with the stratum-2 slave clock.
  
  **Figure 2** Hierarchical master-slave synchronization  
  ![](figure/en-us_image_0000001563879837.png)

**Reliability of Master-Slave Synchronization**

To improve reliability of master-slave synchronization, two master clocks can be deployed on the network, one as the active master clock and the other as the standby master clock. Both the active and standby master clocks are cesium clocks.

All NEs, including the standby master clock, typically synchronize the time with the active master clock. If the active master clock fails, the standby master clock takes over as the reference clock for the entire network. The system switches back to the active master clock when the failure is rectified, and the active master clock then functions as the reference clock for the entire network.

**Working States of the Slave Clock**

In master-slave synchronization mode, a slave clock has three working states:

* Synchronization state (normal)
  
  The slave clock synchronizes the time with and locks its upper-level clock source. Such a clock source may be the active master clock or the clock built into the upper-level NE.
* Holdover state (Hold)
  
  The slave clock enters the hold state after its reference clock is lost. In this case, the clock chip oscillator of the slave clock uses the last frequency information stored before the reference clock is lost as the reference clock. It can then provide clock signals that are consistent with the source reference clock. This ensures that there is only a small difference between the frequency of the slave clock and that of the reference clock within a certain period of time. Because the inherent frequency of the oscillator on the clock chip is prone to drifts, the slave clock in the hold state may lose accuracy over a prolonged period of time.
  
  In the hold state, if the slave clock re-locks the upper-level clock, the slave clock returns to the normal state. Otherwise, the slave clock enters the free state.
* Free-running state (Free)
  
  The clock chip oscillator of the slave clock works in the free state if the slave clock is disconnected from the reference clock or has remained in the hold state for too long.
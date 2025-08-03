Adding a FlexE or Ethernet NE in a FlexE Service Scenario
=========================================================

Adding an Ethernet NE to a live network running FlexE services involves the connection between a FlexE physical interface and standard Ethernet interface. If DCN auto-negotiation is enabled on the FlexE physical interface, the two interfaces can automatically communicate with each other, and the NMS can manage the FlexE NE.

#### Usage Scenario

* Adding a FlexE NE to a live network running FlexE services
  
  As shown in [Figure 1](#EN-US_TASK_0300605033__fig17226162925219), DeviceA and DeviceB work in FlexE mode on the live network, and the new NE DeviceC also works in FlexE mode.
  
  **Figure 1** Adding a FlexE NE to a live network running FlexE services  
  ![](figure/en-us_image_0300605039.png)
  
  After DeviceC is added, it successfully connects to DeviceA and DeviceB because they all work in FlexE mode. In this case, the NMS can directly manage DeviceC.
* Adding an Ethernet NE to a live network running FlexE services
  
  As shown in [Figure 2](#EN-US_TASK_0300605033__fig5797014151514), DeviceA and DeviceB work in FlexE mode on the live network, and the new NE DeviceC works in Ethernet mode.
  
  **Figure 2** Adding an Ethernet NE to a live network running FlexE services  
  ![](figure/en-us_image_0300605041.png)
  
  For different scenarios, you can perform the corresponding operations to ensure that the new Ethernet NE can be successfully connected and managed by the NMS.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In the following scenarios, the operations on DeviceB are the same as those on DeviceA.

#### Procedure

* If DeviceA supports DCN auto-negotiation on FlexE physical interfaces, but DeviceC does not:
  
  
  
  After DeviceC is added, the underlying working mode of the FlexE physical interface on DeviceA automatically switches from FlexE to standard Ethernet within about 10s because DCN auto-negotiation is enabled on the FlexE physical interface by default. The NMS can then manage DeviceC.
  
  + If you run the following commands on DeviceA within 20 minutes of being added, the configuration takes effect immediately to ensure DCN continuity.
    1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
    2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the FlexE physical interface view.
    3. Run the [**force-physical-mode ethernet**](cmdqueryname=force-physical-mode+ethernet) command to forcibly switch the underlying working mode of the FlexE physical interface to standard Ethernet.
    4. To change the time for switching the underlying working mode of a FlexE physical interface from standard Ethernet back to FlexE, or to disable a FlexE physical interface from switching from the standard Ethernet mode back to the FlexE mode, perform the following operations:
       - Run the [**phyautoclear forcephysicalmode**](cmdqueryname=phyautoclear+forcephysicalmode) **enable** *cleartime* command to set the time for switching the underlying working mode of the FlexE physical interface from standard Ethernet back to FlexE.
       - Run the [**phyautoclear forcephysicalmode disable**](cmdqueryname=phyautoclear+forcephysicalmode) command to disable the underlying working mode of the FlexE physical interface from switching from standard Ethernet back to FlexE.
  + If the preceding commands are not run on DeviceA within 20 minutes of being added, the underlying working mode of the FlexE physical interface on DeviceA is switched from the standard Ethernet mode to the FlexE mode at the 20-minute mark. DCN auto-negotiation is then performed 10 seconds later to implement DCN connectivity. As a result, the NMS cannot manage DeviceC for about 10 seconds, and the process repeats.
  
  If you want to continue to run FlexE services on the live network, perform the following operations:
  
  1. Run the [**flexe enable port**](cmdqueryname=flexe+enable+port) *port-position* command on DeviceC to switch the working mode of the Ethernet interface from standard Ethernet to FlexE. Because the underlying working mode of the FlexE physical interface on DeviceA has been switched to standard Ethernet, the DCN channel between DeviceC and DeviceA is interrupted, and DeviceC is disconnected from the NMS.
  2. Change the status of the FlexE physical interface on DeviceC manually, triggering the underlying working mode of DeviceA's FlexE physical interface connected to the FlexE physical interface on DeviceC to quickly switch back to the FlexE mode. You can perform the following operations:
     + Run the [**laser turn-off**](cmdqueryname=laser+turn-off) command on DeviceC to disable the optical module laser, and then run the [**laser turn-on**](cmdqueryname=laser+turn-on) command to enable the optical module laser.
     + Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceC to disable the interface, and then run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to enable the interface.
  
  After the preceding operations are complete, the FlexE physical interface connecting DeviceA to DeviceC is switched back to the FlexE mode. The two devices are now successfully connected using FlexE, and the NMS can continue to manage DeviceC.
* If both DeviceA and DeviceC support DCN auto-negotiation on FlexE physical interfaces:
  
  
  
  After DeviceC is added, the underlying working mode of the FlexE physical interface on DeviceA automatically switches from FlexE to standard Ethernet within about 10s because DCN auto-negotiation is enabled on the FlexE physical interface by default. The NMS can then manage DeviceC.
  
  DeviceC supports DCN auto-negotiation on FlexE physical interfaces, and this function is enabled by default. To continue to run FlexE services on the live network, run the [**flexe enable port**](cmdqueryname=flexe+enable+port) *port-position* command on DeviceC to switch the working mode of the Ethernet interface from standard Ethernet to FlexE.
* If DeviceA does not support DCN auto-negotiation on FlexE physical interfaces, but DeviceC does:
  
  
  
  After DeviceC is added, run the [**force-physical-mode ethernet**](cmdqueryname=force-physical-mode+ethernet) command on DeviceA to forcibly switch the underlying working mode of the FlexE physical interface to standard Ethernet. In this case, DeviceC can communicate with DeviceA and can be managed by the NMS.
  
  If you want to continue to run FlexE services on the live network, perform the following operations:
  
  1. Run the [**flexe enable port**](cmdqueryname=flexe+enable+port) *port-position* command on DeviceC to switch the working mode of the Ethernet interface from standard Ethernet to FlexE. DeviceC supports DCN auto-negotiation on FlexE physical interfaces, and this function is enabled by default. Therefore, the underlying working mode of the FlexE physical interfaces automatically switches from FlexE to standard Ethernet within about 10s.
  2. Run the [**undo force-physical-mode**](cmdqueryname=force-physical-mode+ethernet) command on DeviceA to restore the underlying working mode of the FlexE physical interface to FlexE.
  3. Change the status of the FlexE physical interface on DeviceA manually, triggering the underlying working mode of DeviceC's FlexE physical interface connected to the FlexE physical interface on DeviceA to quickly switch back to the FlexE mode. You can perform the following operations:
     + Run the [**laser turn-off**](cmdqueryname=laser+turn-off) command on DeviceA to disable the optical module laser, and then run the [**laser turn-on**](cmdqueryname=laser+turn-on) command to enable the optical module laser.
     + Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceA to disable the interface, and then run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to enable the interface.
  
  After the preceding operations are complete, the FlexE physical interface connecting DeviceC to DeviceA is switched back to the FlexE mode. The two devices are now successfully connected using FlexE, and the NMS can continue to manage DeviceC.
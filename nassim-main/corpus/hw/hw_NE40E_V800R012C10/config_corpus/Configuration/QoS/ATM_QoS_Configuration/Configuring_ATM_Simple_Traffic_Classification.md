Configuring ATM Simple Traffic Classification
=============================================

This section describes how to apply simple traffic classification to an ATM network.

#### Usage Scenarios

ATM simple traffic classification is applied to the following situations:

* Ethernet or IP packets are carried over the existing ATM network (1483R transparent transmission)
  
  As shown in [Figure 1](#EN-US_TASK_0172371651__fig_dc_ne_qos_cfg_01237802), DeviceA and DeviceB are edge Routers of two ATM networks to provide access to the IP network. On the ATM network, IP packets are transmitted in AAL5 frames. When IP packets are sent out of the ATM network, DeviceA and DeviceB perform ATM termination and forward IP packets to other types of interfaces or forward Layer 2 Ethernet frames to the Ethernet interface.
  
  **Figure 1** Networking diagram for transmitting Ethernet or IP packets over the ATM network  
  ![](images/fig_dc_ne_qos_cfg_01237802.png "Click to enlarge")

You can configure ATM simple traffic classification on an interface, or on a PVC or PVP. Note that:

* If ATM simple traffic classification is configured on an interface, it takes effect on all the PVCs or PVPs under the interface.
* If ATM simple traffic classification is configured not on the interface but only on a specific PVC or PVP, it takes effect only on the PVC or PVP.
* If ATM simple traffic classification is configured on both ATM interface and PVC or PVP, the configuration on PVC or PVP preferentially takes effect.

#### Pre-configuration Tasks

Before configuring ATM simple traffic classification, complete the following tasks:

* Configuring link attributes of the interface
* Allocating IP addresses for the interface
* Configuring PVC or PVP and the related parameters
* Configuring ATM services (IPoA)


[Enabling ATM Simple Traffic Classification](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012380.html)

ATM simple traffic classification can be enabled only on ATM sub-interfaces or PVCs/PVPs.

[Verifying the Configuration of ATM BA Classification](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012382.html)

After configuring BA classification on an ATM interface, check the configurations.
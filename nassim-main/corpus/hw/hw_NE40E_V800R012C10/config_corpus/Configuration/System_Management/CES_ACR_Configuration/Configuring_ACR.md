Configuring ACR
===============

This section describes how to configure ACR.

#### Usage Scenario

Adaptive Clock Recovery (ACR) is a clock synchronization technology used to restore service clocks on a network if they are asynchronous. The accuracy of ACR is largely affected by the packet switched network (PSN).

In terms of transparent clock transmission, ACR can be specifically implemented in two modes, namely, the circuit emulation service (CES) mode and the timing over packet (TOP) mode. In CES mode, clock signals are transparently transmitted from the master clock to the slave clock using time division multiplexing (TDM). In TOP mode, clock signals are transmitted from the master clock to the slave clock through a dedicated PW. Currently, Huawei devices support CES-ACR for clock synchronization.

As shown in [Figure 1](#EN-US_TASK_0000001778921378__fig_dc_ne_clock_cfg_501801), in ACR, the downstream slave clock synchronizes with the upstream master clock. In this case, you need to configure a clock recovery domain on the E1 interface of the slave clock so that it can synchronize with the upstream clock.

**Figure 1** Networking diagram of ACR clock synchronization  
![](figure/en-us_image_0000001779081118.png)  


#### Pre-configuration Tasks

Before configuring ACR, complete the following tasks:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When configuring ACR, ensure that the master and slave devices are equipped with a subcard that supports CES ACR.

* Configure link-layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol status of each interface is Up.
* Configure static routes or an IGP to ensure reachable routes between nodes.
* Ensure that an E1 interface exists on the involved device.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure a clock recovery domain on the slave device that needs clock recovery.
   
   
   * # If the device is installed with an E1 subcard, perform the following operations:
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This step is supported only on the NE40E-M2E, NE40E-M2F, NE40E-M2H, NE40E-M2K.
     
     1. Run the [**controller e1**](cmdqueryname=controller+e1) *controller-number* command to enter the corresponding E1 interface view.
     2. Run the [**clock**](cmdqueryname=clock) **recovery-domain** *domain-value* command to configure a clock recovery domain for the E1 interface.
     3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Perform the following operations on the slave clock that needs clock recovery to configure the clock recovered by ACR as the system clock.
   1. Configure the attributes of a clock source in the recovery domain.
      
      
      
      Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-id* **recovery-domain** *domain-value*  **ssm** { **prc** | **ssua** | **ssub** | **sec** | **dnu** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the CES ACR clock source.
      
      
      
      Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-id* **recovery-domain** *domain-value* **clock-id** *clock-id* command to configure a clock ID for the CES ACR clock source.
      
      
      
      Run the [**clock source cesacr**](cmdqueryname=clock+source+cesacr) **slot** *slot-id* **card** *card-id* **recovery-domain** *domain-value* **priority** *priority-value* command to configure a priority for the CES ACR clock source.
   2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

# If the ACR function on the Router is normal, run the [**display acr-dcr**](cmdqueryname=display+acr-dcr) command to check the current ACR information.

```
<HUAWEI> display acr-dcr slot  card 1
```

# Check ACR information of clock recovery domain 4 on subcard 1 of the interface board in slot 1.

```
<HUAWEI> display acr-dcr slot  card 1 recovery-domain 4
```


[Configuring a Clock Recovery Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_clock_cfg_5018.html)



[Configuring a Clock Signal Source as the System Clock for CES ACR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_clock_cfg_5019.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_clock_cfg_5020.html)
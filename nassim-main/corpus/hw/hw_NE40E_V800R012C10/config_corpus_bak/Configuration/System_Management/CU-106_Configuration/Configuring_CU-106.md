Configuring CU-106
==================

Configuring_CU-106

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001778921430__fig_dc_ne_cu-106_cfg_800501), the BITS interface that functions as the T-GM obtains high-accuracy time information from a global positioning system (GPS), encapsulates the information into a CU-106 packet, and sends the packet to the transport network. A transport network device that functions as the T-BC transparently transmits the time information to all devices on the transport network. BCs send high-accuracy time information carried in the CU-106 packet to the gNodeB.**Figure 1** CU-106 application over a transport network  
![](figure/en-us_image_0000001778921494.png)


#### Pre-configuration Tasks

* Set physical parameters of interfaces and ensure that the interfaces are physically up.


[Importing Time Signals from an External BITS Time Source](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_8007.html)

On a G.8275.1 network, time signals are typically imported from an external BITS time source. You can configure multiple Routers to import time signals from an external BITS time source. A master clock can be selected dynamically using the BMCA.

[Configuring Clock Source Attributes for BMCA Selection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_9002.html)

After multiple T-BCs are configured with the input of BITS signals, clock source attributes for BMCA selection can be configured on the T-BCs to allow the T-BCs to participate in BMCA selection. The local clocks of T-BCs can also be configured to participate in BMCA selection. BMCA can be used to dynamically determine the T-GM. The T-GM provides time signals for the entire CU-106 network. T-BCs use CU-106 to obtain time synchronization information from the T-GM.

[Globally Enabling CU-106](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_9003.html)

To ensure CU-106 for time synchronization, enable CU-106 globally in the system view and configure basic information on a device, such as the device type (T-BC or T-TC) and domain value.

[Enabling CU-106 on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_9004.html)

After enabling CU-106 in the system view, you need to enable CU-106 in the interface view.

[(Optional) Configuring the Time Synchronization Alarm Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_8012.html)

The time synchronization alarm function can be configured to help monitor the time synchronization status. When a time synchronization alarm is generated, the alarm information will be reported to the NMS for further troubleshooting and maintenance.

[Configuring Time Attributes for CU-106 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_9005.html)

This section describes how to configure time attributes for CU-106 packets. T-BCs exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain CU-106 connections. You can set the interval at which a CU-106 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

[(Optional) Configuring a CU-106 Packet Encapsulation Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_9006.html)

You can configure destination MAC addresses of packets according to the actual networking.

[Verifying the Configuration of CU-106](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cu-106_cfg_8009.html)

After configuring the CU-106 function, verify the configuration.
Configuring G.8275.1
====================

Configuring G.8275.1

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001825840849__fig_dc_ne_g82751_cfg_800501), the BITS interface that functions as the T-GM obtains high-accuracy time information from a global positioning system (GPS), encapsulates the information into a G.8275.1 packet, and sends the packet to the transport network. A transport network device that functions as the T-BC transparently transmits the time information to all devices on the transport network. BCs send high-accuracy time information carried in the G.8275.1 packet to the gNodeB.**Figure 1** G.8275.1 application over a transport network  
![](figure/en-us_image_0000001825721081.png)


#### Pre-configuration Tasks

* Set physical parameters of interfaces and ensure that the interfaces are physically Up.


[Importing Time Signals from an External BITS Time Source](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_8006.html)

On a G.8275.1 network, time signals are typically imported from an external BITS time source. You can configure multiple Routers to import time signals from an external BITS time source. A master clock can be selected dynamically using the BMCA.

[Configuring Time Source Attributes for BMCA Selection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_9002.html)

After BITS signal input is configured on multiple T-BCs, you can configure the time source attributes of the T-BCs to allow them to participate in BMCA source selection. You can also configure the local clocks of T-BCs to participate in BMCA source selection. The BMCA helps devices to dynamically select a master clock. The master clock provides time signals for the entire G.8275.1 network. T-BCs use G.8275.1 to achieve time synchronization with the grandmaster clock.

[Configuring G.8275.1 Globally](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_9003.html)

To ensure G.8275.1 for time synchronization, you need to globally enable G.8275.1 in the system view, set the device type to T-BC/T-TC, and configure basic information such as the domain value.

[Configuring G.8275.1 on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_9004.html)

After enabling G.8275.1 in the system view, you need to enable G.8275.1 in the interface view.

[(Optional) Configuring the Time Synchronization Alarm Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_8012.html)

After the time synchronization alarm function is configured to monitor time synchronization status information, the alarm information will be reported to the NMS for further troubleshooting and maintenance.

[(Optional) Configuring Time Attributes for G.8275.1 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_9005.html)

T-BCs exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain G.8275.1 connections. You can set the interval at which a G.8275.1 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

[(Optional) Configuring Encapsulation Modes for G.8275.1 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_9006.html)

You can configure destination MAC addresses of packets according to the actual networking.

[(Optional) Configuring a TOD Interface to Output Time Signals](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_9010.html)

TOD interfaces on T-BC devices can be configured to output time signals.

[Verifying the G.8275.1 Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_g82751_cfg_8009.html)

After configuring the G.8275.1 function, verify the configuration.
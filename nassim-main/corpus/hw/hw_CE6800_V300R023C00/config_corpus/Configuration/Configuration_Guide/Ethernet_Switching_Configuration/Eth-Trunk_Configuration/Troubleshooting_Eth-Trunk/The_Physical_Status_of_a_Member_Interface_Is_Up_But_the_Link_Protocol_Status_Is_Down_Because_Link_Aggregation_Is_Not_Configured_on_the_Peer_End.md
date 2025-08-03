The Physical Status of a Member Interface Is Up But the Link Protocol Status Is Down Because Link Aggregation Is Not Configured on the Peer End
===============================================================================================================================================

The Physical Status of a Member Interface Is Up But the Link Protocol Status Is Down Because Link Aggregation Is Not Configured on the Peer End

#### Fault Symptom

In the following figure, an Eth-Trunk interface is configured on DeviceA but not on DeviceB. As a result, the physical status of member interfaces on DeviceA is up but the link protocol status is down.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.

![](figure/en-us_image_0000001176741307.png)


#### Procedure

1. Run the [**display this**](cmdqueryname=display+this) command on 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 of DeviceB. The three interfaces do not join the Eth-Trunk interface. If the interfaces join the Eth-Trunk, you can view the following configuration in the command output.
   ```
   #
   interface 100GE1/0/1
    eth-trunk 1
   #
   ```
2. On DeviceB, configure the Eth-Trunk interface that works in the same mode as that on DeviceA. For details, see [Creating an Eth-Trunk Interface and Configure a Link Aggregation Mode for It](vrp_eth-trunk_cfg_0012.html).
Resetting a Board
=================

Resetting a Board

#### Context

When a board fails to be upgraded or works improperly, you can reset it. Doing so will update the version or restore the board to the normal state.

![](public_sys-resources/notice_3.0-en-us.png) 

Resetting a board interrupts any services running on it. If a board is working improperly, rectify the underlying fault â rather than resetting it â to prevent the fault from affecting services.



#### Procedure

1. (Optional) Check the status of a device.
   
   
   ```
   [display device](cmdqueryname=display+device)
   ```
2. Reset a board.
   
   
   ```
   [reset slot](cmdqueryname=reset+slot) slot-id 
   ```
   
   When the device is abnormal and the [**reset slot**](cmdqueryname=reset+slot) command cannot be executed, you can run the [**reset master-mpu force**](cmdqueryname=reset+master-mpu+force) command to forcibly restart the device.

#### Verifying the Configuration

Run the [**display device board reset**](cmdqueryname=display+device+board+reset) { *slot-id* | **all** } command to check the reason why a board is reset.
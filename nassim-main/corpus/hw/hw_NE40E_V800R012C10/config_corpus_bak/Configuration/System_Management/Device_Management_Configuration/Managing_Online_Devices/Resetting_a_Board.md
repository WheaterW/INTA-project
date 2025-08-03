Resetting a Board
=================

During device maintenance, you can use a certain command to reset a board. Before resetting a board, you need to save the configuration file on the board to ensure that the configuration can automatically recover after the board is reset.

#### Context

When an operating board of the device fails, you are advised to reset the board by using the **reset slot** command.

In VS mode, this section applies only to the admin VS.

![](../../../../public_sys-resources/caution_3.0-en-us.png) 

You need to back up important data before resetting a board.



#### Procedure

1. Run [**reset slot**](cmdqueryname=reset+slot) *slot-id* [ **card** *card-id* ] in the user view
   
   
   
   The specified board or subcard is restarted.
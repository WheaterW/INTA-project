Checking Device Voltages
========================

By checking the voltage status of each board on the device, you can know the number of voltage sensors for boards, working status of the voltage sensors, alarm threshold of voltage, and actual voltage.

#### Procedure

1. Run [**display voltage lpu**](cmdqueryname=display+voltage+lpu), [**display voltage ipu**](cmdqueryname=display+voltage+ipu)
   
   
   
   The voltage status of the specified board is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support the [**display voltage lpu**](cmdqueryname=display+voltage+lpu) command.
   
   To check the voltage status of all boards on the Router, run the [**display voltage**](cmdqueryname=display+voltage) command.
   
   In practice, you can run the **display voltage** command in any view to check the voltage status of all the boards on the Router. The voltage information includes the following:
   
   * Number of voltage sensors for the boards.
   * Working status of voltage sensors for the boards.
   * Alarm threshold of the board voltage.
   * Actual voltage of the boards.
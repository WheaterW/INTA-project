Checking Device Temperatures
============================

By checking device temperatures, you can view the current temperature status, temperature alarm threshold, and actual temperature of each board.

#### Procedure

1. Run [**display temperature lpu**](cmdqueryname=display+temperature+lpu), [**display temperature ipu**](cmdqueryname=display+temperature+ipu)
   
   
   
   The working temperature of each module on the specified board is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support the [**display temperature lpu**](cmdqueryname=display+temperature+lpu) command.
   
   To check the temperature of each module of all the boards on the Router, run the [**display temperature**](cmdqueryname=display+temperature) command.
   
   In practice, you can run the **display temperature** command in any view to check the current working temperature of the Router. The temperature information includes the following:
   
   * Current temperature status of the board
   * Alarm threshold of the board temperature
   * Actual temperature of the board
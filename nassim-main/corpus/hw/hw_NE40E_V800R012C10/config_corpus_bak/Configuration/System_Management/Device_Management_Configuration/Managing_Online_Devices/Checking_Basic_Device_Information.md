Checking Basic Device Information
=================================

You can check basic information about the device, including the status of all boards and basic information about a module (for example, power module or fan module) in a certain slot.

#### Procedure

1. Run [**display device**](cmdqueryname=display+device) [ **pic-status** | *slot-id* ]
   
   
   
   Basic information about the device is displayed.
   
   
   
   In practice, you can run this command in any view to check basic information about the device. You can specify the *slot-id* parameter to check basic information about the board in the specified slot.
   
   * To check basic information about a board, run the [**display device**](cmdqueryname=display+device) *slot-id* command.
   * To check basic information about the subcards of each interface board on the device, run the [**display device**](cmdqueryname=display+device) **pic-status** command.
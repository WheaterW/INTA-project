Verifying the CPOS Interface Configuration
==========================================

After you configure a channelized packet over SONET/SDH (CPOS) interface, you can check the clock mode, frame format, overhead byte, and administrative unit group (AUG) multiplexing path of the interface and the clock mode and frame format of its E1 channels. Here, SONET stands for synchronous optical network, and SDH stands for synchronous digital hierarchy.

#### Prerequisites

A CPOS interface has been configured.


#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) **serial**[ *interface-number* ] command to check the status and statistics of a serial interface.
* Run the [**display controller**](cmdqueryname=display+controller) **cpos** [ *cpos-number* ] command to check the status and configurations of a CPOS interface.
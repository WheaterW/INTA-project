Setting a Rate for Subcard Ports
================================

You can set a rate for subcard ports so that the subcard works at a desired rate.

#### Context

A CR5DP2C1HF70 has two ports and works at 2 x 155 Mbit/s or 1 x 622 Mbit/s. To allow the CR5DP2C1HF70 to work at a desired rate, set a rate for the ports on the subcard.

In VS mode, this configuration task is supported only by the admin VS.


#### Procedure

1. Run the [**set service-mode**](cmdqueryname=set+service-mode) **port-rate** { **155** | **622** } **slot** *slot-id* command to configure a rate for subcard ports.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   * After a port rate changes from 155 Mbit/s to 622 Mbit/s, the second port on the CR5DP2C1HF70 is unavailable, and the configurations on the ports are lost.
   * After you run this command, the subcard automatically powers off and then on again and works at the configured rate.
   * Only the NE40E-M2E/-M2F/-M2H/-M2K supports this command.

#### Follow-up Procedure

Run the [**display service-mode port-rate**](cmdqueryname=display+service-mode+port-rate) command to check the current subcard port rate.
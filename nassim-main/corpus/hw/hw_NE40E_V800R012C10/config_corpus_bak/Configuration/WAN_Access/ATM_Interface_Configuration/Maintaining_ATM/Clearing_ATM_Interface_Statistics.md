Clearing ATM Interface Statistics
=================================

You can run the reset commands to clear interface statistics
before recollecting traffic statistics on the interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Interface statistics cannot be restored
after being cleared. Exercise caution when running [**reset**](cmdqueryname=reset) commands.

To clear interface statistics displayed on
the NMS or in the [**display interface**](cmdqueryname=display+interface) command output,
run the following commands in the user view. After the statistics
are cleared, the interface starts to collect statistics again.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

See the relevant NMS manual to learn about how
to view the interface traffic statistics on the NMS.



#### Procedure

* Run the [**reset counters interface**](cmdqueryname=reset+counters+interface) [ **atm** [ *interface-number* ] ] command to clear statistics displayed in the [**display interface**](cmdqueryname=display+interface) command output.
* Run the [**reset counters
  if-mib interface**](cmdqueryname=reset+counters+if-mib+interface) [ **atm** [ *interface-number* ] ] command to clear interface
  statistics displayed on the NMS.
* Run the [**reset atm**](cmdqueryname=reset+atm) **interface** [ **atm** *interface-number* ] command to
  clear PVC statistics of an ATM interface.
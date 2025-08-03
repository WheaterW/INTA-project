Configuring Physical Attributes for the Console User Interface
==============================================================

Physical attributes of the console user interface include the transmission rate, flow control mode, parity bit, stopbits, and databits for the console port.

#### Context

To log in to a router through a console port, you must ensure that physical attributes configured on the terminal emulation program for the console port are the same as those of the console user interface on the router.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration process is supported only on the Admin-VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface**](cmdqueryname=user-interface){ *ui-type* | **console***first-ui-number* }
   
   
   
   The console user interface is displayed.
3. Run [**speed**](cmdqueryname=speed) *speed-value*
   
   
   
   A transmission rate is set.
   
   The value can be 300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, or 115200, in bit/s.
4. Run [**flow-control**](cmdqueryname=flow-control)  *flowtype*
   
   
   
   A flow control mode is set.
5. Run [**parity**](cmdqueryname=parity)  *paritytype*
   
   
   
   A parity bit is set.
6. Run [**stopbits**](cmdqueryname=stopbits)  *stopbitvalue*
   
   
   
   Stopbits are set.
7. Run [**databits**](cmdqueryname=databits)  *databitvalue*
   
   
   
   Data bits are set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Deleting Statistics About PIM Control Messages
==============================================

If you need to re-collect the statistics about PIM control messages, delete the existing statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Deleted statistics about PIM control messages cannot be restored. Therefore, exercise caution when deleting such statistics.



#### Procedure

1. Run the [**reset pim**](cmdqueryname=reset+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **control-message** **counters** [ **interface** *interface-type* *interface-number* ] command in the user view to delete statistics about PIM control messages.
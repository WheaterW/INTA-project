Deleting Statistics About HDLC or IP-Trunk Interfaces
=====================================================

You can run the **reset** command to delete interface statistics before re-collecting traffic statistics on a specified interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Interface statistics cannot be restored after you delete it. Therefore, exercise caution when running the reset command.

To clear interface statistics on the NMS or displayed using the **display interface** command, you can run the [**reset counters interface**](cmdqueryname=reset+counters+interface) command in the user view.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For information on how to view the interface statistics on the NMS, see the NMS manual.



#### Procedure

* Run the [**reset counters interface**](cmdqueryname=reset+counters+interface) [ *interface-type* [ *interface-number* ] ] command to delete interface statistics.
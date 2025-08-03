Deleting Statistics About Packets Transmitted in a BD
=====================================================

Before you collect packet statistics within a specified period in a BD, run the reset command to delete existing statistics. Then you can collect correct packet statistics in the BD.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Once deleted, packet statistics cannot be restored in a BD. Therefore, exercise caution before you decide to delete packet statistics.



#### Procedure

* Run the [**reset bridge-domain**](cmdqueryname=reset+bridge-domain) *bd-id* **statistics** command in the user view to delete packet statistics in a specified BD.
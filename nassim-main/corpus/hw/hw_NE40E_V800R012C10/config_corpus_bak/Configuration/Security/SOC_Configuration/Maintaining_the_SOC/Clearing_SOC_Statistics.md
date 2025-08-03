Clearing SOC Statistics
=======================

SOC statistics can be cleared, including statistics on packets that match ACL rules and statistics on packets to which CAR is implemented after they match ACL rules.

#### Context

After the SOC's attack defense function is enabled, if an interface is attacked, the SOC separately collects statistics on packets that match ACL rules and statistics on packets to which CAR is implemented after they match ACL rules. Before collecting statistics again, clear the existing statistics.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

SOC statistics cannot be restored after they are cleared. Exercise caution when running the reset command.



#### Procedure

* Run the [**reset soc attack-defend statistics**](cmdqueryname=reset+soc+attack-defend+statistics) **slot** *slot-id* command in the user view to clear statistics on packets that match ACL rules and statistics on packets to which CAR is implemented after they match ACL rules on the attacked interfaces on the board in a specified slot.
Maintaining L2TP
================

You can maintain L2TP by disconnecting L2TP tunnels.

#### Context

You can run a command to forcibly disconnect a specified L2TP tunnel only when no user exists, a network fault occurs, or a device requests an L2TP tunnel to be disconnected. An L2TP tunnel cannot be restored after it is disconnected. Exercise caution when running the command.


#### Procedure

1. Run the [**reset l2tp statistics lac tunnel-item**](cmdqueryname=reset+l2tp+statistics+lac+tunnel-item) *tunnel-id* command to clear statistics about LAC protocol packets based on a tunnel ID.
2. Run the [**reset l2tp statistics lns tunnel-item**](cmdqueryname=reset+l2tp+statistics+lns+tunnel-item) *tunnel-id* command to clear statistics about LNS protocol packets based on a tunnel ID.
3. After confirming that you need to disconnect an L2TP tunnel, run the [**reset l2tp tunnel**](cmdqueryname=reset+l2tp+tunnel) { **lac** | **lns** **slot** *slot-id* } { **tunnel-item** *tunnel-id* | **tunnel-name** *remote-name* } command in the user view to forcibly disconnect the L2TP tunnel.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**l2tp tunnel auto-reset enable**](cmdqueryname=l2tp+tunnel+auto-reset+enable) command is run, the device automatically removes an L2TP tunnel if no session control message (ICRP or ICCN) from the remote end is received after 127 or more ICRQ or ICRP messages are sent within 10 minutes. In this case, you do not need to run the **reset l2tp tunnel** command to forcibly disconnect a tunnel.
4. Run the [**reset l2tp down-lns-ip**](cmdqueryname=reset+l2tp+down-lns-ip) { **peer** *lns-ip-address* [ [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-name* ] | [**l2tp-group**](cmdqueryname=l2tp-group) *group-name* | [**tunnel-id**](cmdqueryname=tunnel-id) *tunnel-id* } command to delete a locked LNS IP node with a specified IP address, VPN instance, L2TP group, or tunnel ID on a specified UP.
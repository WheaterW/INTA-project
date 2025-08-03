Using Ping to Check PW Connectivity
===================================

After you configure a virtual private wire service (VPWS) network, use pseudo wire (PW) ping to check PW connectivity on the VPWS network.

#### Prerequisites

Before testing PW connectivity using the [**ping vc**](cmdqueryname=ping+vc) command, ensure that the VPWS network has been configured correctly.

If the control word channel is used, you need to run the [**control-word**](cmdqueryname=control-word) command in the PW template view to enable the control word function.


#### Context

To check whether a PW on the VPWS network is faulty, run the [**ping vc**](cmdqueryname=ping+vc) command. If the PW is up, you can use this command to roughly locate faults, such as forwarding entry loss or errors.

[Table 1](#EN-US_TASK_0172369902__en-us_task_0172373177_tab_dc_vrp_ping_cfg_001301) describes test modes and scenarios.

**Table 1** Test modes of PW ping
| Test Mode | Scenario | Description |
| --- | --- | --- |
| Control-word | Supported in single-segment and multi-segment PW scenarios. | * The MPLS echo request packet carries the control word between the PW label and the IP header. After the destination device receives the packet and finds that it carries the control word, the device sends the packet to the CPU for processing. * This detection mode applies only when you enable the control-word on both ends of the PW. |
| Label-alert | Supported only in single-segment PW scenarios. | * The MPLS echo request packet carries the label-alert tag between the PW label and the LSP label. After the destination device receives the packet and detects that it carries the label-alert tag, the device sends the packet to the CPU for processing. * This detection mode applies only when you enable the label-alert for both ends of the PW. |
| TTL | Supported in single-segment and multi-segment PW scenarios. | You must specify a TTL value to ensure that the TTL expires on the destination device so that the device sends the packet to the CPU for processing. |



#### Procedure

* Control-word mode:
  
  
  
  To monitor PW connectivity using the control-word mode, run the [**ping vc**](cmdqueryname=ping+vc) *vc-type* *pw-id* [ *peer-address* ] [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ]\* **control-word** [ **remote** *remote-ip-address* *peer-pw-id* [ **sender** *sender-address* ] ] [ **ttl** *ttl-value* ] [ **pipe** | **uniform** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command.
  
  To monitor multi-segment PW connectivity, you need to specify the **remote** *remote-ip-address* *peer-pw-id* [ **sender** *sender-address* ] parameter to configure an IP address and a PW ID for the remote PE and specify a source IP address.
  
  To perform a test in a BGP-based scenario, run the [**ping vc vpn-instance**](cmdqueryname=ping+vc+vpn-instance) *vpn-name* *local-ce-id* *remote-ce-id* [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ]\* **control-word** [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command.
* Label-alert mode:
  
  
  
  To monitor PW connectivity using the Label-alert mode, run the [**ping vc**](cmdqueryname=ping+vc) *vc-type* *pw-id* [ *peer-address* ] [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ] \* **label-alert** [ **no-control-word** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command.
  
  To perform a test in a BGP-based scenario, run the [**ping vc vpn-instance**](cmdqueryname=ping+vc+vpn-instance) *vpn-name* *local-ce-id* *remote-ce-id* [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ] \* **label-alert** [ **no-control-word** ] [ **bypass** **-si** *interface-name* | *interface-type* *interface-number* ] command.
* TTL mode:
  
  
  
  To monitor PW connectivity using the TTL mode, run the [**ping vc**](cmdqueryname=ping+vc) *vc-type* *pw-id* [ *peer-address* ] [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ] \* **normal** [ **no-control-word** ] [ **remote** *remote-ip-address* *peer-pw-id* ] [ **ttl** *ttl-value* ] [ **pipe** | **uniform** ] command.
  
  To monitor the connectivity of an MS-PW, you need to specify **remote** *remote-ip-address* *peer-pw-id* [ **ttl** *ttl-value* ] [ **pipe** | **uniform** ] to configure the IP address, PW ID, and TTL value of the remote destination PE.
  
  The [**ping vc**](cmdqueryname=ping+vc) command output contains the following information:
  
  + Response to each ping packet: If no response packet is received within the timeout period, the message reading "Request time out" is displayed. If a response packet is received, the number of data bytes, packet sequence number, TTL value, and response time carried in the packet are displayed.
  + Final statistics: include the number of sent packets, number of received packets, percentage of sent packets with failed responses, and minimum, maximum, and average response times.An example is as follows:
  ```
  <HUAWEI> ping vc ethernet 100 control-word 
     PW PING : FEC 128 PSEUDOWIRE (NEW). Type = ethernet, ID = 100 : 100 data bytes, press CTRL_C to break
      Reply from 10.10.10.10: bytes=100 Sequence=1 time = 140 ms    
      Reply from 10.10.10.10: bytes=100 Sequence=2 time = 40 ms    
      Reply from 10.10.10.10: bytes=100 Sequence=3 time = 30 ms    
      Reply from 10.10.10.10: bytes=100 Sequence=4 time = 50 ms    
      Reply from 10.10.10.10: bytes=100 Sequence=5 time = 50 ms 
  --- FEC: FEC 128 PSEUDOWIRE (NEW). Type = ethernet, ID = 100 ping statistics---
  
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 30/62/140 ms
  ```
  
  A BGP-based example is as follows:
  ```
  <HUAWEI> ping vc vpn-instance vpn1 1 2 -v label-alert 
  PW PING : FEC 128 PSEUDOWIRE (NEW). Type = vlan, ID = 100 : 100 data bytes, press CTRL_C to break
       Reply from 4.4.4.4: bytes=100 Sequence=1 time = 110 ms Return Code 3, Subcode 1
       Reply from 4.4.4.4: bytes=100 Sequence=2 time = 90 ms Return Code 3, Subcode 1
       Reply from 4.4.4.4: bytes=100 Sequence=3 time = 60 ms Return Code 3, Subcode 1
       Reply from 4.4.4.4: bytes=100 Sequence=4 time = 60 ms Return Code 3, Subcode 1
       Reply from 4.4.4.4: bytes=100 Sequence=5 time = 90 ms Return Code 3, Subcode 1
      --- FEC: L2 VPN ENDPOINT. Sender VEID = 1, Remote VEID = 2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 60/82/110 ms 
  ```
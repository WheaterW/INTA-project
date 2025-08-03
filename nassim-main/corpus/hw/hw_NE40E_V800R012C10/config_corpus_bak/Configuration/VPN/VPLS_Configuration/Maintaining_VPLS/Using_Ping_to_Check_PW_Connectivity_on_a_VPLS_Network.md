Using Ping to Check PW Connectivity on a VPLS Network
=====================================================

After you configure a virtual private LAN service (VPLS) network, use pseudo wire (PW) ping to monitor PW connectivity on the VPLS network.

#### Prerequisites

Before you run the [**ping vpls**](cmdqueryname=ping+vpls) command to check PW connectivity, ensure that the VPLS network has been configured correctly.


#### Context

To check whether a PW on the VPLS network is faulty, run the [**ping vpls**](cmdqueryname=ping+vpls) command.


#### Procedure

1. To locate the faulty node on the VPLS network, run either of the following commands as required:
   
   
   * In BGP mode, run the [**ping vpls**](cmdqueryname=ping+vpls) [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ] \* **vsi** *vsi-name* *local-site-id* *remote-site-id* [ **bypass** **-si** *interface-type* *interface-number* ] command.
   * in LDP mode, run the [**ping vpls**](cmdqueryname=ping+vpls) [ **-c** *echo-number* | **-m** *time-value* | **-s** *data-bytes* | **-t** *timeout-value* | **-exp** *exp-value* | **-r** *reply-mode* | **-v** | **-g** ] \* **vsi** *vsi-name* **peer** *peer-address* [ **negotiate-vc-id** *vc-id* ] [ **control-word** [ **remote** *remote-address* *remote-pw-id* [ **sender** *sender-address* ] ] ] [ **bypass** **-si** *interface-type* *interface-number* ] command.
   
   
   
   The [**ping vpls**](cmdqueryname=ping+vpls) command output contains the following information:
   
   * Response to each ping VPLS packet. If no response packet is received after the corresponding timer expires, the message reading "Request time out" is displayed. If a response packet is received, the number of data bytes, packet sequence number, TTL, and response time are displayed.
   * Final statistics: include the number of sent packets, number of received packets, percentage of sent packets with failed responses, and minimum, maximum, and average response times.
   
   For example:
   
   ```
   <HUAWEI> ping vpls vsi a2 peer 10.1.1.1
       PW PING : FEC 128 PSEUDOWIRE (NEW). Type = vlan, ID = 2 : 100 data bytes, press CTRL_C to break
       Reply from 10.1.1.1: bytes=100 Sequence=1 time=60 ms
       Reply from 10.1.1.1: bytes=100 Sequence=2 time=50 ms
       Reply from 10.1.1.1: bytes=100 Sequence=3 time=60 ms
       Reply from 10.1.1.1: bytes=100 Sequence=4 time=60 ms
       Reply from 10.1.1.1: bytes=100 Sequence=5 time=60 ms
   
     --- FEC: FEC 128 PSEUDOWIRE (NEW). Type = vlan, ID = 2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 50/58/60 ms
   
   
   ```
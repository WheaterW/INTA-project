Checking VXLAN Connectivity Using a Ping Operation
==================================================

Checking VXLAN Connectivity Using a Ping Operation

#### Prerequisites

Before checking VXLAN tunnel connectivity using the [**ping vxlan**](cmdqueryname=ping+vxlan) command, ensure that the VXLAN has been configured correctly.


#### Context

Perform the following operations on the VTEPs to be checked.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable the VXLAN ping function on the ping operation initiator.
   
   
   ```
   [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port port-number [ source-ip-interface interface-type interface-number ]
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   This step must be performed if the **-r** *replymode* parameter is set to **3** when the [**ping vxlan**](cmdqueryname=ping+vxlan) command is run on the ping operation initiator.
3. Enable the VXLAN ping function on the responder, and set the monitoring port number on the VXLAN server for the NQA test.
   
   
   ```
   [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port port-number [ source-ip-interface interface-type interface-number ]
   ```
4. Test the IPv4 VXLAN tunnel connectivity.
   
   
   ```
   [ping vxlan](cmdqueryname=ping+vxlan) [ -c count | -m interval | -t timeout | -r replymode | -tos tos | -a innersrc-address ] * vni vniid source source-address peer dest-address [ udp-port dest-port ] [ load-balance { vxlan-source-udpport vxlan-source-udpport [ endvxlansrcudport ] | { source-address lb-src-address destination-address lb-dst-address protocol { udp | lb-protocolid } source-port lb-src-port destination-port lb-dst-port source-mac source-mac destination-mac destination-mac } } ]
   ```
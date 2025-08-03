Checking VXLAN Connectivity Using a Tracert Operation
=====================================================

Checking VXLAN Connectivity Using a Tracert Operation

#### Prerequisites

Before locating a VXLAN tunnel fault using the [**tracert vxlan**](cmdqueryname=tracert+vxlan) command, ensure that the VXLAN has been configured correctly.


#### Context

Perform the following operations on the VTEPs to be checked.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable the VXLAN tracert function on the tracert operation initiator.
   
   
   ```
   [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port port-number [ source-ip-interface interface-type interface-number ]
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   This step must be performed if the **-r** *replymode* parameter is set to **3** when the [**tracert vxlan**](cmdqueryname=tracert+vxlan) command is run on the tracert operation initiator.
3. Enable the VXLAN tracert function on the responder, and set the number of the monitoring port on the VXLAN server for the NQA test.
   
   
   ```
   [nqa vxlanecho enable](cmdqueryname=nqa+vxlanecho+enable) udp-port port-number [ source-ip-interface interface-type interface-number ]
   ```
4. Test the IPv4 VXLAN tunnel connectivity.
   
   
   ```
   [tracert vxlan](cmdqueryname=tracert+vxlan) [ -h maxttl | -t timeout | -r replymode | -a innersrc-address ] * vni vniid source source-address peer dest-address [ udp-port dest-port ] [ pipe ] [ load-balance { vxlan-source-udpport vxlan-source-udpport | { source-address lb-src-address destination-address lb-dst-address protocol { udp | lb-protocolid } source-port lb-src-port destination-port lb-dst-port source-mac lb-sourcemac destination-mac lb-destinationmac } } ]
   ```
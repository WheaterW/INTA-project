Checking the Traffic Statistics of a VPLS PW
============================================

After configuring VPLS traffic statistics collection, check VPLS PW traffic information.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a PW goes down within 5 minutes, traffic before the PW goes down cannot be used to compute the traffic rate in the 5-minute period.


Before checking the public network traffic statistics about a VPLS PW with the specified VSI name, perform the following operations as needed:

* Run the [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) or [**traffic-statistics peer**](cmdqueryname=traffic-statistics+peer) commands in the VSI-LDP view if the target PW is an LDP VPLS PW.
* Run the [**traffic-statistics peer enable**](cmdqueryname=traffic-statistics+peer+enable) command in the VSI-BGP view if the target PW is a BGP VPLS PW.

Run the [**traffic-statistics packet-type enable**](cmdqueryname=traffic-statistics+packet-type+enable) command in the VSI view check packet-type-based traffic statistics about the VPLS PW with the specified VSI name.

After the traffic statistics collection function is configured for a VPLS PW, you can run the following command in any view to check the running status of the traffic on the VPLS PW.


#### Procedure

* Run the [**display traffic-statistics vsi**](cmdqueryname=display+traffic-statistics+vsi) *vsi-name* [ **peer** *peer-address* [ **negotiation-vc-id** *vc-id* | **ldp129** | **remote-site** *remote-site-id* ] ] command to check the statistics about the public network traffic on the LDP/FEC 129/BGP VPLS PW with the specified VSI name.
* Run the [**display traffic-statistics vsi**](cmdqueryname=display+traffic-statistics+vsi) *vsi-name* **suppression** **peer** *peer-address* [ **negotiation-vc-id** *negotiation-vc-id* | **remote-site** *remote-site-id* | **ldp129** ] command to check the traffic suppression statistics of a specified PW.
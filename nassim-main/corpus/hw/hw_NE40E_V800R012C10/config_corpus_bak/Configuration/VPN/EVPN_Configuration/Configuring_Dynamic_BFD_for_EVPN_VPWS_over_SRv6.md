Configuring Dynamic BFD for EVPN VPWS over SRv6
===============================================

To speed up EVPN VPWS over SRv6 convergence when the link status changes, configure dynamic BFD for EVPN VPWS over SRv6. When BFD detects a link fault, it notifies EVPN of the fault and triggers fast EVPN convergence. This feature provides a fast fault detection mechanism for EVPN VPWS over SRv6, speeding up network convergence.

#### Usage Scenario

If a device or link fails, EVPN can use dynamic BFD for fast link convergence. BFD detects faults on EVPN VPWS links within milliseconds. The fast detection speed ensures rapid link switching and minimal traffic loss.

To use BFD sessions to provide link detection for EVPN VPWS over SRv6, configure dynamic BFD for EVPN VPWS over SRv6 on PEs.


#### Pre-configuration Tasks

Before configuring dynamic BFD for EVPN VPWS over SRv6, configure link layer protocol parameters (and IP addresses) for interfaces to ensure that the link layer protocol on the interfaces is up. Then complete one of the following tasks:

* [Configuring EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html)
* [Configuring EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html)
* [Configuring Static EVPN VPWS over SRv6 BE](dc_vrp_evpn_cfg_0230.html)
* [Configuring Static EVPN VPWS over SRv6 TE Policy](dc_vrp_evpn_cfg_0240.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally on the local device.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Enter the EVPL instance view.
   * Run the [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* command to enter the dynamic EVPL instance view.
   * Run the [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* **static-mode** command to enter the static EVPL instance view.
5. Run [**bfd detect**](cmdqueryname=bfd+detect) [ **detect-multiplier** *multiplier* | **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* ] \* [ **track-interface** ]
   
   
   
   BFD for EVPN VPWS over SRv6 is enabled, and BFD session parameters are set.
   
   
   
   command directly The parameters need to be configured based on network conditions and network reliability requirements. Use a short BFD packet transmission interval for links that require high reliability, and a long transmission interval for links that do not require high reliability.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   There are three formulas: Actual interval for the local device to transmit BFD packets = MAX {Locally configured interval for transmitting BFD packets, Remotely configured interval for receiving BFD packets}, Actual interval for the local device to receive BFD packets = MAX {Remotely configured interval for transmitting BFD packets, Locally configured interval for receiving BFD packets}, and Local detection period = Actual interval for receiving BFD packets x Remotely configured BFD detection multiplier.
   
   For example, if the following conditions are met:
   
   * On the local device, the configured interval for transmitting BFD packets is 200 ms, the interval for receiving BFD packets is 300 ms, and the detection multiplier is 4.
   * On the peer device, the configured interval for transmitting BFD packets is 100 ms, the interval for receiving BFD packets is 600 ms, and the detection multiplier is 5.
   
   In this case:
   
   * On the local device, the actual interval for transmitting BFD packets is 600 ms, calculated by using the formula MAX {200 ms, 600 ms}; the interval for receiving BFD packets is 300 ms, calculated by using the formula MAX {100 ms, 300 ms}; the detection period is 1500 ms, calculated by multiplying 300 ms by 5.
   * On the peer device, the actual interval for transmitting BFD packets is 300 ms, calculated by using the formula MAX {100 ms, 300 ms}; the interval for receiving BFD packets is 600 ms, calculated by using the formula MAX {200 ms, 600 ms}; the detection period is 2400 ms, calculated by multiplying 600 ms by 4.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring dynamic BFD for EVPN VPWS, you can run the following command to verify the configuration.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **all for-evpn-vpws** command to check information about BFD sessions established by EVPN VPWS.
* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **evpn-vpws** *evpl-instance-id* **verbose** command to check detailed information about BFD sessions established by EVPN VPWS.
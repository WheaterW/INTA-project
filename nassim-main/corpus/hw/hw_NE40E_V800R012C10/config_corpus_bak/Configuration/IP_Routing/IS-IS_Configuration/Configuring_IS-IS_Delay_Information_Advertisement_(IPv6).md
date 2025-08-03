Configuring IS-IS Delay Information Advertisement (IPv6)
========================================================

To allow IS-IS to collect and flood information about the intra-domain IPv6 link delays, you can enable the advertisement of IPv6 delay information for an IS-IS process.

#### Usage Scenario

Traditional path computation algorithms compute the optimal path to a destination address based on costs. However, such a computed path may not have the minimum delay. For services that have stringent requirements on delay, path computation can be performed based on the delay rather than on the cost to ensure that service traffic is transmitted along the path with the minimum delay. To meet these requirements, enable the advertisement of IPv6 delay information for an IS-IS process. After this function is enabled, IS-IS collects and floods information about the intra-area IPv6 link delay, and BGP-LS reports the information to the controller. This allows the controller to use the delay information to compute the optimal path on the P2P network.


#### Pre-configuration Tasks

Before enabling the advertisement of delay information, complete the following task:

* Configure the TWAMP Light controller to detect delay information.
* [Set the network type of the IS-IS interface to P2P.](dc_vrp_isis_cfg_1027.html)


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and the view is displayed.
   
   
   
   *process-id* specifies an IS-IS process. If the *process-id* parameter is not specified, the system creates process 1 by default. To bind an IS-IS process to a VPN instance, run the [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name* command.
3. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** | **compatible** }
   
   
   
   An IS-IS cost style is set.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) [ **topology** { **compatible** [ **enable-mt-spf** ] | **ipv6** | **standard** } ]
   
   
   
   IPv6 is enabled for the IS-IS process.
5. (Optional) Run [**ipv6 metric-delay normalize**](cmdqueryname=ipv6+metric-delay+normalize) **interval** *interval-value* [ **offset** *offset-value* ]
   
   
   
   The link delay normalization function is configured for the IS-IS process.
   
   
   
   For the delay-based path computation algorithm, the delay differences of links are different, and the differences may be small. However, even if the delay differences are small, only one optimal path can be generated according to the existing SPF algorithm, and load balancing cannot be implemented within a certain delay tolerance range. As a result, link resources on the network cannot be fully utilized. To resolve this problem to the greatest extent, normalization processing may be performed on the link delays with a small difference or a difference within an acceptable range so that load balancing can be implemented and link resources on the network can be fully utilized. Delay variation cannot be normalized.
   
   You can also run the [**isis**](cmdqueryname=isis+ipv6+metric-delay+normalize) [ **process-id** *process-id-value* ] **ipv6 metric-delay** **normalize** **interval** *interval-value* [ **offset** *offset-value* ] command in the IS-IS interface view to configure the link delay normalization function on an interface. If the function is configured both for an IS-IS process and an IS-IS interface, the interface's configuration takes precedence over the process's configuration.
6. Run [**ipv6 traffic-eng**](cmdqueryname=ipv6+traffic-eng) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   IPv6 TE is enabled for a specified level of the IS-IS process.
7. Run [**ipv6 metric-delay advertisement enable**](cmdqueryname=ipv6+metric-delay+advertisement+enable) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   Advertisement of the maximum and minimum IPv6 delay information is configured.
8. Run **[**ipv6 metric-delay average advertisement enable**](cmdqueryname=ipv6+metric-delay+average+advertisement+enable)** [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   The advertisement of the average IPv6 delay is enabled.
9. Run **[**ipv6 metric-delay variation advertisement enable**](cmdqueryname=ipv6+metric-delay+variation+advertisement+enable)** [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   The advertisement of IPv6 delay variation is enabled.
10. (Optional) Run [**ipv6 metric-delay suppress timer**](cmdqueryname=ipv6+metric-delay+suppress+timer) *timer-value* **percent-threshold** *percent-value* **absolute-threshold** *absolute-value*
    
    
    
    Parameters used to suppress the advertisement of IPv6 delay information are configured.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the **[**display isis interface**](cmdqueryname=display+isis+interface) **verbose** **traffic-eng**** command to check information about IS-IS-enabled interfaces.
* Run the **[**display isis traffic-eng advertisements**](cmdqueryname=display+isis+traffic-eng+advertisements)** command to check the TE information advertised by IS-IS.
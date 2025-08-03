Configuring an IS-IS Process to Advertise IPv4 Packet Loss Rates
================================================================

Configuring an IS-IS process to advertise IPv4 packet loss rates helps ensure that service traffic is transmitted along the path with the lowest packet loss rate.

#### Prerequisites

Before configuring an IS-IS process to advertise packet loss rates, complete the following tasks:

* Run the [**cost-style**](cmdqueryname=cost-style) command to set the IS-IS cost style to wide, wide-compatible, or compatible.
* Run the [**traffic-eng**](cmdqueryname=traffic-eng) command to enable IS-IS TE.

#### Context

Traditional path computation algorithms compute the optimal path to a destination address based on costs. However, this path may not be the one with the lowest packet loss rate. For services that have stringent requirements on the packet loss rate, path computation can be performed based on packet loss rates instead of costs to ensure that service traffic is transmitted along the path with the lowest packet loss rate. Specifically, configure an IS-IS process to advertise IPv4 packet loss rates. After this function is configured, IS-IS collects and floods information about intra-area IPv4 packet loss rates, and BGP-LS reports the information to the controller. The controller then computes the optimal path on the P2P network based on the packet loss rates.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to create an IS-IS process and enter its view.
3. Run the [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** | **compatible** } command to set an IS-IS cost style.
4. Run the [**traffic-eng**](cmdqueryname=traffic-eng) [ **level-1** | **level-2** | **level-1-2** ] command to enable IPv4 TE for a specified level of the IS-IS process.
5. Run the [**metric-link-loss advertisement enable**](cmdqueryname=metric-link-loss+advertisement+enable) [ **level-1** | **level-2** | **level-1-2** ] command to configure the function of advertising IPv4 packet loss rates.
6. (Optional) Run the [**metric-link-loss suppress timer**](cmdqueryname=metric-link-loss+suppress+timer) *timer-value* **percent-threshold** *percent-value* **absolute-threshold** *absolute-value* command to configure suppression parameters for packet loss rate advertisement.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The advertised packet loss rates may be dynamic ones measured using TWAMP Light or static ones manually configured.
   
   The valid dynamic packet loss rates measured using TWAMP Light are advertised only to the IS-IS interface bound to the TWAMP Light test session.
   
   After receiving packet loss rate information, IS-IS advertises and floods the information.
7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the **[**display isis interface**](cmdqueryname=display+isis+interface) **verbose** **traffic-eng**** command to check information about IS-IS-enabled interfaces.
* Run the **display isis traffic-eng advertisements** command to check the TE information advertised by IS-IS.
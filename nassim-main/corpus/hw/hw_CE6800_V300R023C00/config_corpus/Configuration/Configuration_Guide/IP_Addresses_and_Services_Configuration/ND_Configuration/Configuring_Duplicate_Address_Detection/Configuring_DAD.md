Configuring DAD
===============

Configuring DAD

#### Prerequisites

Before configuring DAD, you have completed the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is up.
* Configure IPv6 addresses for interfaces.

#### Context

A device can send NS messages to detect whether the IPv6 address to be configured is being used by another device. The number of DAD attempts refers to the number of times NS messages are sent. DAD is similar to gratuitous ARP in IPv4, but implemented using NS and NA messages.

A device can send NS messages to detect whether its neighbors are reachable. You can configure an NS message transmission interval to control the neighbor reachability detection frequency. Do not set a short interval, because although frequent NS message transmissions help rapidly determine whether neighbors are reachable, this negatively impacts system performance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface on which the number of DAD attempts needs to be configured.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure DAD.
   
   
   
   **Table 1** Configuring DAD
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the number of DAD attempts. | [**ipv6 nd dad attempts**](cmdqueryname=ipv6+nd+dad+attempts) *value* | If the number is set to 0, DAD is disabled. |
   | Configure a neighbor reachability detection interval. | [**ipv6 nd ns retrans-timer**](cmdqueryname=ipv6+nd+ns+retrans-timer) *interval* | Frequently sending NS messages causes high CPU usage, which affects system performance. Therefore, you are advised to set a large interval for sending NS messages. The default interval of 1000 ms is recommended. |
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface) [ *interface-type* *interface-number* | **brief** ] command to check DAD configurations.
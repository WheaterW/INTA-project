Configuring BFD for M-LAG
=========================

Configuring BFD for M-LAG

#### Context

In most scenarios, a remote discriminator does not need to be configured for a U-BFD session; instead, only a local discriminator is required. However, in multichassis link aggregation group (M-LAG) scenarios, you need to specify a remote discriminator for the U-BFD session configured to monitor the link between an M-LAG device and a downstream device. Otherwise, the BFD status may be abnormal. For details about M-LAG scenarios, see High Availability Configuration > M-LAG Configuration.


#### Prerequisites

Before configuring BFD for M-LAG, you have completed the following task:

* Configure a U-BFD Echo session.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally and enter the global BFD view.
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Configure a remote discriminator for the U-BFD session.
   ```
   [bfd forwarding match](cmdqueryname=bfd+forwarding+match) remote-discriminator discriminator-value [ to discriminator-value ]
   ```
   
   By default, a remote discriminator is not configured for a U-BFD session.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } [ **verbose** ] command to check BFD session information.
Configuring an Observing Port
=============================

Configuring an Observing Port

#### Context

An observing port forwards the received mirrored traffic to the directly connected monitoring device for analysis. When configuring an observing port, you can also limit the rate of mirrored packets, which applies to the following scenarios:

* The bandwidth of an observing port is higher than that of the connected peer device. In this scenario, you can limit the rate at which the observing port sends mirrored traffic, to prevent congestion or packet loss on the peer device.
* Mirroring and other services are configured on an observing port (not recommended). In this scenario, you can limit the rate of mirrored traffic on the observing port to ensure the bandwidth of other services.

Rate limiting configured on an observing port takes effect on all mirrored traffic (including incoming and outgoing mirrored traffic) received on the observing port.

If a large number of packets need to be mirrored and the monitoring device only needs to analyze packet headers to obtain packet sources, you can configure the function of copying a specified length of original packets to an observing port. This function greatly saves storage space on the monitoring device.

![](public_sys-resources/note_3.0-en-us.png) 

To prevent other services from conflicting with mirroring services, you are advised not to configure other services on observing ports.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an observing port or observing port group. To copy packets to multiple observing ports, you can configure an observing port group.
   
   
   * Configure an observing port.
     ```
     [observe-port](cmdqueryname=observe-port) [ observe-port-index ] interface interface-type interface-number [ cir cir-value [ gbps | kbps | mbps ] ]
     ```
     
     You can specify the **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] parameter to rate limit the mirrored packets.
   * Configure an observing port group.
     ```
     [observe-port group](cmdqueryname=observe-port+group) group-id
     [group-member](cmdqueryname=group-member) { interface-type interface-number [ to interface-type interface-number ] } &<1-8>
     [quit](cmdqueryname=quit)
     ```
3. (Optional) Configure the packet truncation function.
   
   
   ```
   [observe-port packet-length](cmdqueryname=observe-port+packet-length) packet-length
   ```
   
   The specified truncation length of mirrored packets must be an integer multiple of 32. In addition, the actual length of packets to be mirrored is the configured truncation length plus a 4-byte CRC. For example, if the configured length is 64 bytes, the actual length is 68 (64+4) bytes.
   
   By default, the packet truncation function is not configured.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display observe-port**](cmdqueryname=display+observe-port) [ *index* ] command to check the observing port configuration.


#### Follow-up Procedure

Configure an appropriate mirroring function to mirror traffic to an observing port or observing port group.

* [Configuring Local Port Mirroring](galaxy_mirror_cfg_0008.html)
* [Configuring Local VLAN Mirroring](galaxy_mirror_cfg_0022.html)
* [Configuring MQC-based Local Flow Mirroring](galaxy_mirror_cfg_0017.html)
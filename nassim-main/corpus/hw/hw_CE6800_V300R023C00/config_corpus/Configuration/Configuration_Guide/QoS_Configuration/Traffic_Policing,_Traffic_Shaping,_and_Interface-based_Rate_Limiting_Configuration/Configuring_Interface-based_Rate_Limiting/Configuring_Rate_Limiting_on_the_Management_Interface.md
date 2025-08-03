Configuring Rate Limiting on the Management Interface
=====================================================

Configuring Rate Limiting on the Management Interface

#### Context

If there is heavy traffic on the management interface due to malicious attacks or network exceptions, the CPU of the device becomes overloaded, and system operations are impacted. You can configure rate limiting on the management interface to limit the rate of traffic entering the device through the management interface, thereby ensuring the system runs properly.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the management interface view.
   
   
   ```
   [interface](cmdqueryname=interface) meth 0/0/0
   ```
3. Configure rate limiting on the management interface.
   
   
   ```
   [qos lr pps](cmdqueryname=qos+lr+pps) packets
   ```
   
   By default, the rate limit on the management interface is 3000 pps.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   A small rate limit may impact the FTP, Telnet, SFTP, STelnet, and SSH functions.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display this interface**](cmdqueryname=display+this+interface) command in the management interface view. The **Over-car-pps** field in the command output indicates the packets that are discarded due to rate limiting on the management interface.
* Run the [**display interface**](cmdqueryname=display+interface) **meth 0/0/0** command in any view. The **Over-car-pps** field in the command output indicates the packets that are discarded due to rate limiting on the management interface.
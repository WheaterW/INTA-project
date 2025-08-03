Configuring a Loopback Interface
================================

Configuring a Loopback Interface

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a loopback interface and enter the loopback interface view.
   
   
   ```
   [interface loopback](cmdqueryname=interface+loopback) loopback-number
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface loopback**](cmdqueryname=display+interface+loopback) [ *loopback-number* ] command to check the status of the loopback interface.
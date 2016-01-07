
HP Vertica Python Client 7.2.0
------------------------------



Installing
~~~~~~~~~~

Type the following command: ::

    $ sudo pip install <path to wheel>


Check installation: ::

    $ pip show hp-vertica-client
    ---
    Name: hp-vertica-client
    Version: 7.2.1.0
    Location: /usr/local/lib/python2.7/dist-packages
    Requires: 


Uninstalling::

    $ sudo pip uninstall hp-vertica-client

-----------------------------------------------------------------------


Install
-------

Package::

    $ sudo dpkg -i ./vertica_7.2.0-1_amd64.deb

Deployment::

    $ sudo /opt/vertica/sbin/install_vertica --host '127.0.0.1' --deb ./vertica_7.2.0-1_amd64.deb --dba-user daniel --dba-group daniel --data-dir /vertica --license /hdd/Vertica/license/500GB.key --accept-eula


``admintools.conf``::

    install_opts = --hosts '127.0.0.1' --dba-user daniel --dba-group daniel --accept-eula --clean --failure-threshold HALT

``vertica.ini``::

    [Driver]
    DriverManagerEncoding=UTF-16
    ODBCInstLib=/usr/lib/x86_64-linux-gnu/libodbcinst.so
    ErrorMessagesPath=/opt/vertica/lib64
    LogLevel=6
    LogPath=/tmp


``${HOME}/odbc.ini``::

    [Vertica]
    Description = HP Vertica RDBMS
    Driver = /opt/vertica/lib64/libverticaodbc.so
    Database = dev
    Servername = localhost
    UID = daniel
    PWD = letmein
    Port = 5433
    ;;ConnSettings =
    ;;SSLKeyFile = /home/dbadmin/client.key
    ;;SSLCertFile = /home/dbadmin/client.crt
    ;;Locale = en_GB


``${HOME}/.odbcint.ini``::

    [ODBC]
    Threading = 1
    Pooling = Yes
    Trace = Yes
    TraceFile = /tmp/sql.log
    
    
    [HPVertica]
    Description = Vertica
    Driver = /opt/vertica/lib64/libverticaodbc.so

# Install Influx And SNMP

## Installing Influx On Ubuntu

Influx is an open source time series database that can be used to store and analyze time series data. It is written in Go and runs on Linux, macOS, and Windows machines. Installing Influx on Ubuntu is a straightforward process.

### Prerequisites

Before you install Influx, you must make sure you have the following prerequisites:

- A supported version of Ubuntu, such as Ubuntu 18.04 or later
- A working internet connection
- A user account with sudo privileges

### Downloading Influx

To download Influx, open a terminal window and use the following command:

```
wget <https://dl.influxdata.com/influxdb/releases/influxdb_1.8.2_amd64.deb>

```

### Installing Influx

Now that you have downloaded the Influx package, you can install it with these commands:

```
sudo dpkg -i influxdb_1.8.2_amd64.deb
sudo systemctl enable influxdb
sudo systemctl start influxdb

```

### Testing Influx

You can test that Influx is working properly by running the following command:

```
curl -G <http://localhost:8086/query> --data-urlencode "q=SHOW DATABASES"

```

The output should look like this:

```
{
  "results": [
    {
      "statement_id": 0,
      "series": [
        {
          "name": "databases",
          "columns": [
            "name"
          ],
          "values": [
            [
              "_internal"
            ]
          ]
        }
      ]
    }
  ]
}

```

If you get this output, then you have successfully installed Influx on your Ubuntu machine.

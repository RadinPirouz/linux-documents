# Installing Grafana Prometheus

# Installing Grafana on Ubuntu with apt

Installing Grafana on Ubuntu is a relatively simple process. The following steps will guide you through the installation process.

## Prerequisites

Before you begin, you will need to have a working Ubuntu system with apt installed.

## Step 1: Add the Grafana repository

Add the Grafana repository to your system by running the following command:

```
sudo apt-get install apt-transport-https
sudo apt-get install software-properties-common wget
wget -q -O - <https://packages.grafana.com/gpg.key> | sudo apt-key add -
sudo add-apt-repository "deb <https://packages.grafana.com/oss/deb> stable main"

```

## Step 2: Install Grafana

Once the repository is added, you can install Grafana with the following command:

```
sudo apt-get update
sudo apt-get install grafana

```

## Step 3: Start Grafana

Once the installation is complete, start the Grafana server with the following command:

```
sudo service grafana-server start

```

## Step 4: Access the Grafana Dashboard

Once the server is started, you can access the Grafana dashboard by browsing to [http://localhost:3000](http://localhost:3000/) in your web browser. The default username and password are both `admin`.

## Conclusion

You have now successfully installed Grafana on your Ubuntu system using apt. You can now start using Grafana to monitor and visualize your data.

# Installing Prometheus on Ubuntu

Installing Prometheus on Ubuntu is a relatively simple process. The following steps will guide you through the installation process.

## Prerequisites

Before you begin, you will need to have a working Ubuntu system with apt installed.

## Step 1: Add the Prometheus repository

Add the Prometheus repository to your system by running the following command:

```
sudo apt-get install apt-transport-https
echo "deb <https://packages.grafana.com/oss/deb> stable main" | sudo tee -a /etc/apt/sources.list.d/prometheus.list

```

## Step 2: Install Prometheus

Once the repository is added, you can install Prometheus with the following command:

```
sudo apt-get update
sudo apt-get install prometheus

```

## Step 3: Start Prometheus

Once the installation is complete, start the Prometheus server with the following command:

```
sudo service prometheus start

```

## Step 4: Access the Prometheus Dashboard

Once the server is started, you can access the Prometheus dashboard by browsing to [http://localhost:9090](http://localhost:9090/) in your web browser.

## Conclusion

You have now successfully installed Prometheus on your Ubuntu system using apt. You can now start using Prometheus to monitor and visualize your data.

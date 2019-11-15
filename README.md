# Fraud-Analytics-Circular-Trading
Fraud Analytics Using Predictive and Social Network Techniques

# Introduction

In this we try to bring out the companies that have participated in fradulent transactions and to find that out we have focused on the concept of circular trading as explained in the initial report. So the problem finally boils down to finding loops/cycles in the graph of transactions. As the data we used comprises of ___ number of transactions and it wouldn't be possible to find all the loops/cycles with the present avaliable computational resourses. So we have developed the following algorithm, which takes into consideration the loss of data while compression of the graph as well as the optimal compression which fits in the RAM, to detect these potential fraudulent transactions.

## Cycle Detection

Detecting cycles on such a massive transaction data is highly time taking so we first try to group the tractions using two different clustering algorithms.
* Spectral Clustering
* SNN

### Spectral Clustering

We first started off using spectral clustering but then found out that the computation of the eigen values of the lapacian was using up the avaliable resorces and thus ended up aborting the spectral clustering method to find clusters. 

```
Give examples
```

### SNN

Shared Nearest Neighbor (SNN) is a solution to clustering high-dimensional data with the ability to find clusters of varying density. SNN assigns objects to a cluster, which share a large number of their nearest neighbors. We try to group the transactions and then operate on different clusters to find/detect cycles.

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


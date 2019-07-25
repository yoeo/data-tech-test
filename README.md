# Data engineer intern technical test

The goal of this technical test is to check if the candidate
can solve business problems using SQL queries.

## Environment set-up instructions

We will solve the problems using Spark Notebook,
an interactive big-data development environment.

### Requirements:

* Linux operating system is recommended.
  Should also work on Windows and Mac OS but we didn't test that.
* Java 7 or later is installed on your system.
  [Java install instructions](https://java.com/en/download/help/download_options.xml)
* Git is installed on your system.
  [Git install instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Spark Notebook set-up instructions:

#### Using a shell (Linux)

Open a shell on Linux and run the following commands:
```bash
# Download Spark Notebook
wget https://s3.eu-central-1.amazonaws.com/spark-notebook/zip/spark-notebook-0.8.3-scala-2.11.8-spark-2.2.2-hadoop-2.7.3-with-hive.zip?max-keys=100000 -O sparknotebook.zip

# Un-zip Spark Notebook
unzip sparknotebook.zip

# Retrieve the test
cd spark-notebook-0.8.3-scala-2.11.8-spark-2.2.2-hadoop-2.7.3-with-hive/notebooks
git clone https://github.com/yoeo/data-tech-test.git data-tech-test

# Run Spark Notebook
cd ../bin
./spark-notebook
```

Then go to the following URL to pass the test
http://localhost:9000/notebooks/data-tech-test/questions.snb

> The commands could be adapted to run on
> Windows (Powershell, Windows subsystem for Linux) or Mac OS (with Homebrew).

#### Manual set-up (Windows, MacOS or Linux)

1. Download Spark Notebook zip archive from
  http://spark-notebook.io/dl/zip/0.8.3/2.11/2.2.2/2.7.3/true/true
2. Extract content of the zip archive on your computer.
  The Spark Notebook directory should be created with the name
  `spark-notebook-0.8.3-scala-2.11.8-spark-2.2.2-hadoop-2.7.3-with-hive`
3. Go to the `notebooks` directory that is inside the Spark Notebook directory
  and clone this repository using `git`
4. Go to `bin` directory that is inside the Spark Notebook directory
  and run Spark Notebook:
  * On Windows launch `spark-notebook.bat` script
  * On Linux or Mac OS (untested) run `spark-notebook`
5. Finally, open the Notebook and follow the instructions
  http://localhost:9000/notebooks/data-tech-test/questions.snb


## Troubleshooting

If you are not able to set-up Spark Notebook, you can still pass the test.
You can **send by email the answers** to the questions asked this PDF document:
https://github.com/yoeo/data-tech-test/questions.pdf

---

**Happy coding.**

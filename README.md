# static and dynamic analysis of python software replication-package

This is the replication package for the following paper:
Static and Dynamic Analysis of Python Software

## Authors

Daphné Larrivain
<daphne.larrivain@ecole.ensicaen.fr>
ENSICAEN, Caen, France

Shinhyung Yang
<shinhyung.yang@email.uni-kiel.de>
Kiel University, Kiel, Germany

Wilhelm Hasselbring
<hasselbring@email.uni-kiel.de>
Kiel University, Kiel, Germany


## Package structure

### UXsim

[UXsim](https://github.com/toruseo/UXsim) is the app provided for the guided example.

### Tools

[Tools](tools) contains the [kieker](tools/oceandsl-tools/) tool suite and the [static analyser](https://github.com/Misrobody/pyparse#).

### Scripts

[scripts](scripts) contains the pipeline scripts and utilities needed for the guided example.

### Python

[python](python) contains the fix for the sar tool, the graph grouper and the dynamic analysis entrypoint.

### Otkt-gen

[otkt-gen](otkt-gen) contains the collector and the otkt python module necessary for the dynamic analysis.

### Data

[data](data) contains:
 - The pipeline outputs for the 5 timed examples, including all the in between steps and the generated graphs.
 - The monitoring data required to launch the pipeline without having to run the static and/or dynamic analyses before hand.

### Bin

This is where the guided example output will go.

## Replication

The following wil walk you through the complete pipeline using the UXsim application as an example. You can use the same methodology to replicate the other examples.
If you want to try out the pipeline without running the dynamic and static analyses, go straight to 'running the pipeline' and run it with the provided data in `data/monitoring-data`.
Note: it is important to do the static analysis first, as to not skew the static analysis results with the added code for the dynamic analysis intrumentation.

### Static Analysis

From the root, run the static analyzer.

```
time python3 tools/pyparse/src/pyparse/pyparse.py \
 -i UXsim/uxsim \
 -o bin/uxsim-static \
 -m both -e -v
```

### Dynamic analysis

Instrument and install UXsim. The following will prepend `from otkt.tools.instrument import instrument` to all Python files
as well as annotate every function/method definition with `@instrument`
  
```
cd UXsim
../scripts/instrument.sh
# make sure you have the right dependencies.
pip install .
cd ..
```

Build the Otkt utilities (collector and python module).
```
cd otkt-gen
make
cd ..
```

From another terminal, launch the collector.
```
./scripts/collector.sh
```

Now run the entrypoint.

```
python3 python/UXsim-test.py
```

Kieker logs have been create in `/tmp`. Transfer them to the bin directory.
```
ll /tmp/kieker*
cp -r /tmp/kieker* ./bin/
```

## Running the pipeline

Now, run the pipeline.

```
./scripts/combined-model.sh bin/kieker* bin/uxsim-static combined-uxsim
```
